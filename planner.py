from database import get_food_data, get_recipes, get_meal_templates, get_substitution_rules
import math

def create_meal_plan(goals):
    """Cria plano alimentar seguindo método Pedro Barros"""
    
    # Extrair dados do input
    peso = goals.get("peso_kg", 75)
    altura = goals.get("altura_m", 1.70)
    sexo = goals.get("sexo", "M")
    nome = goals.get("nome", "Paciente")
    
    # Metas nutricionais
    total_kcal_goal = goals.get("total_kcal", 2000)
    protein_min_g_kg = goals.get("protein_min_g_kg", 2.2)
    carb_max_percent = goals.get("carb_max_percent", 35)
    fat_max_percent = goals.get("fat_max_percent", 25)
    
    # Configurações especiais
    num_refeicoes = goals.get("num_refeicoes", 5)
    tem_pre_treino = goals.get("tem_pre_treino", False)
    pre_treino_kcal = goals.get("pre_treino_kcal", 120)
    jantar_especial = goals.get("jantar_especial", None)
    
    # PASSO 1: Calcular metas de macros
    macros = calculate_macros(peso, total_kcal_goal, protein_min_g_kg, carb_max_percent, fat_max_percent)
    
    # PASSO 2: Distribuir calorias por refeição
    meal_distribution = distribute_calories(total_kcal_goal, num_refeicoes, tem_pre_treino, pre_treino_kcal)
    
    # PASSO 3: Montar refeições respeitando P≥C
    meals = build_meals(meal_distribution, macros, jantar_especial)
    
    # PASSO 4: Verificar e ajustar precisão ±10 kcal
    meals = adjust_precision(meals, total_kcal_goal)
    
    # PASSO 5: Adicionar substituições
    meals = add_substitutions(meals)
    
    # PASSO 6: Formatar no padrão Pedro Barros
    return format_meal_plan(nome, meals, macros, total_kcal_goal)

def calculate_macros(peso, total_kcal, protein_min_g_kg, carb_max_percent, fat_max_percent):
    """Calcula metas de macronutrientes seguindo as regras"""
    
    # Proteína: mínimo especificado
    protein_g = peso * protein_min_g_kg
    protein_kcal = protein_g * 4
    
    # Carboidrato: máximo especificado, mínimo 80g
    carb_max_kcal = total_kcal * (carb_max_percent / 100)
    carb_max_g = carb_max_kcal / 4
    carb_g = max(80, min(carb_max_g, (total_kcal * 0.35) / 4))  # Entre 80g e o máximo
    carb_kcal = carb_g * 4
    
    # Gordura: residual, respeitando limites
    fat_max_kcal = total_kcal * (fat_max_percent / 100)
    fat_kcal = min(total_kcal - protein_kcal - carb_kcal, fat_max_kcal)
    fat_g = fat_kcal / 9
    
    # Verificar se está dentro dos limites 0.6-0.9g/kg
    fat_g_kg = fat_g / peso
    if fat_g_kg < 0.6:
        fat_g = peso * 0.6
        fat_kcal = fat_g * 9
    elif fat_g_kg > 0.9:
        fat_g = peso * 0.9
        fat_kcal = fat_g * 9
    
    # Ajustar carboidratos se necessário
    remaining_kcal = total_kcal - protein_kcal - fat_kcal
    carb_kcal = remaining_kcal
    carb_g = carb_kcal / 4
    
    return {
        "protein_g": round(protein_g, 1),
        "protein_kcal": round(protein_kcal),
        "carb_g": round(carb_g, 1),
        "carb_kcal": round(carb_kcal),
        "fat_g": round(fat_g, 1),
        "fat_kcal": round(fat_kcal),
        "fiber_g": max(25, round(total_kcal / 100) * 1.5)  # 1.5g por 100kcal
    }

def distribute_calories(total_kcal, num_refeicoes, tem_pre_treino, pre_treino_kcal):
    """Distribui calorias entre refeições"""
    
    distribution = {}
    
    # Se tem pré-treino, reservar calorias
    if tem_pre_treino:
        distribution["pre_treino"] = pre_treino_kcal
        remaining_kcal = total_kcal - pre_treino_kcal
    else:
        remaining_kcal = total_kcal
    
    # Distribuição padrão para 5 refeições
    if num_refeicoes == 5:
        distribution.update({
            "cafe_manha": round(remaining_kcal * 0.22),
            "almoco": round(remaining_kcal * 0.32),
            "lanche": round(remaining_kcal * 0.18),
            "jantar": round(remaining_kcal * 0.23),
            "ceia": round(remaining_kcal * 0.05)
        })
    elif num_refeicoes == 4:
        distribution.update({
            "cafe_manha": round(remaining_kcal * 0.25),
            "almoco": round(remaining_kcal * 0.35),
            "lanche": round(remaining_kcal * 0.20),
            "jantar": round(remaining_kcal * 0.20)
        })
    elif num_refeicoes == 3:
        distribution.update({
            "almoco": round(remaining_kcal * 0.40),
            "lanche": round(remaining_kcal * 0.25),
            "jantar": round(remaining_kcal * 0.35)
        })
    
    return distribution

def build_meals(distribution, macros, jantar_especial):
    """Constrói refeições respeitando regra P≥C"""
    
    db = get_food_data()
    recipes = get_recipes()
    templates = get_meal_templates()
    
    meals = {}
    remaining_macros = macros.copy()
    
    # Construir cada refeição
    for meal_name, kcal_target in distribution.items():
        if meal_name == "pre_treino":
            # Pré-treino: apenas carboidratos
            meals[meal_name] = {
                "kcal": kcal_target,
                "itens": [
                    {"item": "Doce de leite", "qtd": round(kcal_target / 3.2), "unidade": "g", "kcal": kcal_target}
                ],
                "protein_g": 0,
                "carb_g": kcal_target / 4,
                "fat_g": 0
            }
        elif meal_name == "ceia":
            # Ceia padrão
            meals[meal_name] = build_ceia(kcal_target)
        elif meal_name == "lanche":
            # Usar template de lanche
            meals[meal_name] = build_lanche_from_template(kcal_target, remaining_macros)
        elif meal_name == "jantar" and jantar_especial:
            # Jantar especial (ex: hambúrguer)
            if jantar_especial == "hamburguer":
                meals[meal_name] = recipes["hamburguer_artesanal"].copy()
            else:
                meals[meal_name] = build_standard_meal(meal_name, kcal_target, remaining_macros)
        else:
            # Refeições padrão
            meals[meal_name] = build_standard_meal(meal_name, kcal_target, remaining_macros)
        
        # Atualizar macros restantes
        meal = meals[meal_name]
        remaining_macros["protein_g"] -= meal.get("protein_g", 0)
        remaining_macros["carb_g"] -= meal.get("carb_g", 0)
        remaining_macros["fat_g"] -= meal.get("fat_g", 0)
    
    # Verificar e ajustar regra P≥C
    meals = enforce_protein_rule(meals)
    
    return meals

def build_standard_meal(meal_name, kcal_target, remaining_macros):
    """Constrói refeição padrão"""
    
    db = get_food_data()
    meal = {
        "kcal": 0,
        "protein_g": 0,
        "carb_g": 0,
        "fat_g": 0,
        "itens": []
    }
    
    # Proporções típicas por refeição
    if meal_name == "cafe_manha":
        protein_ratio = 0.30
        carb_ratio = 0.50
        fat_ratio = 0.20
    elif meal_name == "almoco":
        protein_ratio = 0.35
        carb_ratio = 0.45
        fat_ratio = 0.20
    elif meal_name == "jantar":
        protein_ratio = 0.40
        carb_ratio = 0.35
        fat_ratio = 0.25
    else:
        protein_ratio = 0.33
        carb_ratio = 0.34
        fat_ratio = 0.33
    
    # Calcular metas para esta refeição
    protein_kcal = kcal_target * protein_ratio
    carb_kcal = kcal_target * carb_ratio
    fat_kcal = kcal_target * fat_ratio
    
    protein_g = protein_kcal / 4
    carb_g = carb_kcal / 4
    fat_g = fat_kcal / 9
    
    # Garantir P≥C
    if protein_g < carb_g:
        diff = carb_g - protein_g
        protein_g += diff / 2
        carb_g -= diff / 2
    
    # Montar refeição
    if meal_name == "cafe_manha":
        # Ovos
        ovos_qtd = 2
        ovos_g = ovos_qtd * 50
        ovos_data = db["ovo_inteiro"]
        
        meal["itens"].append({
            "item": "Ovo de galinha inteiro",
            "qtd": ovos_qtd,
            "unidade": "unidade",
            "kcal": round(ovos_g * ovos_data["kcal_por_g"])
        })
        meal["protein_g"] += ovos_g * ovos_data["proteina_por_g"]
        meal["carb_g"] += ovos_g * ovos_data["carb_por_g"]
        meal["fat_g"] += ovos_g * ovos_data["gordura_por_g"]
        
        # Pão
        pao_g = 50
        pao_data = db["pao_frances"]
        
        meal["itens"].append({
            "item": "Pão francês",
            "qtd": 1,
            "unidade": "unidade",
            "kcal": round(pao_g * pao_data["kcal_por_g"])
        })
        meal["protein_g"] += pao_g * pao_data["proteina_por_g"]
        meal["carb_g"] += pao_g * pao_data["carb_por_g"]
        meal["fat_g"] += pao_g * pao_data["gordura_por_g"]
        
        # Queijo
        queijo_g = 30
        queijo_data = db["queijo_mussarela"]
        
        meal["itens"].append({
            "item": "Queijo mussarela",
            "qtd": queijo_g,
            "unidade": "g",
            "kcal": round(queijo_g * queijo_data["kcal_por_g"])
        })
        meal["protein_g"] += queijo_g * queijo_data["proteina_por_g"]
        meal["carb_g"] += queijo_g * queijo_data["carb_por_g"]
        meal["fat_g"] += queijo_g * queijo_data["gordura_por_g"]
        
        # Completar com whey se necessário
        protein_needed = protein_g - meal["protein_g"]
        if protein_needed > 10:
            whey_g = round(protein_needed / 0.8)
            whey_data = db["whey_protein"]
            
            meal["itens"].append({
                "item": "Whey Protein",
                "qtd": whey_g,
                "unidade": "g",
                "kcal": round(whey_g * whey_data["kcal_por_g"])
            })
            meal["protein_g"] += whey_g * whey_data["proteina_por_g"]
            meal["carb_g"] += whey_g * whey_data["carb_por_g"]
            meal["fat_g"] += whey_g * whey_data["gordura_por_g"]
    
    elif meal_name == "almoco" or meal_name == "jantar":
        # Proteína principal
        if meal_name == "almoco":
            protein_g_needed = max(120, round(protein_g / 0.31))
        else:
            protein_g_needed = max(150, round(protein_g / 0.31))
        
        frango_data = db["file_de_frango_grelhado"]
        
        meal["itens"].append({
            "item": "Filé de frango grelhado",
            "qtd": protein_g_needed,
            "unidade": "g",
            "kcal": round(protein_g_needed * frango_data["kcal_por_g"])
        })
        meal["protein_g"] += protein_g_needed * frango_data["proteina_por_g"]
        meal["fat_g"] += protein_g_needed * frango_data["gordura_por_g"]
        
        # Carboidrato
        carb_g_needed = round(carb_g / 0.28)
        arroz_data = db["arroz_branco_cozido"]
        
        meal["itens"].append({
            "item": "Arroz branco (cozido)",
            "qtd": carb_g_needed,
            "unidade": "g",
            "kcal": round(carb_g_needed * arroz_data["kcal_por_g"])
        })
        meal["carb_g"] += carb_g_needed * arroz_data["carb_por_g"]
        meal["protein_g"] += carb_g_needed * arroz_data["proteina_por_g"]
        
        # Legumes
        legumes_g = 100
        legumes_data = db["legumes_variados"]
        
        meal["itens"].append({
            "item": "Legumes Variados",
            "qtd": legumes_g,
            "unidade": "g",
            "kcal": round(legumes_g * legumes_data["kcal_por_g"])
        })
        meal["carb_g"] += legumes_g * legumes_data["carb_por_g"]
        meal["protein_g"] += legumes_g * legumes_data["proteina_por_g"]
        
        # Feijão
        feijao_g = 86
        feijao_data = db["feijao_cozido"]
        
        meal["itens"].append({
            "item": "Feijão cozido",
            "qtd": 1,
            "unidade": "concha",
            "kcal": round(feijao_g * feijao_data["kcal_por_g"])
        })
        meal["carb_g"] += feijao_g * feijao_data["carb_por_g"]
        meal["protein_g"] += feijao_g * feijao_data["proteina_por_g"]
        
        # Azeite
        azeite_g = 5
        azeite_data = db["azeite_extra_virgem"]
        
        meal["itens"].append({
            "item": "Azeite extra virgem",
            "qtd": azeite_g,
            "unidade": "g",
            "kcal": round(azeite_g * azeite_data["kcal_por_g"])
        })
        meal["fat_g"] += azeite_g * azeite_data["gordura_por_g"]
    
    # Calcular totais
    meal["kcal"] = sum(item["kcal"] for item in meal["itens"])
    meal["protein_g"] = round(meal["protein_g"], 1)
    meal["carb_g"] = round(meal["carb_g"], 1)
    meal["fat_g"] = round(meal["fat_g"], 1)
    
    return meal

def build_lanche_from_template(kcal_target, remaining_macros):
    """Constrói lanche usando template padrão"""
    
    recipes = get_recipes()
    
    # Usar panqueca proteica como base e ajustar
    base_recipe = recipes["panqueca_proteica"]
    
    # Calcular fator de ajuste
    factor = kcal_target / base_recipe["kcal"]
    
    meal = {
        "kcal": kcal_target,
        "protein_g": round(base_recipe["proteina_g"] * factor, 1),
        "carb_g": round(base_recipe["carb_g"] * factor, 1),
        "fat_g": round(base_recipe["gordura_g"] * factor, 1),
        "itens": []
    }
    
    # Ajustar itens
    for item in base_recipe["itens"]:
        adjusted_item = item.copy()
        if item["unidade"] == "g":
            adjusted_item["qtd"] = round(item["qtd"] * factor)
        adjusted_item["kcal"] = round(item["kcal"] * factor)
        meal["itens"].append(adjusted_item)
    
    return meal

def build_ceia(kcal_target):
    """Constrói ceia padrão"""
    
    db = get_food_data()
    
    meal = {
        "kcal": 0,
        "protein_g": 0,
        "carb_g": 0,
        "fat_g": 0,
        "itens": []
    }
    
    # Componentes fixos da ceia
    # Whey (varia de 15-35g)
    whey_g = min(35, max(15, round(kcal_target * 0.35 / 4.06)))
    whey_data = db["whey_protein"]
    
    meal["itens"].append({
        "item": "Whey Protein",
        "qtd": whey_g,
        "unidade": "g",
        "kcal": round(whey_g * whey_data["kcal_por_g"])
    })
    meal["protein_g"] += whey_g * whey_data["proteina_por_g"]
    meal["carb_g"] += whey_g * whey_data["carb_por_g"]
    meal["fat_g"] += whey_g * whey_data["gordura_por_g"]
    
    # Iogurte (100-150g)
    iogurte_g = 120
    iogurte_data = db["iogurte_natural_desnatado"]
    
    meal["itens"].append({
        "item": "Iogurte natural desnatado",
        "qtd": iogurte_g,
        "unidade": "g",
        "kcal": round(iogurte_g * iogurte_data["kcal_por_g"])
    })
    meal["protein_g"] += iogurte_g * iogurte_data["proteina_por_g"]
    meal["carb_g"] += iogurte_g * iogurte_data["carb_por_g"]
    meal["fat_g"] += iogurte_g * iogurte_data["gordura_por_g"]
    
    # Fruta (75-100g)
    fruta_g = 85
    fruta_data = db["frutas_gerais"]
    
    meal["itens"].append({
        "item": "Fruta (exceto banana e abacate)",
        "qtd": fruta_g,
        "unidade": "g",
        "kcal": round(fruta_g * fruta_data["kcal_por_g"])
    })
    meal["protein_g"] += fruta_g * fruta_data["proteina_por_g"]
    meal["carb_g"] += fruta_g * fruta_data["carb_por_g"]
    meal["fat_g"] += fruta_g * fruta_data["gordura_por_g"]
    
    # Chia (5-10g)
    chia_g = 7
    chia_data = db["chia"]
    
    meal["itens"].append({
        "item": "Chia",
        "qtd": chia_g,
        "unidade": "g",
        "kcal": round(chia_g * chia_data["kcal_por_g"])
    })
    meal["protein_g"] += chia_g * chia_data["proteina_por_g"]
    meal["carb_g"] += chia_g * chia_data["carb_por_g"]
    meal["fat_g"] += chia_g * chia_data["gordura_por_g"]
    
    # Calcular totais
    meal["kcal"] = sum(item["kcal"] for item in meal["itens"])
    meal["protein_g"] = round(meal["protein_g"], 1)
    meal["carb_g"] = round(meal["carb_g"], 1)
    meal["fat_g"] = round(meal["fat_g"], 1)
    
    return meal

def enforce_protein_rule(meals):
    """Garante que P≥C em todas as refeições (exceto pré-treino)"""
    
    db = get_food_data()
    
    for meal_name, meal in meals.items():
        if meal_name == "pre_treino":
            continue
        
        # Verificar regra P≥C
        if meal["protein_g"] < meal["carb_g"]:
            # Ajustar aumentando proteína ou reduzindo carbo
            diff = meal["carb_g"] - meal["protein_g"]
            
            # Adicionar whey protein para aumentar proteína
            whey_needed = round(diff / 0.8)
            whey_data = db["whey_protein"]
            
            # Verificar se já tem whey na refeição
            whey_item = None
            for item in meal["itens"]:
                if "Whey" in item["item"]:
                    whey_item = item
                    break
            
            if whey_item:
                # Aumentar quantidade existente
                old_qtd = whey_item["qtd"]
                whey_item["qtd"] += whey_needed
                whey_item["kcal"] = round(whey_item["qtd"] * whey_data["kcal_por_g"])
            else:
                # Adicionar novo item
                meal["itens"].append({
                    "item": "Whey Protein",
                    "qtd": whey_needed,
                    "unidade": "g",
                    "kcal": round(whey_needed * whey_data["kcal_por_g"])
                })
            
            # Recalcular macros
            meal["protein_g"] += whey_needed * whey_data["proteina_por_g"]
            meal["carb_g"] += whey_needed * whey_data["carb_por_g"]
            meal["fat_g"] += whey_needed * whey_data["gordura_por_g"]
            meal["kcal"] = sum(item["kcal"] for item in meal["itens"])
    
    return meals

def adjust_precision(meals, total_kcal_goal):
    """Ajusta para precisão de ±10 kcal"""
    
    # Calcular total atual
    current_total = sum(meal["kcal"] for meal in meals.values())
    diff = total_kcal_goal - current_total
    
    # Se está dentro da margem, retornar
    if abs(diff) <= 10:
        return meals
    
    # Ajustar na maior refeição (geralmente almoço ou jantar)
    largest_meal_name = max(meals.keys(), key=lambda k: meals[k]["kcal"] if k != "pre_treino" else 0)
    largest_meal = meals[largest_meal_name]
    
    # Ajustar proteína principal
    for item in largest_meal["itens"]:
        if "frango" in item["item"].lower() or "carne" in item["item"].lower():
            # Calcular ajuste necessário
            kcal_per_g = 1.84  # frango
            g_adjustment = round(diff / kcal_per_g)
            
            if item["unidade"] == "g":
                item["qtd"] += g_adjustment
                item["kcal"] += round(g_adjustment * kcal_per_g)
                
                # Atualizar macros da refeição
                largest_meal["protein_g"] += g_adjustment * 0.31
                largest_meal["kcal"] = sum(i["kcal"] for i in largest_meal["itens"])
                break
    
    return meals

def add_substitutions(meals):
    """Adiciona opções de substituição"""
    
    rules = get_substitution_rules()
    templates = get_meal_templates()
    
    for meal_name, meal in meals.items():
        if meal_name == "almoco" or meal_name == "jantar":
            meal["substituicoes"] = {
                "proteina": rules["proteinas"]["substitutos"],
                "carboidrato": list(rules["carboidratos"]["equivalencias"]["100g arroz"]),
                "leguminosa": rules["leguminosas"]["substitutos"],
                "legumes_variados": rules["legumes_variados"]
            }
        
        elif meal_name == "lanche":
            # Adicionar 6 opções de lanche
            meal["opcoes_substituicao"] = templates["lanches_padrao"]
        
        elif meal_name == "jantar" and "hamburguer" not in str(meal.get("itens", [])):
            # Adicionar 4 opções de jantar
            meal["opcoes_jantar"] = templates["jantares_padrao"]
    
    return meals

def format_meal_plan(nome, meals, macros, total_kcal):
    """Formata o plano no padrão Pedro Barros"""
    
    from datetime import datetime
    
    # Data atual
    data_atual = datetime.now().strftime("%d/%m/%Y")
    
    # Calcular totais finais
    total_protein = sum(meal.get("protein_g", 0) for meal in meals.values())
    total_carb = sum(meal.get("carb_g", 0) for meal in meals.values())
    total_fat = sum(meal.get("fat_g", 0) for meal in meals.values())
    total_kcal_calculated = sum(meal.get("kcal", 0) for meal in meals.values())
    
    plan = {
        "header": {
            "titulo": "Plano Alimentar",
            "nome": nome,
            "data": data_atual,
            "tipo": "Todos os dias - Dieta única"
        },
        "summary": {
            "total_kcal_calculado": round(total_kcal_calculated),
            "total_kcal_meta": total_kcal,
            "total_proteina_g": round(total_protein, 1),
            "total_carb_g": round(total_carb, 1),
            "total_gordura_g": round(total_fat, 1),
            "meta_proteina_g": macros["protein_g"],
            "meta_carb_g": macros["carb_g"],
            "meta_gordura_g": macros["fat_g"],
            "precisao_kcal": abs(total_kcal_calculated - total_kcal) <= 10
        },
        "meals": meals,
        "footer": "Este documento é de uso exclusivo do destinatário e pode ter conteúdo confidencial. Se você não for o destinatário, qualquer uso, cópia, divulgação ou distribuição é estritamente proibido."
    }
    
    return plan
