# main.py (Versão Final 12.0 - Segurança Avançada e Integridade de Dados)

from flask import Flask, request, jsonify, Response
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
from pydantic import ValidationError

# Importações internas
from logic import generate_plan_logic
from database import validate_food_data

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('nutri-api')

# Verificação inicial da integridade da base de dados
data_validation = validate_food_data()
if not data_validation["valid"]:
    for error in data_validation["errors"]:
        logger.error(f"ERRO CRÍTICO DE DADOS: {error}")
    # Em ambiente de produção, pode-se decidir se o servidor deve iniciar com erros
    # raise SystemExit("Database integrity errors detected. Server startup aborted.")

# Inicialização do aplicativo
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": os.environ.get("ALLOWED_ORIGINS", "*")}})

# Configuração do limitador de taxa
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per day", "20 per hour"],
    storage_uri=os.environ.get("REDIS_URL", "memory://"),
)

# Carrega a chave secreta e outras configurações
API_KEY = os.environ.get("NUTRI_API_KEY")
STRICT_MODE = os.environ.get("STRICT_VALIDATION", "true").lower() == "true"
ENFORCE_GRAMATURA = os.environ.get("ENFORCE_GRAMATURA", "true").lower() == "true"
MAX_NUTRITIONAL_DEVIATION = int(os.environ.get("MAX_NUTRITIONAL_DEVIATION", "5"))

# --- MIDDLEWARE DE AUTENTICAÇÃO AVANÇADA ---
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        request_id = str(uuid.uuid4())
        
        # Log da requisição recebida
        logger.info(f"Request {request_id} recebido: {request.path}")
        start_time = time.time()
        
        # Verificação de segurança multi-camada
        if 'X-API-Key' not in request.headers:
            logger.warning(f"Request {request_id} rejeitado: Chave de API ausente")
            return jsonify({"erro": "Acesso não autorizado. Chave de API ausente."}), 401
            
        if request.headers['X-API-Key'] != API_KEY:
            logger.warning(f"Request {request_id} rejeitado: Chave de API inválida")
            return jsonify({"erro": "Acesso não autorizado. Chave de API inválida."}), 401
        
        # Executa a função principal
        try:
            result = f(*args, **kwargs, request_id=request_id)
            
            # Log de finalização e tempo de execução
            execution_time = time.time() - start_time
            logger.info(f"Request {request_id} finalizado em {execution_time:.2f}s")
            
            return result
        except Exception as e:
            # Log detalhado do erro
            logger.error(f"Request {request_id} falhou: {str(e)}")
            logger.error(traceback.format_exc())
            return jsonify({
                "erro": "Erro interno do servidor",
                "request_id": request_id,
                "timestamp": datetime.now().isoformat()
            }), 500
    
    return decorated_function

# --- ENDPOINT DE VERIFICAÇÃO DE SAÚDE ---
@app.route('/health', methods=['GET'])
def health_check():
    # Verificação rápida dos componentes essenciais
    health_status = {
        "status": "online",
        "timestamp": datetime.now().isoformat(),
        "version": "12.0",
        "database_valid": data_validation["valid"],
        "warnings": len(data_validation.get("warnings", [])),
        "config": {
            "strict_mode": STRICT_MODE,
            "enforce_gramatura": ENFORCE_GRAMATURA,
            "max_nutritional_deviation": MAX_NUTRITIONAL_DEVIATION
        }
    }
    
    status_code = 200 if health_status["database_valid"] else 500
    return jsonify(health_status), status_code

# --- ENDPOINT PRINCIPAL ---
@app.route('/', methods=['GET'])
def verificar_status():
    return jsonify({ 
        "status": "NutriAPI Engine v12.0 (Segurança Avançada) está online e operacional.",
        "timestamp": datetime.now().isoformat()
    })

# --- ENDPOINT DE GERAÇÃO DE PLANOS ---
@app.route('/gerarPlano', methods=['POST'])
@require_api_key
@limiter.limit("10/minute")  # Limite específico para este endpoint
def gerar_plano(request_id):
    """Gera um plano nutricional baseado nos parâmetros enviados."""
    
    # Validação de conteúdo
    if not request.is_json:
        logger.warning(f"Request {request_id}: Conteúdo não é JSON")
        return jsonify({"erro": "Requisição deve ser enviada no formato JSON"}), 400
        
    request_data = request.get_json()
    
    # Validação básica dos dados de entrada
    if not request_data:
        logger.warning(f"Request {request_id}: JSON vazio")
        return jsonify({"erro": "Requisição JSON vazia."}), 400
        
    if "paciente" not in request_data:
        logger.warning(f"Request {request_id}: Dados do paciente ausentes")
        return jsonify({"erro": "Dados do paciente são obrigatórios."}), 400
    
    # Enriquecimento dos dados com configurações
    request_data["_meta"] = {
        "request_id": request_id,
        "timestamp": datetime.now().isoformat(),
        "config": {
            "strict_mode": STRICT_MODE,
            "enforce_gramatura": ENFORCE_GRAMATURA,
            "max_nutritional_deviation": MAX_NUTRITIONAL_DEVIATION
        }
    }
    
    # Geração do plano com tratamento de exceções
    try:
        response, status_code = generate_plan_logic(request_data)
        
        # Log do resultado
        success = status_code == 200
        log_method = logger.info if success else logger.warning
        log_method(f"Request {request_id} geração de plano: {'Sucesso' if success else 'Falha'}")
        
        return jsonify(response), status_code
        
    except ValidationError as ve:
        # Erro específico de validação Pydantic
        logger.warning(f"Request {request_id} erro de validação: {str(ve)}")
        return jsonify({
            "erro": "Erro de validação dos dados",
            "detalhes": str(ve),
            "request_id": request_id
        }), 422
        
    except Exception as e:
        # Erro genérico
        logger.error(f"Request {request_id} erro inesperado: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({
            "erro": "Erro interno ao processar a requisição",
            "request_id": request_id
        }), 500

# --- ENDPOINT DE VALIDAÇÃO ---
@app.route('/validarPlano', methods=['POST'])
@require_api_key
def validar_plano(request_id):
    """Valida um plano existente sem gerar um novo."""
    if not request.is_json:
        return jsonify({"erro": "Requisição deve ser enviada no formato JSON"}), 400
        
    try:
        plano = request.get_json()
        # Aqui poderia chamar uma função dedicada para validação
        from logic import NutriPlanIntegrityValidator
        validator = NutriPlanIntegrityValidator(strict_mode=STRICT_MODE)
        resultado = validator.validate(plano)
        
        return jsonify({
            "valido": resultado.get("_validation", {}).get("passed", False),
            "erros": resultado.get("_validation", {}).get("errors", []),
            "plano_corrigido": resultado
        })
    except Exception as e:
        logger.error(f"Request {request_id} erro ao validar plano: {str(e)}")
        return jsonify({
            "erro": "Erro ao validar o plano",
            "detalhes": str(e),
            "request_id": request_id
        }), 500

# --- BLOCO DE INICIALIZAÇÃO ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    
    # Modo de desenvolvimento
    debug_mode = os.environ.get("FLASK_ENV") == "development"
    
    if debug_mode:
        app.run(host="0.0.0.0", port=port, debug=True)
    else:
        # Para produção, é mais seguro usar um servidor WSGI como gunicorn
        import waitress
        logger.info(f"Iniciando servidor em modo produção na porta {port}")
        waitress.serve(app, host="0.0.0.0", port=port, threads=4)
