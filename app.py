# -*- coding: utf-8 -*-
"""
Ponto de Entrada da Aplicação Web (API) - Sistema de Nutrição

Este arquivo implementa uma API Flask para o sistema de geração de planos
alimentares. Ele expõe um endpoint seguro que recebe dados do paciente e,
utilizando a lógica de negócio encapsulada no módulo 'nutri_engine', retorna
um plano nutricional completo e personalizado.

Arquitetura da API:
1.  **Framework:** Utiliza Flask, um micro-framework Python leve e robusto.
2.  **Segurança:** O acesso ao endpoint principal é protegido por uma chave de API
    enviada no cabeçalho `X-API-KEY`.
3.  **Endpoint (`/gerarPlano`):** Um único endpoint que aceita requisições
    `POST` com um corpo JSON contendo os dados do paciente e suas metas.
4.  **Separação de Responsabilidades:** Este arquivo foca na camada de API
    (roteamento, autenticação, validação). A lógica complexa de geração de
    planos é delegada ao módulo `nutri_engine.py`.
"""

import os
from functools import wraps
from flask import Flask, request, jsonify
from nutri_engine import generate_complete_meal_plan

# =============================================================================
# CONFIGURAÇÃO DA APLICAÇÃO FLASK
# =============================================================================

app = Flask(__name__)

# Carrega a chave de API das variáveis de ambiente.
API_KEY = os.environ.get("API_KEY")

# Decorator para proteger rotas com a chave de API
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not API_KEY:
            # Erro de configuração do servidor
            return jsonify({"error": "API Key not configured on the server."}), 500

        key = request.headers.get('X-API-Key')
        if not key or key != API_KEY:
            return jsonify({"error": "Unauthorized. Invalid or missing API Key."}), 401
        
        return f(*args, **kwargs)
    return decorated_function

# =============================================================================
# DEFINIÇÃO DOS ENDPOINTS DA API
# =============================================================================

@app.route('/gerarPlano', methods=['POST'])
@require_api_key
def handle_generate_plan():
    """
    Endpoint principal para a geração de planos alimentares.
    Espera um JSON com os dados do paciente e retorna o plano completo.
    """
    # 1. Obter e validar dados de entrada
    request_data = request.get_json()
    if not request_data:
        return jsonify({"error": "Invalid input. Request body must be a valid JSON."}), 400

    if 'paciente' not in request_data or 'metas' not in request_data:
        return jsonify({
            "error": "Missing required keys in request body.",
            "missing": ["paciente", "metas"]
        }), 400

    # 2. Chamar a lógica de negócio para gerar o plano
    try:
        meal_plan_response = generate_complete_meal_plan(request_data)
    except Exception as e:
        # Captura erros inesperados da lógica de negócio
        app.logger.error(f"Error during meal plan generation: {e}")
        return jsonify({"error": "An internal error occurred while generating the meal plan."}), 500

    # 3. Retornar o plano gerado com sucesso
    return jsonify(meal_plan_response), 200

@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint de verificação de saúde (health check).
    Usado por serviços de monitoramento para verificar se a aplicação está online.
    """
    return jsonify({"status": "ok"}), 200

# =============================================================================
# PONTO DE ENTRADA PARA EXECUÇÃO LOCAL
# =============================================================================

if __name__ == '__main__':
    # O host '0.0.0.0' torna a aplicação acessível na rede local.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
