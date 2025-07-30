from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota padrão (verificar se a API está no ar)
@app.route('/')
def status():
    return "API do Plano Alimentar está funcionando!"

# Nova rota que gera um plano alimentar
@app.route('/gerarPlano', methods=['POST'])
def gerar_plano():
    dados = request.get_json()
    objetivo = dados.get("objetivo", "não informado")
    restricoes = dados.get("restricoes", "nenhuma")

    plano = f"Plano para o objetivo '{objetivo}', com restrições: {restricoes}."
    return jsonify({ "plano": plano })

if __name__ == '__main__':
    app.run()
