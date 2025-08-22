from flask import Flask, request, jsonify
from logic import gerar_plano_personalizado
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # permite chamadas da web/GPT

# Carrega a chave da API a partir da variável de ambiente
API_KEY = os.environ.get("API_KEY")


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API do Plano Nutricional Pedro Barros"}), 200


@app.route("/gerarPlano", methods=["POST"])
def gerar_plano():
    # 🔐 Verificação de autenticação com chave de API
    key = request.headers.get("API_KEY")
    if key != API_KEY:
        return jsonify({"erro": "Não autorizado"}), 401

    try:
        # 🔎 Extrai os dados do corpo da requisição
        dados = request.get_json()

        # ⚙️ Gera o plano nutricional com base nos dados
        plano_formatado, resumo_nutricional, substituicoes = gerar_plano_personalizado(dados)

        # 📦 Monta a resposta para a GPT
        resposta = {
            "plano_formatado": plano_formatado,
            "resumo_nutricional": resumo_nutricional,
            "refeicoes": substituicoes
        }

        return jsonify(resposta), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=10000)
