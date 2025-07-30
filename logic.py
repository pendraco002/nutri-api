# logic.py (Versão de Produção v2.1 - Com Otimizador Funcional)

from database import get_food_data, get_meal_components
from datetime import datetime
import random

# --- FUNÇÕES AUXILIARES DE CÁLCULO ---

def calculate_macros_from_list(items_list, db_foods):
    """Calcula os macros totais de uma lista de ingredientes."""
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

# --- FUNÇÃO DE CONSTRUÇÃO E OTIMIZAÇÃO DE REFEIÇÃO ---

def build_optimized_meal(template, target_kcal, db_foods):
    """
    Cria uma refeição a partir de um template e otimiza as porções
    para se aproximar da meta calórica da refeição.
    """
    # Define uma proporção inicial para os ingredientes
    # Um otimizador real usaria um método mais inteligente (ex: solver)
    base_portions = {
        "proteina": 0.5, "carboidrato": 0.3, "gordura": 0.1, "fibra": 0.1
    }
    
    # Cria a lista de ingredientes com uma porção inicial
    meal_items = []
    for ingredient_id in template["ingredientes_base"]:
        # Simplificação: assume que o nome do ingrediente indica seu tipo macro
        item_type = "proteina"
        if "arroz" in ingredient_id or "batata" in ingredient_id or "pao" in ingredient_id:
            item_type = "carboidrato"
        
        meal_items.append({"id": ingredient_id, "gramas": 100 * base_portions.get(item_type, 0.2)})

    # Otimização por fator de escala
    current_macros = calculate_macros_from_list(meal_items, db_foods)
    current_kcal = current_macros.get("kcal", 1) # Evita divisão por zero
    
    if current_kcal > 0:
        scaling_factor = target_kcal / current_kcal
        for item in meal_items:
            item["gramas"] *= scaling_factor
            item["gramas"] = round(item["gramas"] / 5) * 5 # Arredonda para múltiplos de 5

    # Recalcula macros finais e formata a saída
    final_macros = calculate_macros_from_list(meal_items, db_foods)
    
    formatted_items = []
    for item in meal_items:
        formatted_items.append({
            "item": item["id"].replace("_", " ").title(),
            "qtd": int(item["gramas"]),
            "unidade": "g"
        })

    return {
        "nome": template["nome_template"],
        "kcal_total_refeicao": round(final_macros["kcal"]),
        "macros": final_macros,
        "itens": formatted_items
    }

# --- FUNÇÃO PRINCIPAL DE LÓGICA ---

def generate_plan_logic(request_data):
    paciente_info = request_data.get('paciente', {})
    metas = request_data.get('metas', {})
    
    peso_kg = paciente_info.get('peso_kg')
    meta_kcal = metas.get('kcal_total')
    if not peso_kg or not meta_kcal:
        return {"erro": "Dados insuficientes."}, 400

    db_foods = get_food_data()
    db_components = get_meal_components()

    # Estrutura do plano com base no número de refeições ou padrão
    num_refeicoes = metas.get("num_refeicoes", 4)
    meal_structure = ["almoço", "lanche", "jantar"]
    if num_refeicoes >= 4:
        meal_structure.append("ceia")
    if num_refeicoes >= 5:
        meal_structure.insert(0, "cafe_da_manha") # Adiciona café da manhã se forem 5+ refeições

    # Distribuição de calorias
    kcal_distribution = {
        "cafe_da_manha": meta_kcal * 0.25,
        "almoço": meta_kcal * 0.30,
        "lanche": meta_kcal * 0.20,
        "jantar": meta_kcal * 0.25,
        "ceia": meta_kcal * 0.10, # Ajustar se a soma passar de 1.0
    }

    final_refeicoes = []
    summary_macros = {"kcal": 0, "p": 0, "c": 0, "g": 0}
    horarios = {"cafe_da_manha": "08:00", "almoço": "12:30", "lanche": "16:00", "jantar": "20:00", "ceia": "22:30"}

    for meal_name in meal_structure:
        target_kcal = kcal_distribution.get(meal_name, 0)
        
        # Seleciona um template aleatório para a refeição principal
        main_template = random.choice(db_components.get(meal_name, db_components["lanche"]))
        
        # Constrói e otimiza a refeição principal
        main_meal = build_optimized_meal(main_template, target_kcal, db_foods)
        
        # Constrói e otimiza as substituições
        substitutions = []
        available_subs = [t for t in db_components.get(meal_name, []) if t["id"] != main_template["id"]]
        for sub_template in random.sample(available_subs, min(len(available_subs), 3)): # Pega até 3 subs
            substitutions.append(build_optimized_meal(sub_template, target_kcal, db_foods))

        main_meal["substituicoes"] = substitutions
        main_meal["horario"] = horarios[meal_name]
        main_meal["nome_refeicao"] = meal_name.replace("_", " ").title()
        
        final_refeicoes.append(main_meal)
        
        # Atualiza o resumo total
        for key in summary_macros:
            summary_macros[key] += main_meal["macros"][key]

    response_payload = {
        "plano": {
            "paciente": paciente_info.get("nome", "Paciente"),
            "data": datetime.now().strftime("%d/%m/%Y"),
            "resumo": {
                "meta_kcal": meta_kcal,
                "total_kcal_calculado": round(summary_macros["kcal"]),
                "total_proteina_g": round(summary_macros["p"]),
                "total_carboidratos_g": round(summary_macros["c"]),
                "total_gordura_g": round(summary_macros["g"])
            },
            "refeicoes": final_refeicoes
        }
    }
    
    return response_payload, 200
