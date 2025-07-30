# main.py (Versão de Produção v2.0)

from flask import Flask, request, jsonify
from logic import generate_plan_logic
import os
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verificar_status():
    """Endpoint para verificar a saúde da API."""
    app.logger.info("Status check: OK")
    return jsonify({"status": "NutriAPI Engine v2.0 está online e operacional."})

@app.route('/gerarPlano', methods=['POST'])
def gerar_plano_endpoint():
    """Endpoint principal que recebe a chamada do GPT."""
    app.logger.info("Recebida nova requisição para /gerarPlano")
    
    if not request.is_json:
        app.logger.warning("Requisição recebida sem o content-type application/json.")
        return jsonify({"erro": "Header 'Content-Type' deve ser 'application/json'."}), 415

    try:
        request_data = request.get_json()
        app.logger.info(f"Payload recebido: {request_data}")
        
        # Chama o motor de lógica para processar os dados
        response_data, status_code = generate_plan_logic(request_data)
        
        if status_code == 200:
            app.logger.info("Plano gerado com sucesso.")
        else:
            app.logger.error(f"Erro na lógica de geração: {response_data.get('erro')}")
            
        return jsonify(response_data), status_code

    except Exception as e:
        app.logger.critical(f"Erro inesperado no servidor: {e}", exc_info=True)
        return jsonify({"erro": "Ocorreu um erro interno inesperado no servidor."}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False) # Debug desativado para produção
