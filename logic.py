# logic.py (Versão Final 9.0 - Completo e Sincronizado)

from pulp import LpProblem, LpVariable, lpSum, LpMinimize, value
from database import get_food_data, get_meal_templates, get_substitution_rules, get_static_info
from datetime import datetime
import random

def generate_plan_logic(request_data):
    try:
        # 1. Extração e Validação de Dados
        paciente_info = request_data.get('paciente', {})
        metas = request_data.get('metas', {})
        peso_kg = paciente_info.get('peso_kg')
        meta_kcal = metas.get('kcal_total')

        if not peso_kg or not meta_kcal:
            return {"erro": "Peso do paciente e meta de calorias são obrigatórios."}, 400

        # 2. Definição das Metas Numéricas
        meta_proteina_min = metas.get("proteina_min_g_por_kg", 1.8) * peso_kg
        meta_carb_max_g = (meta_kcal * (metas.get("carboidrato_max_percent", 40) / 100)) / 4
        meta_gordura_max_g = (meta_kcal * (metas.get("gordura_max_percent", 30) / 100)) / 9
        
        db_foods = get_food_data()
        templates = get_meal_templates()
        num_refeicoes = metas.get("num_refeicoes", 5)

        # 3. Seleção de Templates de Refeição
        # Lógica simplificada para garantir a variedade e o tipo correto de refeição
        refeicoes_escolhidas = []
        tipos_refeicao = ["cafe_da_manha", "lanche", "jantar", "ceia"] # Almoço é um tipo de jantar
        
        # Garante que as refeições principais sejam do tipo 'base'
        almoco_template = random.choice([t for t in templates["jantar"] if t["type"] == "base"])
        jantar_template = random.choice([t for t in templates["jantar"] if t["type"] == "base"])
        
        refeicoes_escolhidas.append({"nome_refeicao": "Almoço", "template": almoco_template})
        refeicoes_escolhidas.append({"nome_refeicao": "Jantar", "template": jantar_template})
        refeicoes_escolhidas.append({"nome_refeicao": "Cafe Da Manha", "template": random.choice(templates["cafe_da_manha"])})
        refeicoes_escolhidas.append({"nome_refeicao": "Lanche", "template": random.choice(templates["lanche"])})
        refeicoes_escolhidas.append({"nome_refeicao": "Ceia", "template": random.choice(templates["ceia"])})
        
        # 4. Preparação para o Solver
        prob = LpProblem("Diet_Optimization", LpMinimize)
        food_vars = {}
        all_ingredients = set()

        for refeicao in refeicoes_escolhidas:
            for ing_str in refeicao["template"]["ingredientes"]:
                food_id = ing_str.split(':')[0]
                all_ingredients.add(food_id)

        for food_id in all_ingredients:
            food_vars[food_id] = LpVariable(f"food_{food_id}", 0, None)

        # 5. Definição da Função Objetivo e Restrições
        # Objetivo: Minimizar o desvio da meta calórica
        total_kcal_expr = lpSum(db_foods[f]['kcal'] * food_vars[f] for f in all_ingredients)
        desvio_kcal = LpVariable("desvio_kcal", 0, None)
        prob += desvio_kcal

        prob += total_kcal_expr - meta_kcal <= desvio_kcal
        prob += meta_kcal - total_kcal_expr <= desvio_kcal
        
        # Restrições de Macronutrientes
        prob += lpSum(db_foods[f]['p'] * food_vars[f] for f in all_ingredients) >= meta_proteina_min
        prob += lpSum(db_foods[f]['c'] * food_vars[f] for f in all_ingredients) <= meta_carb_max_g
        prob += lpSum(db_foods[f]['g'] * food_vars[f] for f in all_ingredients) <= meta_gordura_max_g

        # 6. Resolução do Problema
        prob.solve()

        # 7. Construção da Resposta Final
        if prob.status != 1: # Se não for "Optimal"
            return {"erro": "Não foi possível encontrar uma solução ótima para as metas fornecidas."}, 400

        refeicoes_finais = []
        kcal_final, proteina_final, carb_final, gordura_final = 0, 0, 0, 0

        for refeicao in refeicoes_escolhidas:
            itens_refeicao = []
            kcal_refeicao, p_refeicao, c_refeicao, g_refeicao = 0, 0, 0, 0
            
            for ing_str in refeicao["template"]["ingredientes"]:
                food_id = ing_str.split(':')[0]
                gramas = value(food_vars[food_id])
                
                if gramas > 0:
                    kcal_item = db_foods[food_id]['kcal'] * gramas
                    p_item = db_foods[food_id]['p'] * gramas
                    c_item = db_foods[food_id]['c'] * gramas
                    g_item = db_foods[food_id]['g'] * gramas
                    
                    itens_refeicao.append({"item": food_id.replace("_", " ").title(), "qtd": round(gramas), "unidade": "g"})
                    kcal_refeicao += kcal_item
                    p_refeicao += p_item
                    c_refeicao += c_item
                    g_refeicao += g_item

            refeicoes_finais.append({
                "nome_refeicao": refeicao["nome_refeicao"],
                "kcal_total_refeicao": round(kcal_refeicao),
                "itens": itens_refeicao
            })
            
            kcal_final += kcal_refeicao
            proteina_final += p_refeicao
            carb_final += c_refeicao
            gordura_final += g_refeicao

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

    except Exception as e:
        # Log do erro no servidor para depuração
        print(f"Erro interno no servidor: {e}")
        return {"erro": "Ocorreu um erro interno inesperado no servidor."}, 500
