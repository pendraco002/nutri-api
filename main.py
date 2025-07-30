@app.route('/gerarPlano', methods=['POST'])
def gerar_plano():
    dados = request.get_json()
    objetivo = dados.get("objetivo", "não informado")
    restricoes = dados.get("restricoes", "nenhuma")

    plano = f"Plano para o objetivo '{objetivo}', com restrições: {restricoes}."
    return jsonify({ "plano": plano })
