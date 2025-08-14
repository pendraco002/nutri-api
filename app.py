# -*- coding: utf-8 -*-
"""
Ponto de Entrada da Aplicação Web (API) - Sistema de Nutrição

Este arquivo implementa uma API Flask para o sistema de geração de planos
alimentares. Ele expõe um endpoint seguro que recebe dados do paciente e,
utilizando a lógica de negócio encapsulada, retorna um plano nutricional
completo e personalizado.

Arquitetura da API:
1.  **Framework:** Utiliza Flask, um micro-framework Python leve e robusto,
    ideal para a criação de APIs.
2.  **Segurança:** O acesso ao endpoint principal é protegido por uma chave de API.
    A chave deve ser enviada no cabeçalho `X-API-KEY` de cada requisição. A
    chave esperada é lida de uma variável de ambiente (`API_KEY`), uma prática
    de segurança padrão para evitar chaves hardcoded no código.
3.  **Endpoint (`/generate_plan`):** Um único endpoint que aceita requisições
    `POST` com um corpo JSON contendo os dados do paciente.
4.  **Entrada e Saída:** A comunicação é feita via JSON, um formato universal
    e de fácil integração com diferentes clientes (web, mobile, etc.).
5.  **Separação de Responsabilidades:** Este arquivo foca exclusivamente na
    camada de API (receber requisições, autenticar, validar, e retornar
    respostas). A lógica complexa de cálculo nutricional e geração de planos é
    delegada a um módulo de lógica separado (simulado aqui para demonstração).
6.  **Pronto para Produção:** O código é estruturado para ser servido por um
    servidor WSGI como Gunicorn, conforme especificado pelo comando
    `gunicorn app:app` no `render.yaml`.
"""

import os
from functools import wraps
from flask import Flask, request, jsonify

# =============================================================================
# MÓDULO DE LÓGICA NUTRICIONAL (SIMULADO)
# =============================================================================
# Em um projeto real, a função `generate_complete_meal_plan` estaria em um
# arquivo separado (ex: `nutritional_logic.py`) e seria importada aqui.
# Este módulo de lógica seria o responsável por importar os dados de
# `nutritional_database_and_meal_planning_data` e aplicar as regras de negócio.
# Para tornar este exemplo executável, a lógica é simulada abaixo.

def generate_complete_meal_plan(patient_data: dict) -> dict:
    """
    Função simulada que representa o núcleo do sistema.

    Recebe os dados do paciente e retorna um plano alimentar estruturado.
    Esta função seria responsável por:
    1. Calcular as necessidades calóricas (TMB, GET).
    2. Definir a distribuição de macronutrientes.
    3. Selecionar componentes da `MEAL_COMPONENT_LIBRARY`.
    4. Escalar os ingredientes para atingir as metas.
    5. Gerar opções de substituição a partir dos `MEAL_SUBSTITUTION_GROUPS`.
    """
    # Apenas um exemplo estático para demonstrar o formato da resposta da API.
    # A lógica real seria dinâmica com base nos `patient_data`.
    client_name = patient_data.get("name", "Cliente")
    return {
        "client_name": client_name,
        "daily_targets": {
            "calories": "2500 kcal",
            "protein": "180g",
            "carbohydrates": "250g",
            "fat": "80g"
        },
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
                    "Opção 2: Crepioca com Queijo (ajustado para as mesmas calorias)",
                    "Opção 3: Sanduíche de Frango (ajustado para as mesmas calorias)"
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
                "substitution_options": [
                    "Opção 2: Carne Moída com Batata Doce (ajustado)",
                    "Opção 3: Tilápia com Legumes (ajustado)"
                ]
            },
            {
                "meal_name": "Jantar (20:00)",
                "main_option": {
                    "description": "Pizza Fake de Frango",
                    "ingredients": [
                        {"name": "Massa de Rap10 Integral", "quantity": "45g"},
                        {"name": "Peito de Frango Grelhado", "quantity": "150g"},
                        {"name": "Queijo Mussarela Light", "quantity": "50g"},
                        {"name": "Tomate", "quantity": "60g"}
                    ]
                },
                "substitution_options": [
                    "Opção 2: Strogonoff Fit de Frango (ajustado)"
                ]
            }
        ],
        "recommendations": [
            "Beba pelo menos 3 litros de água por dia.",
            "Priorize o consumo de saladas e vegetais folhosos nas refeições principais.",
            "Ajuste os horários das refeições conforme sua rotina."
        ]
    }

# =============================================================================
# CONFIGURAÇÃO DA APLICAÇÃO FLASK
# =============================================================================

app = Flask(__name__)

# Carrega a chave de API das variáveis de ambiente.
# No ambiente de produção (ex: Render), esta variável deve ser configurada.
API_KEY = os.environ.get("API_KEY")

# Decorator para proteger rotas com a chave de API
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not API_KEY:
            # Erro de configuração do servidor
            return jsonify({"error": "API Key not configured on the server."}), 500

        key = request.headers.get('X-API-KEY')
        if not key or key != API_KEY:
            return jsonify({"error": "Unauthorized. Invalid or missing API Key."}), 401
        
        return f(*args, **kwargs)
    return decorated_function

# =============================================================================
# DEFINIÇÃO DOS ENDPOINTS DA API
# =============================================================================

@app.route('/generate_plan', methods=['POST'])
@require_api_key
def handle_generate_plan():
    """
    Endpoint principal para a geração de planos alimentares.
    Espera um JSON com os dados do paciente e retorna o plano completo.
    """
    # 1. Obter e validar dados de entrada
    patient_data = request.get_json()
    if not patient_data:
        return jsonify({"error": "Invalid input. Request body must be a valid JSON."}), 400

    required_fields = ['name', 'weight_kg', 'height_cm', 'age', 'gender', 'activity_level', 'goal']
    missing_fields = [field for field in required_fields if field not in patient_data]

    if missing_fields:
        return jsonify({
            "error": "Missing required fields in request body.",
            "missing": missing_fields
        }), 400

    # 2. Chamar a lógica de negócio para gerar o plano
    try:
        meal_plan = generate_complete_meal_plan(patient_data)
    except Exception as e:
        # Captura erros inesperados da lógica de negócio
        app.logger.error(f"Error during meal plan generation: {e}")
        return jsonify({"error": "An internal error occurred while generating the meal plan."}), 500

    # 3. Retornar o plano gerado com sucesso
    return jsonify(meal_plan), 200

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
# Este bloco permite executar o servidor Flask localmente para desenvolvimento
# e teste usando o comando `python app.py`. Em produção, um servidor WSGI
# como Gunicorn será usado.

if __name__ == '__main__':
    # O host '0.0.0.0' torna a aplicação acessível na rede local.
    # A porta é lida da variável de ambiente PORT, padrão para serviços como o Render.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
