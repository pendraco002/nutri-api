# main.py (Versão Final 11.0 - Com Segurança)

from flask import Flask, request, jsonify
from functools import wraps
import os
from logic import generate_plan_logic

app = Flask(__name__)

# Carrega a chave secreta das variáveis de ambiente
API_KEY = os.environ.get("NUTRI_API_KEY")

# --- O "PASSE DE SEGURANÇA" (DECORATOR DE AUTENTICAÇÃO) ---
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Verifica se o header 'X-API-Key' foi enviado na requisição
        if 'X-API-Key' in request.headers and request.headers['X-API-Key'] == API_KEY:
            return f(*args, **kwargs)
        else:
            # Se a chave estiver errada ou ausente, rejeita a chamada
            return jsonify({"erro": "Acesso não autorizado. Chave de API inválida ou ausente."}), 401
    return decorated_function
# ---------------------------------------------------------

@app.route('/', methods=['GET'])
def verificar_status():
    return jsonify({ "status": "NutriAPI Engine v11.0 (Blindada) está online e operacional." })

@app.route('/gerarPlano', methods=['POST'])
@require_api_key  # Aplica o "Passe de Segurança" a este endpoint
def gerar_plano():
    request_data = request.get_json()
    if not request_data:
        return jsonify({"erro": "Requisição JSON inválida ou vazia."}), 400
    
    # Chama a lógica principal para gerar o plano
    response, status_code = generate_plan_logic(request_data)
    return jsonify(response), status_code

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
