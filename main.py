from flask import Flask, request, jsonify
from planner import create_meal_plan
import os

app = Flask(__name__)

@app.route('/')
def verificar_status():
    return "API Nutri Online!"

@app.route('/gerarPlano', methods=['POST'])
def gerar_plano():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Nenhum dado JSON fornecido."}), 400

        # Extrair dados do request
        objetivo = data.get('objetivo')
        restricoes = data.get('restricoes')

        # Aqui, o Custom GPT deve enviar os dados do paciente de forma estruturada
        # para que o planner.py possa processá-los. O 'objetivo' e 'restricoes'
        # da API OpenAPI são strings, então o GPT precisará parsear e enviar
        # um JSON mais detalhado para o planner.py.
        # Por enquanto, vamos simular o parsing de um input mais detalhado
        # que o GPT enviaria para o planner.

        # Exemplo de como o GPT pode formatar o 'objetivo' e 'restricoes' para o planner:
        # objetivo: "Gerar plano de 2000 kcal com no mínimo 170g de proteína, máximo de 35% de carboidratos e 25% de gordura, para ganho de massa muscular."
        # restricoes: "Sem lactose, não incluir brócolis. Plano para 5 refeições diárias, com treino nos dias de semana. Incluir opção de hambúrguer artesanal no jantar."

        # O GPT precisará ser instruído a enviar um JSON mais completo para o planner.
        # Por simplicidade, vamos criar um dicionário de dados do paciente aqui.
        # Em um cenário real, o GPT faria o parsing das strings 'objetivo' e 'restricoes'
        # para preencher este dicionário ou a API seria mais flexível.

        # Placeholder para os dados do paciente que o GPT deveria inferir/enviar
        # Você precisará ajustar isso para como o GPT realmente enviará os dados.
        patient_data = {
            "nome": "Usuário",
            "sexo": "masculino", # Exemplo
            "peso": 80, # Exemplo
            "altura": 180, # Exemplo
            "idade": 30, # Exemplo
            "objetivo": 

objetivo, # Usar o objetivo passado pela API
            "restricoes": restricoes, # Usar as restrições passadas pela API
            "num_refeicoes": 5, # Exemplo, o GPT deve inferir
            "dias_treino": ["segunda", "quarta", "sexta"], # Exemplo, o GPT deve inferir
            "incluir_pre_treino": True, # Exemplo, o GPT deve inferir
            "meta_calorias": None, # O GPT pode preencher se souber
            "proteina_min_g": None, # O GPT pode preencher se souber
            "carb_max_perc": None, # O GPT pode preencher se souber
            "gordura_max_perc": None, # O GPT pode preencher se souber
            "fibras_min_g": None, # O GPT pode preencher se souber
        }

        # Aqui é onde o GPT, ao chamar a API, deve ser inteligente para
        # extrair os dados do usuário e formatá-los para o `patient_data`.
        # A API `gerarPlano` do OpenAPI tem apenas `objetivo` e `restricoes` como strings.
        # O GPT precisará ser instruído a criar uma string JSON dentro desses campos
        # ou a API precisaria ser redesenhada para receber um JSON mais complexo.
        # Por enquanto, a `create_meal_plan` espera um dicionário.
        # Para fins de demonstração, vamos tentar extrair alguns dados simples
        # das strings `objetivo` e `restricoes`.

        # Exemplo de parsing simplificado (o GPT fará isso de forma mais robusta)
        if "kcal" in objetivo:
            try:
                patient_data["meta_calorias"] = int(objetivo.split("kcal")[0].split()[-1])
            except ValueError: pass
        if "proteina" in objetivo:
            try:
                patient_data["proteina_min_g"] = float(objetivo.split("proteina")[0].split()[-1].replace("g", ""))
            except ValueError: pass
        if "refeicoes" in restricoes:
            try:
                patient_data["num_refeicoes"] = int(restricoes.split("refeicoes")[0].split()[-1])
            except ValueError: pass
        if "treino" in restricoes:
            patient_data["incluir_pre_treino"] = True

        plano = create_meal_plan(patient_data)

        # A API retorna o plano estruturado. O Custom GPT será responsável
        # por formatar este JSON no Markdown final.
        return jsonify({"plano": plano}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Use gunicorn para produção, Flask para desenvolvimento
    # from gunicorn.app.base import BaseApplication
    # class FlaskApplication(BaseApplication):
    #     def __init__(self, app, options=None):
    #         self.options = options or {}
    #         self.application = app
    #         super().__init__()
    #     def load_config(self):
    #         config = {key: value for key, value in self.options.items()
    #                   if key in self.cfg.settings and value is not None}
    #         for key, value in config.items():
    #             self.cfg.set(key.lower(), value)
    #     def load(self):
    #         return self.application
    # options = {
    #     'bind': '%s:%s' % ('0.0.0.0', os.environ.get('PORT', '5000')),
    #     'workers': 1,
    # }
    # FlaskApplication(app, options).run()
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', '5000'))
