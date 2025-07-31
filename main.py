# main.py - VERSÃO FINAL COM SEGURANÇA APRIMORADA
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
import json
import time
import logging
import traceback
from functools import wraps
from datetime import datetime
import uuid
import hashlib

# Importações internas
from logic import generate_plan_logic

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('nutri-api')

# Inicialização do aplicativo
app = Flask(__name__)

# CORS mais restritivo
allowed_origins = os.environ.get("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
CORS(app, resources={r"/*": {"origins": allowed_origins}})

# Rate limiting
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)

# Carrega a chave secreta com hash
API_KEY = os.environ.get("NUTRI_API_KEY", "default_key_change_in_production")
API_KEY_HASH = hashlib.sha256(API_KEY.encode()).hexdigest()

# Configurações de segurança
MAX_CONTENT_LENGTH = 1 * 1024 * 1024  # 1MB max payload
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Middleware de autenticação aprimorado
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        request_id = str(uuid.uuid4())
        start_time = time.time()
        
        # Log da requisição
        logger.info(f"Request {request_id} recebido: {request.path} from {request.remote_addr}")
        
        # Verificação de API Key
        provided_key = request.headers.get('X-API-Key', '')
        if not provided_key:
            logger.warning(f"Request {request_id} rejeitado: Chave ausente")
            return jsonify({"erro": "Acesso não autorizado"}), 401
            
        # Comparação segura
        provided_hash = hashlib.sha256(provided_key.encode()).hexdigest()
        if provided_hash != API_KEY_HASH:
            logger.warning(f"Request {request_id} rejeitado: Chave inválida")
            return jsonify({"erro": "Acesso não autorizado"}), 401
        
        # Validação de content-type
        if request.method == 'POST' and not request.is_json:
            logger.warning(f"Request {request_id}: Content-Type inválido")
            return jsonify({"erro": "Content-Type deve ser application/json"}), 400
        
        try:
            result = f(*args, **kwargs, request_id=request_id)
            
            # Log de performance
            execution_time = time.time() - start_time
            logger.info(f"Request {request_id} concluído em {execution_time:.2f}s")
            
            return result
            
        except Exception as e:
            logger.error(f"Request {request_id} erro: {str(e)}")
            logger.error(traceback.format_exc())
            
            return jsonify({
                "erro": "Erro interno do servidor",
                "request_id": request_id,
                "timestamp": datetime.now().isoformat()
            }), 500
    
    return decorated_function

# Validador de payload
def validate_payload(data):
    """Valida estrutura do payload."""
    errors = []
    
    # Validação de estrutura
    if not isinstance(data, dict):
        errors.append("Payload deve ser um objeto JSON")
        
    if "paciente" not in data:
        errors.append("Campo 'paciente' é obrigatório")
    else:
        paciente = data["paciente"]
        if not isinstance(paciente, dict):
            errors.append("'paciente' deve ser um objeto")
        elif "peso_kg" not in paciente:
            errors.append("'paciente.peso_kg' é obrigatório")
        elif not isinstance(paciente["peso_kg"], (int, float)) or paciente["peso_kg"] <= 0:
            errors.append("'paciente.peso_kg' deve ser um número positivo")
            
    if "metas" in data:
        metas = data["metas"]
        if not isinstance(metas, dict):
            errors.append("'metas' deve ser um objeto")
        else:
            if "kcal_total" in metas:
                kcal = metas["kcal_total"]
                if not isinstance(kcal, (int, float)) or kcal < 1000 or kcal > 5000:
                    errors.append("'metas.kcal_total' deve estar entre 1000 e 5000")
                    
    return errors

# Sanitizador de strings
def sanitize_string(value, max_length=100):
    """Sanitiza strings do input."""
    if not isinstance(value, str):
        return str(value)[:max_length]
    
    # Remove caracteres perigosos
    sanitized = value.strip()
    sanitized = sanitized.replace('\n', ' ').replace('\r', ' ')
    sanitized = ''.join(char for char in sanitized if char.isprintable())
    
    return sanitized[:max_length]

# ENDPOINTS

@app.route('/health', methods=['GET'])
def health_check():
    """Verificação de saúde do serviço."""
    try:
        # Testa imports críticos
        from database import get_food_data
        foods = get_food_data()
        
        health_status = {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "version": "4.0",
            "database": {
                "foods_count": len(foods),
                "status": "connected"
            }
        }
        
        return jsonify(health_status), 200
        
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 503

@app.route('/', methods=['GET'])
def verificar_status():
    """Status da API."""
    return jsonify({ 
        "status": "NutriAPI Engine v4.0 está online",
        "timestamp": datetime.now().isoformat(),
        "endpoints": {
            "/": "GET - Status",
            "/health": "GET - Health check",
            "/gerarPlano": "POST - Gerar plano nutricional"
        }
    })

@app.route('/gerarPlano', methods=['POST'])
@require_api_key
@limiter.limit("30 per hour")
def gerar_plano(request_id):
    """Gera plano nutricional personalizado."""
    
    try:
        # Obter e validar dados
        request_data = request.get_json(force=True)
        
        # Validação de payload
        validation_errors = validate_payload(request_data)
        if validation_errors:
            logger.warning(f"Request {request_id} validação falhou: {validation_errors}")
            return jsonify({
                "erro": "Dados inválidos",
                "detalhes": validation_errors
            }), 400
        
        # Sanitização de dados
        if "paciente" in request_data and "nome" in request_data["paciente"]:
            request_data["paciente"]["nome"] = sanitize_string(
                request_data["paciente"]["nome"], 
                max_length=50
            )
        
        # Adicionar metadados
        request_data["_meta"] = {
            "request_id": request_id,
            "timestamp": datetime.now().isoformat(),
            "ip": request.remote_addr
        }
        
        # Log do request sanitizado
        logger.info(f"Request {request_id} processando para: {request_data.get('paciente', {}).get('nome', 'Unknown')}")
        
        # Gerar plano
        response, status_code = generate_plan_logic(request_data)
        
        # Adicionar request_id à resposta
        if isinstance(response, dict):
            response["request_id"] = request_id
        
        # Log de sucesso/falha
        if status_code == 200:
            logger.info(f"Request {request_id} plano gerado com sucesso")
        else:
            logger.warning(f"Request {request_id} falha na geração: {status_code}")
        
        return jsonify(response), status_code
        
    except json.JSONDecodeError:
        logger.error(f"Request {request_id} JSON inválido")
        return jsonify({"erro": "JSON inválido"}), 400
        
    except Exception as e:
        logger.error(f"Request {request_id} erro inesperado: {str(e)}")
        logger.error(traceback.format_exc())
        
        return jsonify({
            "erro": "Erro interno ao processar requisição",
            "request_id": request_id,
            "timestamp": datetime.now().isoformat()
        }), 500

# Error handlers
@app.errorhandler(413)
def request_entity_too_large(error):
    """Payload muito grande."""
    return jsonify({
        "erro": "Payload muito grande",
        "max_size": f"{MAX_CONTENT_LENGTH / 1024 / 1024}MB"
    }), 413

@app.errorhandler(429)
def ratelimit_handler(e):
    """Rate limit excedido."""
    return jsonify({
        "erro": "Limite de requisições excedido",
        "mensagem": str(e.description),
        "retry_after": e.retry_after
    }), 429

@app.errorhandler(500)
def internal_error(error):
    """Erro interno."""
    return jsonify({
        "erro": "Erro interno do servidor",
        "timestamp": datetime.now().isoformat()
    }), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    
    # Em produção, usar gunicorn
    if os.environ.get("FLASK_ENV") == "production":
        app.run(host="0.0.0.0", port=port)
    else:
        # Desenvolvimento
        app.run(host="0.0.0.0", port=port, debug=True)
