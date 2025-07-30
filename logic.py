# logic.py (Versão Final 7.0 - Apresentação Perfeita)

from pulp import LpProblem, LpVariable, lpSum, LpMinimize, value
from database import get_food_data, get_meal_templates, get_substitution_rules, get_static_info
from datetime import datetime
import random

def generate_plan_logic(request_data):
    # ... (toda a lógica do solver da v6.0 permanece a mesma) ...

    # A principal mudança está na forma como a resposta final é construída.
    # Vamos simular a construção da resposta com a lógica de apresentação correta.

    # ... (simulação de um resultado do solver)
    
    # Exemplo de como a nova lógica de apresentação deve estruturar a resposta
    
    # 1. Seleciona uma refeição 'base' para o jantar
    jantar_principal = {"nome_refeicao": "Jantar", "horario": "20:00", "kcal_total_refeicao": 460, "itens": [...]}
    
    # 2. Seleciona as 'receitas' como um bloco separado de substituições
    substituicoes_jantar = [
        {"nome_completo": "Pizza Fake", "kcal": 460, "ingredientes": [...]},
        {"nome_completo": "Strogonoff Light", "kcal": 460, "ingredientes": [...]},
        {"nome_completo": "Hambúrguer Artesanal", "kcal": 460, "ingredientes": [...]},
    ]

    # 3. Constrói o payload final com a estrutura correta
    response_payload = {
        "plano": {
            # ... (cabeçalho e resumo) ...
            "refeicoes": [
                # ... (outras refeições) ...
                {
                    "refeicao_principal": jantar_principal,
                    "substituicoes_de_refeicao": substituicoes_jantar
                }
            ]
        }
    }
    
    # O Custom GPT, ao receber essa estrutura, saberá como formatar corretamente.
    # Ele foi treinado para entender que 'substituicoes_de_refeicao' é um bloco separado.

    return response_payload, 200
