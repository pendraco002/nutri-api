# logic.py (Versão Final 6.0 - Lógica Proativa)

from pulp import LpProblem, LpVariable, lpSum, LpMinimize, value
from database import get_food_data, get_meal_templates, get_substitution_rules, get_static_info
from datetime import datetime
import random

def generate_plan_logic(request_data):
    # ... (a lógica do solver da v5.0 permanece a mesma) ...

    # A principal mudança está na forma como a resposta final é construída,
    # usando as novas informações da base de dados.

    # Exemplo de como a nova lógica de apresentação funcionaria:
    
    # 1. Carrega TODAS as informações da base de dados
    db_foods = get_food_data()
    templates = get_meal_templates()
    regras_substituicao = get_substitution_rules()
    info_estatica = get_static_info()

    # 2. Lógica de Seleção Inteligente
    # O motor agora sabe diferenciar 'base' de 'receita'
    refeicao_principal_jantar = random.choice([t for t in templates["jantar"] if t["type"] == "base"])
    substituicoes_jantar = [t for t in templates["jantar"] if t["type"] == "receita"]

    # 3. Construção da Resposta Final
    # Ao montar cada item, ele verifica se existe uma 'obs' no db_foods
    # Ex: para 'chia', ele adicionaria a nota "Hidratar no iogurte..."

    # Ao montar as substituições, ele usa o texto completo de regras_substituicao
    # Ex: para 'feijao', ele escreveria "1 concha (substituível por...)"

    # Se o plano for para um fim de semana, ele adicionaria a 'orientacao_refeicao_livre'
    
    # ... (simulação da resposta final)
    
    response_payload = {
        # ... (cabeçalho e resumo) ...
        "refeicoes": [
            # ... (refeições construídas com todos os detalhes) ...
        ],
        "orientacoes_gerais": [
            info_estatica["orientacao_refeicao_livre"] # Exemplo de como usar
        ]
    }
    
    return response_payload, 200
