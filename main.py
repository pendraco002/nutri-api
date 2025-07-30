# Arquivo: main.py (Versão Final)

from flask import Flask, request, jsonify
from planner import create_formatted_plan # Importa a nova função
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verificar_status():
    """ Endpoint para verificar se a API está online. """
    return jsonify({ "mensagem": "API Nutri-Core 'Pedro Barros' está funcionando." })

@app.route('/gerarPlano', methods=['POST'])
def gerar_plano_endpoint():
    """
    Endpoint principal que recebe o pedido do GPT e retorna o plano formatado.
    """
    try:
        dados = request.get_json()
        objetivo = dados.get("objetivo", "não informado")
        restricoes = dados.get("restricoes", "nenhuma")

        # Chama a função principal do planner para gerar a string formatada
        plano_texto_completo = create_formatted_plan(objetivo, restricoes)

        # Retorna o plano como uma string dentro de um objeto JSON
        return jsonify({ "plano": plano_texto_completo })

    except Exception as e:
        # Em caso de erro no nosso código, informa o GPT
        print(f"Erro ao gerar plano: {e}")
        return jsonify({"error": "Ocorreu um erro interno ao processar o plano."}), 500

if __name__ == "__main__":
    # Configuração para funcionar no Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
