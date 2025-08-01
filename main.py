# main.py - VERSÃO COMPLETA E CORRIGIDA
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
import json
import logging
import uuid
from functools import wraps
from datetime import datetime

# Importa a lógica principal
from logic import generate_plan_logic

# Configuração de logging
logging.basicConfig(
   level=logging.INFO,
   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuração CORS - CORRIGIDA
allowed_origins = os.environ.get("ALLOWED_ORIGINS", "*")
if allowed_origins == "*":
   CORS(app, resources={r"/*": {"origins": "*"}})
else:
   CORS(app, resources={r"/*": {"origins": allowed_origins.split(",")}})

# Configuração do Rate Limiter
limiter = Limiter(
   app=app,
   key_func=get_remote_address,
   default_limits=["200 per day", "50 per hour"]
)

# Chave da API (em produção, use variáveis de ambiente)
API_KEY = os.environ.get('API_KEY', 'your-secret-api-key')

def require_api_key(f):
   @wraps(f)
   def decorated_function(*args, **kwargs):
       api_key = request.headers.get('X-API-Key')
       if api_key != API_KEY:
           logger.warning(f"Unauthorized access attempt from {request.remote_addr}")
           return jsonify({'erro': 'Não autorizado'}), 401
       return f(*args, **kwargs)
   return decorated_function

def generate_request_id():
   """Gera um ID único para cada requisição."""
   return str(uuid.uuid4())

@app.before_request
def before_request():
   """Adiciona request_id ao contexto."""
   request.request_id = generate_request_id()
   logger.info(f"Request {request.request_id} - {request.method} {request.path}")

@app.after_request
def after_request(response):
   """Log da resposta."""
   logger.info(f"Request {request.request_id} - Status: {response.status_code}")
   return response

@app.route('/')
def home():
   """Endpoint raiz."""
   return jsonify({
       'status': 'online',
       'service': 'NutriAPI - Motor de Cálculo Nutricional',
       'version': '4.0.0',
       'timestamp': datetime.utcnow().isoformat()
   })

@app.route('/health')
def health():
   """Health check endpoint."""
   return jsonify({
       'status': 'healthy',
       'timestamp': datetime.utcnow().isoformat()
   })

@app.route('/gerarPlano', methods=['POST'])
@require_api_key
@limiter.limit("10 per minute")
def gerar_plano():
   """Endpoint principal para gerar planos nutricionais."""
   request_id = request.request_id
   
   try:
       # Valida se há dados no request
       if not request.data:
           logger.warning(f"Request {request_id} - Empty request body")
           return jsonify({'erro': 'Dados não fornecidos'}), 400
       
       # Parse do JSON
       try:
           request_data = request.get_json()
       except Exception as e:
           logger.error(f"Request {request_id} - Invalid JSON: {str(e)}")
           return jsonify({'erro': 'JSON inválido'}), 400
       
       # Validação básica dos dados
       if not request_data:
           return jsonify({'erro': 'Dados vazios'}), 400
       
       if 'paciente' not in request_data:
           return jsonify({'erro': 'Dados do paciente não fornecidos'}), 400
       
       if 'metas' not in request_data:
           return jsonify({'erro': 'Metas nutricionais não fornecidas'}), 400
       
       # Log dos dados recebidos (sem dados sensíveis)
       logger.info(f"Request {request_id} - Processing plan for patient")
       
       # Chama a lógica principal
       response, status_code = generate_plan_logic(request_data)
       
       # Log do resultado
       if status_code == 200:
           logger.info(f"Request {request_id} - Plan generated successfully")
       else:
           logger.error(f"Request {request_id} - Error generating plan: {response.get('erro', 'Unknown error')}")
       
       return jsonify(response), status_code
       
   except Exception as e:
       logger.error(f"Request {request_id} - Unexpected error: {str(e)}", exc_info=True)
       return jsonify({
           'erro': 'Erro interno do servidor',
           'request_id': request_id
       }), 500

@app.errorhandler(404)
def not_found(error):
   """Handler para rotas não encontradas."""
   return jsonify({'erro': 'Endpoint não encontrado'}), 404

@app.errorhandler(429)
def ratelimit_handler(e):
   """Handler para rate limit excedido."""
   return jsonify({
       'erro': 'Limite de requisições excedido',
       'mensagem': str(e.description)
   }), 429

@app.errorhandler(500)
def internal_error(error):
   """Handler para erros internos."""
   logger.error(f"Internal server error: {str(error)}", exc_info=True)
   return jsonify({'erro': 'Erro interno do servidor'}), 500

if __name__ == '__main__':
   port = int(os.environ.get('PORT', 5000))
   debug = os.environ.get('FLASK_ENV') == 'development'
   
   if debug:
       app.run(debug=True, host='0.0.0.0', port=port)
   else:
       # Em produção, use um servidor WSGI como gunicorn
       app.run(debug=False, host='0.0.0.0', port=port)
