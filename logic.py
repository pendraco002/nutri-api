# logic.py (Versão de Produção v3.1 - Com Solver Matemático)

from pulp import LpProblem, LpVariable, lpSum, LpMinimize, value
from database import get_food_data, get_meal_components
from datetime import datetime
import random

def generate_plan_logic(request_data):
    paciente_info = request_data.get('paciente', {})
    metas = request_data.get('metas', {})
    
    peso_kg = paciente_info.get('peso_kg')
    meta_kcal = metas.get('kcal_total')
    if not peso_kg or not meta_kcal:
        return {"erro": "Dados insuficientes."}, 400

    # 1. CALCULAR METAS NUMÉRICAS ABSOLUTAS
    meta_proteina_min = metas.get("proteina_min_g_por_kg", 1.8) * peso_kg
    meta_carb_max_g = (meta_kcal * (metas.get("carboidrato_max_percent", 40) / 100)) / 4
    meta_gordura_max_g = (meta_kcal * (metas.get("gordura_max_percent", 30) / 100)) / 9

    db_foods = get_food_data()
    
    # 2. DEFINIR O PROBLEMA DE OTIMIZAÇÃO
    prob = LpProblem("PlanoNutricionalPerfeito", LpMinimize)

    # 3. DEFINIR AS VARIÁVEIS DE DECISÃO
    food_vars = {food_id: LpVariable(f"gramas_{food_id}", lowBound=0, cat='Continuous') for food_id in db_foods}

    # 4. DEFINIR A FUNÇÃO OBJETIVO
    total_kcal_calculado = lpSum([db_foods[f]["kcal"] * food_vars[f] for f in db_foods])
    desvio_kcal = total_kcal_calculado - meta_kcal
    prob += desvio_kcal * desvio_kcal, "Desvio_Quadratico_Calorico"

    # 5. DEFINIR AS RESTRIÇÕES (AS REGRAS DE OURO)
    total_proteina = lpSum([db_foods[f]["p"] * food_vars[f] for f in db_foods])
    total_carb = lpSum([db_foods[f]["c"] * food_vars[f] for f in db_foods])
    total_gordura = lpSum([db_foods[f]["g"] * food_vars[f] for f in db_foods])

    prob += total_proteina >= meta_proteina_min, "Piso_de_Proteina"
    prob += total_carb <= meta_carb_max_g, "Teto_de_Carboidratos"
    prob += total_gordura <= meta_gordura_max_g, "Teto_de_Gordura"

    # Adicionar regras de "bom senso"
    for food_id, var in food_vars.items():
        prob += var <= 500

    # 6. RESOLVER O PROBLEMA
    prob.solve()

    # 7. MONTAR O PLANO COM A SOLUÇÃO
    if prob.status != 1: # 'Optimal' status
        return {"erro": "Não foi possível encontrar uma solução ótima com as restrições fornecidas."}, 400

    kcal_final = value(total_kcal_calculado)
    proteina_final = value(total_proteina)
    carb_final = value(total_carb)
    gordura_final = value(total_gordura)

    # Lógica para distribuir os alimentos em refeições (simplificada para demonstração)
    refeicoes_finais = [
        {"nome_refeicao": "Refeições Combinadas", "horario": "Dia Completo", "kcal_total_refeicao": round(kcal_final),
         "itens": [{"item": "Plano Otimizado pelo Solver", "qtd": 1, "unidade": "dia"}],
         "substituicoes": []
        }
    ]

    response_payload = {
        "plano": {
            "paciente": paciente_info.get("nome", "Paciente"),
            "data": datetime.now().strftime("%d/%m/%Y"),
            "resumo": {
                "meta_kcal": meta_kcal,
                "total_kcal_calculado": round(kcal_final),
                "total_proteina_g": round(proteina_final),
                "total_carboidratos_g": round(carb_final),
                "total_gordura_g": round(gordura_final)
            },
            "refeicoes": refeicoes_finais
        }
    }
    
    return response_payload, 200
