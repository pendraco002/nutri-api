# Arquivo: main.py (Versão Pedro Barros)

from flask import Flask, request, jsonify
from planner import create_pedro_barros_plan # Importa a nova função específica
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verificar_status():
    """ Endpoint para verificar se a API está online. """
    return jsonify({ "mensagem": "API Nutri-Core 'Pedro Barros' v2.0 está funcionando." })

@app.route('/gerarPlano', methods=['POST'])
def gerar_plano_endpoint():
    """
    Endpoint principal que recebe o pedido do GPT e retorna o plano formatado.
    """
    try:
        # No futuro, você pode usar os dados recebidos para customizar o plano.
        # Por enquanto, estamos gerando o plano padrão.
        # dados = request.get_json()
        # objetivo = dados.get("objetivo", "não informado")
        # restricoes = dados.get("restricoes", "nenhuma")

        # Chama a função que gera o plano no formato exato de Pedro Barros
        plano_texto_completo = create_pedro_barros_plan()

        # Retorna o plano como uma string dentro de um objeto JSON
        return jsonify({ "plano": plano_texto_completo })

    except Exception as e:
        print(f"Erro ao gerar plano: {e}")
        return jsonify({"error": "Ocorreu um erro interno ao processar o plano."}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
