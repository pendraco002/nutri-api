from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verificar_status():
    return jsonify({ "mensagem": "A API está funcionando corretamente." })

@app.route('/gerarPlano', methods=['POST'])
def gerar_plano():
    dados = request.get_json()
    objetivo = dados.get("objetivo", "não informado")
    restricoes = dados.get("restricoes", "nenhuma")

    plano = f"Plano para o objetivo '{objetivo}', com restrições: {restricoes}."
    return jsonify({ "plano": plano })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
