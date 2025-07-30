# logic.py (Versão de Produção v2.2 - Com Otimizador Iterativo)

from database import get_food_data, get_meal_components
from datetime import datetime
import random

# --- FUNÇÕES AUXILIARES ---

def calculate_macros_from_list(items_list, db_foods):
    total_macros = {"kcal": 0, "p": 0, "c": 0, "g": 0}
    for item in items_list:
        food_data = db_foods.get(item["id"])
        if food_data:
            grams = item["gramas"]
            total_macros["kcal"] += food_data["kcal"] * grams
            total_macros["p"] += food_data["p"] * grams
            total_macros["c"] += food_data["c"] * grams
            total_macros["g"] += food_data["g"] * grams
    return total_macros

def build_meal_from_template(template, target_kcal, db_foods):
    # Esta função agora apenas monta um rascunho inicial
    meal_items = []
    # Define porções iniciais mais realistas
    for ingredient_id in template["ingredientes_base"]:
        gramas = 100 # Começa com uma base de 100g
        if "whey" in ingredient_id or "requeijao" in ingredient_id:
            gramas = 30
        elif "ovo" in ingredient_id:
            gramas = 50 # 1 ovo
        meal_items.append({"id": ingredient_id, "gramas": gramas})

    current_macros = calculate_macros_from_list(meal_items, db_foods)
    current_kcal = current_macros.get("kcal", 1)
    
    if current_kcal > 0:
        scaling_factor = target_kcal / current_kcal
        for item in meal_items:
            item["gramas"] = round((item["gramas"] * scaling_factor) / 5) * 5

    final_macros = calculate_macros_from_list(meal_items, db_foods)
    formatted_items = [{"item": i["id"].replace("_", " ").title(), "qtd": int(i["gramas"]), "unidade": "g"} for i in meal_items]

    return {
        "nome": template["nome_template"],
        "kcal_total_refeicao": round(final_macros["kcal"]),
        "macros": final_macros,
        "itens": formatted_items,
        "internal_items": meal_items # Guarda a estrutura interna para otimização
    }

# --- FUNÇÃO PRINCIPAL DE LÓGICA ---

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
    db_components = get_meal_components()

    # 2. MONTAR UM PLANO DE RASCUNHO
    num_refeicoes = metas.get("num_refeicoes", 5)
    meal_structure = ["cafe_da_manha", "almoço", "lanche", "jantar"]
    if num_refeicoes >= 5: meal_structure.append("ceia")
    if num_refeicoes >= 6: meal_structure.insert(2, "lanche_2") # Adiciona um segundo lanche

    kcal_distribution = {"cafe_da_manha": 0.2, "almoço": 0.3, "lanche": 0.15, "lanche_2": 0.15, "jantar": 0.25, "ceia": 0.05}
    
    draft_plan = []
    for meal_name in meal_structure[:num_refeicoes]:
        target_kcal = meta_kcal * kcal_distribution[meal_name]
        template = random.choice(db_components.get(meal_name, db_components["lanche"]))
        meal = build_meal_from_template(template, target_kcal, db_foods)
        meal["nome_refeicao"] = meal_name
        draft_plan.append(meal)

    # 3. OTIMIZADOR ITERATIVO
    # Este loop ajusta o rascunho para se aproximar das metas
    for _ in range(10): # Roda o otimizador 10 vezes
        summary = calculate_macros_from_list([item for meal in draft_plan for item in meal["internal_items"]], db_foods)
        
        # Lógica de correção:
        # Se os carboidratos estão altos, reduz um item de carbo de alguma refeição
        if summary["c"] > meta_carb_max_g:
            for meal in draft_plan:
                for item in meal["internal_items"]:
                    if "arroz" in item["id"] or "batata" in item["id"] or "pao" in item["id"] or "aveia" in item["id"]:
                        item["gramas"] = max(0, item["gramas"] - 10) # Reduz 10g
                        break # Sai do loop interno para recalcular
                else: continue
                break # Sai do loop externo para recalcular
        
        # Se a gordura está alta, reduz um item de gordura
        if summary["g"] > meta_gordura_max_g:
            for meal in draft_plan:
                for item in meal["internal_items"]:
                    if "mussarela" in item["id"] or "requeijao" in item["id"]:
                        item["gramas"] = max(0, item["gramas"] - 5) # Reduz 5g
                        break
                else: continue
                break
        
        # Se as calorias estão muito fora, ajusta a maior refeição
        kcal_diff = summary["kcal"] - meta_kcal
        if abs(kcal_diff) > 50:
            meal_to_adjust = max(draft_plan, key=lambda m: m["kcal_total_refeicao"])
            for item in meal_to_adjust["internal_items"]:
                # Ajuste proporcional
                item["gramas"] = max(0, item["gramas"] * (1 - kcal_diff / meta_kcal / 2))

    # 4. FINALIZAR E FORMATAR O PLANO OTIMIZADO
    final_refeicoes = []
    final_summary = {"kcal": 0, "p": 0, "c": 0, "g": 0}
    horarios = {"cafe_da_manha": "08:00", "almoço": "12:30", "lanche": "16:00", "lanche_2": "18:00", "jantar": "20:30", "ceia": "22:30"}

    for meal in draft_plan:
        # Recalcula tudo após a otimização
        final_meal = build_meal_from_template(meal, meal["kcal_total_refeicao"], db_foods)
        final_meal["nome_refeicao"] = meal["nome_refeicao"].replace("_", " ").title()
        final_meal["horario"] = horarios[meal["nome_refeicao"].lower().replace(" ", "_")]
        
        # Adiciona substituições (lógica simplificada por enquanto)
        final_meal["substituicoes"] = []
        
        final_refeicoes.append(final_meal)
        for key in final_summary:
            final_summary[key] += final_meal["macros"][key]

    response_payload = {
        "plano": {
            "paciente": paciente_info.get("nome", "Paciente"),
            "data": datetime.now().strftime("%d/%m/%Y"),
            "resumo": {
                "meta_kcal": meta_kcal,
                "total_kcal_calculado": round(final_summary["kcal"]),
                "total_proteina_g": round(final_summary["p"]),
                "total_carboidratos_g": round(final_summary["c"]),
                "total_gordura_g": round(final_summary["g"])
            },
            "refeicoes": final_refeicoes
        }
    }
    
    return response_payload, 200
