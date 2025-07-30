# main.py (Versão simplificada sem dependências problemáticas)
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
import time
import logging
import traceback
from functools import wraps
from datetime import datetime
import uuid

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
CORS(app, resources={r"/*": {"origins": os.environ.get("ALLOWED_ORIGINS", "*")}})

# Carrega a chave secreta
API_KEY = os.environ.get("NUTRI_API_KEY")

# --- MIDDLEWARE DE AUTENTICAÇÃO ---
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        request_id = str(uuid.uuid4())
        
        # Log da requisição recebida
        logger.info(f"Request {request_id} recebido: {request.path}")
        start_time = time.time()
        
        # Verificação de segurança
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
        "version": "12.0"
    }
    
    return jsonify(health_status), 200

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
        "timestamp": datetime.now().isoformat()
    }
    
    # Geração do plano com tratamento de exceções
    try:
        response, status_code = generate_plan_logic(request_data)
        
        # Log do resultado
        success = status_code == 200
        log_method = logger.info if success else logger.warning
        log_method(f"Request {request_id} geração de plano: {'Sucesso' if success else 'Falha'}")
        
        return jsonify(response), status_code
        
    except Exception as e:
        # Erro genérico
        logger.error(f"Request {request_id} erro inesperado: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({
            "erro": "Erro interno ao processar a requisição",
            "request_id": request_id
        }), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
