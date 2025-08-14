# -*- coding: utf-8 -*-
import os
from functools import wraps
from flask import Flask, request, jsonify
# Importa o motor de lógica e dados do arquivo local
from nutri_engine import MEAL_COMPONENT_LIBRARY, MEAL_SUBSTITUTION_GROUPS

app = Flask(__name__)

# Carrega a chave de API da variável de ambiente segura do Render.
# Esta é a prática recomendada para gerenciar segredos.
API_KEY = os.environ.get("X_API_KEY")

def generate_complete_meal_plan(patient_data: dict) -> dict:
    """
    Função SIMULADA que representa o núcleo do sistema.
    Em uma implementação completa, esta função usaria os dados de 'patient_data'
    para interagir com MEAL_COMPONENT_LIBRARY e MEAL_SUBSTITUTION_GROUPS
    e gerar um plano dinâmico.
    """
    client_name = patient_data.get("name", "Cliente")
    return {
        "client_name": client_name,
        "daily_targets": {"calories": "2500 kcal", "protein": "180g", "carbohydrates": "250g", "fat": "80g"},
        "meal_plan": [
            {
                "meal_name": "Café da Manhã (08:00)",
                "main_option": {
                    "description": "Panqueca de Banana e Aveia",
                    "ingredients": [
                        {"name": "Ovo Inteiro", "quantity": "110g"},
                        {"name": "Aveia em Flocos", "quantity": "35g"},
                        {"name": "Banana Prata", "quantity": "55g"}
                    ]
                },
                "substitution_options": [
                    "Opção 2: Crepioca com Queijo (ajustado)",
                    "Opção 3: Sanduíche de Frango (ajustado)"
                ]
            },
            {
                "meal_name": "Almoço (13:00)",
                "main_option": {
                    "description": "Frango com Arroz e Feijão",
                    "ingredients": [
                        {"name": "Peito de Frango Grelhado", "quantity": "180g"},
                        {"name": "Arroz Branco Cozido", "quantity": "120g"},
                        {"name": "Feijão Preto Cozido", "quantity": "90g"}
                    ]
                },
                "substitution_options": ["Opção 2: Carne Moída com Batata Doce (ajustado)"]
            }
        ],
        "recommendations": ["Beba pelo menos 3 litros de água por dia."]
    }

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not API_KEY:
            return jsonify({"error": "Chave de API não configurada no servidor."}), 500
        
        key = request.headers.get('X-API-KEY')
        if not key or key != API_KEY:
            return jsonify({"error": "Não autorizado. Chave de API inválida ou ausente."}), 401
        
        return f(*args, **kwargs)
    return decorated_function

@app.route('/gerarPlano', methods=['POST'])
@require_api_key
def handle_generate_plan():
    patient_data = request.get_json()
    if not patient_data:
        return jsonify({"error": "Input inválido. O corpo da requisição deve ser um JSON."}), 400

    required_fields = ['name', 'weight_kg', 'height_cm', 'age', 'gender', 'activity_level', 'goal']
    missing_fields = [field for field in required_fields if field not in patient_data]
    if missing_fields:
        return jsonify({"error": "Campos obrigatórios ausentes.", "missing": missing_fields}), 400

    try:
        meal_plan = generate_complete_meal_plan(patient_data)
        return jsonify(meal_plan), 200
    except Exception as e:
        app.logger.error(f"Erro na geração do plano: {e}")
        return jsonify({"error": "Erro interno ao gerar o plano alimentar."}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
