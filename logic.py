# logic.py (Versão Final 13.0 - Transparência e Precisão Absoluta)

from pulp import LpProblem, LpVariable, lpSum, LpMinimize, value
from database import get_food_data, get_meal_templates, get_substitution_rules, get_static_info
from datetime import datetime
import random

# (Os schemas Pydantic da v11.0 permanecem os mesmos)

def generate_plan_logic(request_data):
    try:
        # ... (Passos 1 a 3: Validação, Saneamento, Seleção de Templates - permanecem os mesmos) ...
        
        # --- PASSO 4: OTIMIZAÇÃO COM SOLVER (CONFIGURAÇÃO DE ALTA PRECISÃO) ---
        prob = LpProblem("Diet_Optimization_High_Precision", LpMinimize)
        
        # ... (Definição das variáveis, como antes) ...
        
        # Objetivo: Minimizar o desvio absoluto da meta calórica
        total_kcal_expr = lpSum(db_foods[f]['kcal'] * food_vars[f] for f in all_ingredients)
        desvio_kcal = LpVariable("desvio_kcal", 0, None)
        prob += desvio_kcal

        # Restrições de desvio mais rígidas
        prob += total_kcal_expr - meta_kcal <= desvio_kcal
        prob += meta_kcal - total_kcal_expr <= desvio_kcal
        
        # Restrições de Macronutrientes (como antes)
        # ...

        # --- PASSO 5: RESOLUÇÃO DO PROBLEMA ---
        prob.solve()

        if prob.status != 1: # "Optimal"
            return {"erro": "Não foi possível encontrar uma solução ótima para as metas fornecidas."}, 400

        # --- PASSO 6: CONSTRUÇÃO DA RESPOSTA COM DETALHAMENTO TOTAL ---
        refeicoes_finais = []
        kcal_final, proteina_final, carb_final, gordura_final = 0, 0, 0, 0

        for refeicao in refeicoes_escolhidas:
            itens_refeicao_detalhados = []
            kcal_refeicao, p_refeicao, c_refeicao, g_refeicao = 0, 0, 0, 0
            
            for ing_str in refeicao["template"]["ingredientes"]:
                food_id = ing_str.split(':')[0]
                gramas = value(food_vars[food_id])
                
                if gramas > 0.1: # Apenas inclui ingredientes com quantidade significativa
                    kcal_item = db_foods[food_id]['kcal'] * gramas
                    p_item = db_foods[food_id]['p'] * gramas
                    c_item = db_foods[food_id]['c'] * gramas
                    g_item = db_foods[food_id]['g'] * gramas
                    
                    # Constrói o item com todos os detalhes
                    itens_refeicao_detalhados.append({
                        "item": food_id.replace("_", " ").title(),
                        "qtd_g": round(gramas, 1),
                        "kcal": round(kcal_item),
                        "macros": {
                            "p": round(p_item, 1),
                            "c": round(c_item, 1),
                            "g": round(g_item, 1)
                        }
                    })
                    
                    kcal_refeicao += kcal_item
                    p_refeicao += p_item
                    c_refeicao += c_item
                    g_refeicao += g_item

            # Adiciona a refeição com o resumo de macros
            refeicoes_finais.append({
                "nome_refeicao": refeicao["nome_refeicao"],
                "kcal_total_refeicao": round(kcal_refeicao),
                "macros_refeicao": {
                    "p": round(p_refeicao, 1),
                    "c": round(c_refeicao, 1),
                    "g": round(g_refeicao, 1)
                },
                "itens": itens_refeicao_detalhados
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
                    "total_proteina_g": round(proteina_final, 1),
                    "total_carboidratos_g": round(carb_final, 1),
                    "total_gordura_g": round(gordura_final, 1)
                },
                "refeicoes": refeicoes_finais
            }
        }
        
        return response_payload, 200

    except Exception as e:
        print(f"Erro interno no servidor: {e}")
        return {"erro": "Ocorreu um erro interno inesperado no servidor."}, 500
