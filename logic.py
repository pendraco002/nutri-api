# logic.py (Versão de Produção v2.5 - Polimento Final)

from database import get_food_data, get_meal_components
from datetime import datetime
import random

# (As funções auxiliares podem permanecer as mesmas da v2.3/v2.4)
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
    meal_items = []
    for ingredient_id in template["ingredientes_base"]:
        gramas = 100
        if "whey" in ingredient_id or "requeijao" in ingredient_id: gramas = 30
        elif "ovo" in ingredient_id: gramas = 50
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
        "internal_items": meal_items
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
    base_structure = ["cafe_da_manha", "almoço", "lanche", "jantar", "ceia"]
    meal_structure = base_structure[:num_refeicoes]
    kcal_distribution = {"cafe_da_manha": 0.25, "almoço": 0.30, "lanche": 0.20, "jantar": 0.25, "ceia": 0.10}
    
    draft_plan = []
    for meal_name in meal_structure:
        target_kcal = meta_kcal * kcal_distribution[meal_name]
        components = db_components.get(meal_name, db_components["lanche"])
        template = random.choice(components)
        meal = build_meal_from_template(template, target_kcal, db_foods)
        meal["nome_refeicao_id"] = meal_name
        draft_plan.append(meal)

    # 3. OTIMIZADOR HIERÁRQUICO v2.5
    for _ in range(25): # Mais iterações para ajuste fino
        summary = calculate_macros_from_list([item for meal in draft_plan for item in meal["internal_items"]], db_foods)
        
        # PRIORIDADE 1: ATINGIR O PISO DE PROTEÍNA
        if summary["p"] < meta_proteina_min:
            meal_to_adjust = max(draft_plan, key=lambda m: m["macros"]["p"])
            for item in meal_to_adjust["internal_items"]:
                # Lógica de substituição inteligente: prioriza fontes de proteína magra
                if "whey" in item["id"] or "frango" in item["id"] or "tilapia" in item["id"] or "clara" in item["id"]:
                    item["gramas"] *= 1.15 # Aumenta mais agressivamente
                    break
            else: # Se não encontrou proteína magra, aumenta a primeira que achar
                meal_to_adjust["internal_items"][0]["gramas"] *= 1.05
        
        # PRIORIDADE 2: RESPEITAR O TETO DE GORDURAS
        if summary["g"] > meta_gordura_max_g:
            meal_to_adjust = max(draft_plan, key=lambda m: m["macros"]["g"])
            for item in meal_to_adjust["internal_items"]:
                if "mussarela" in item["id"] or "requeijao" in item["id"] or "gema" in item["id"] or "pao_hamburguer" in item["id"]:
                    item["gramas"] *= 0.85 # Reduz mais agressivamente
                    break
        
        # PRIORIDADE 3: RESPEITAR O TETO DE CARBOIDRATOS
        if summary["c"] > meta_carb_max_g:
            meal_to_adjust = max(draft_plan, key=lambda m: m["macros"]["c"])
            for item in meal_to_adjust["internal_items"]:
                if "arroz" in item["id"] or "batata" in item["id"] or "pao" in item["id"] or "aveia" in item["id"] or "tapioca" in item["id"]:
                    item["gramas"] *= 0.9
                    break

        # Recalcula o rascunho
        for meal in draft_plan:
            new_macros = calculate_macros_from_list(meal["internal_items"], db_foods)
            meal["macros"] = new_macros
            meal["kcal_total_refeicao"] = round(new_macros["kcal"])

    # 4. AJUSTE FINAL DE CALORIAS
    final_summary = calculate_macros_from_list([item for meal in draft_plan for item in meal["internal_items"]], db_foods)
    if final_summary["kcal"] > 0:
        scaling_factor = meta_kcal / final_summary["kcal"]
        for meal in draft_plan:
            for item in meal["internal_items"]:
                item["gramas"] *= scaling_factor

    # 5. FINALIZAR E FORMATAR
    final_refeicoes = []
    final_summary_after_scaling = {"kcal": 0, "p": 0, "c": 0, "g": 0}
    horarios = {"cafe_da_manha": "08:00", "almoço": "12:30", "lanche": "16:00", "jantar": "20:30", "ceia": "22:30"}

    for meal_draft in draft_plan:
        final_macros = calculate_macros_from_list(meal_draft["internal_items"], db_foods)
        formatted_items = [{"item": i["id"].replace("_", " ").title(), "qtd": int(i["gramas"]), "unidade": "g"} for i in meal_draft["internal_items"]]
        
        meal_final = {
            "nome": meal_draft["nome"],
            "kcal_total_refeicao": round(final_macros["kcal"]),
            "macros": final_macros,
            "itens": formatted_items,
            "nome_refeicao": meal_draft["nome_refeicao_id"].replace("_", " ").title(),
            "horario": horarios.get(meal_draft["nome_refeicao_id"], "N/A"),
            "substituicoes": []
        }
        final_refeicoes.append(meal_final)
        for key in final_summary_after_scaling:
            final_summary_after_scaling[key] += final_macros[key]

    response_payload = {
        "plano": {
            "paciente": paciente_info.get("nome", "Paciente"),
            "data": datetime.now().strftime("%d/%m/%Y"),
            "resumo": {
                "meta_kcal": meta_kcal,
                "total_kcal_calculado": round(final_summary_after_scaling["kcal"]),
                "total_proteina_g": round(final_summary_after_scaling["p"]),
                "total_carboidratos_g": round(final_summary_after_scaling["c"]),
                "total_gordura_g": round(final_summary_after_scaling["g"])
            },
            "refeicoes": final_refeicoes
        }
    }
    
    return response_payload, 200
