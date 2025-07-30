# logic.py (Versão de Produção v2.0)

from database import get_food_data, get_meal_components
from datetime import datetime
import random

# --- FUNÇÕES AUXILIARES DE CÁLCULO ---

def calculate_macros(item_id, gramas, db):
    """Calcula os macros para um item e quantidade específicos."""
    food = db.get(item_id)
    if not food:
        return {"kcal": 0, "p": 0, "c": 0, "g": 0}
    return {
        "kcal": food["kcal"] * gramas,
        "p": food["p"] * gramas,
        "c": food["c"] * gramas,
        "g": food["g"] * gramas,
    }

# --- FUNÇÕES DE CONSTRUÇÃO DE BLOCOS DE REFEIÇÃO ---

def build_meal_block(meal_type, target_kcal, db_foods, db_components):
    """
    Constrói um bloco de refeição completo com uma opção principal e substituições.
    Esta é uma implementação que demonstra a estrutura. Um otimizador real
    ajustaria as 'gramas_base' para atingir a 'target_kcal' com precisão.
    """
    meal_options = db_components.get(meal_type, [])
    if not meal_options:
        return None

    # Seleciona aleatoriamente os componentes para o bloco
    random.shuffle(meal_options)
    
    # Define a primeira opção como principal
    main_option_template = meal_options[0]
    
    # Lógica simplificada de porções - um otimizador real seria mais complexo
    gramas_base = {
        "proteina": 150, "carboidrato": 100, "legumes": 120, "ovo": 100, "whey": 30
    }

    def create_meal_from_template(template):
        """Cria uma refeição individual a partir de um template."""
        meal_items = []
        total_macros = {"kcal": 0, "p": 0, "c": 0, "g": 0}
        
        # Lógica de exemplo para montar a refeição
        # Isso seria muito mais sofisticado em produção
        if "frango" in template["id"] or "tilapia" in template["id"]:
            macros = calculate_macros(template["ingredientes_base"][0], gramas_base["proteina"], db_foods)
            meal_items.append({"item": template["nome_template"], "qtd": gramas_base["proteina"], "unidade": "g"})
        else: # Lanches, etc.
            macros = calculate_macros(template["ingredientes_base"][0], gramas_base["ovo"], db_foods)
            meal_items.append({"item": template["nome_template"], "qtd": 2, "unidade": "un"})

        for key in total_macros:
            total_macros[key] += macros[key]
            
        return {
            "nome": template["nome_template"],
            "kcal_total_refeicao": round(total_macros["kcal"]),
            "itens": meal_items
        }

    main_meal = create_meal_from_template(main_option_template)
    substitutions = []
    for sub_template in meal_options[1:5]: # Pega até 4 substituições
        substitutions.append(create_meal_from_template(sub_template))

    main_meal["substituicoes"] = substitutions
    return main_meal


# --- FUNÇÃO PRINCIPAL DE LÓGICA ---

def generate_plan_logic(request_data):
    """
    Motor de Lógica v2.0 - Estruturado para otimização e construção de blocos.
    """
    paciente_info = request_data.get('paciente', {})
    metas = request_data.get('metas', {})
    
    # Validação de dados essenciais
    peso_kg = paciente_info.get('peso_kg')
    meta_kcal = metas.get('kcal_total')
    if not peso_kg or not meta_kcal:
        return {"erro": "Dados insuficientes. 'peso_kg' e 'kcal_total' são obrigatórios."}, 400

    # Carrega bases de dados
    db_foods = get_food_data()
    db_components = get_meal_components()

    # Define a estrutura do plano (ex: 4 refeições + ceia opcional)
    # A lógica de decisão (ex: incluir ceia ou não) seria baseada nas metas
    meal_structure = ["almoço", "lanche", "jantar", "ceia"]
    
    # Distribuição de calorias (exemplo simples)
    # Um sistema real usaria as regras (ex: última refeição com mais kcal)
    kcal_distribution = {
        "almoço": meta_kcal * 0.35,
        "lanche": meta_kcal * 0.20,
        "jantar": meta_kcal * 0.35,
        "ceia": meta_kcal * 0.10,
    }

    # Monta o plano refeição por refeição
    final_refeicoes = []
    summary_macros = {"kcal": 0, "p": 0, "c": 0, "g": 0}
    
    horarios = {"almoço": "12:30", "lanche": "16:00", "jantar": "20:00", "ceia": "22:30"}

    for meal_name in meal_structure:
        target_kcal = kcal_distribution[meal_name]
        
        # Chama o construtor de blocos para criar a refeição com substituições
        meal_block = build_meal_block(meal_name, target_kcal, db_foods, db_components)
        
        if meal_block:
            # Adiciona horário e ajusta o nome
            meal_block["horario"] = horarios[meal_name]
            meal_block["nome_refeicao"] = meal_name.replace("_", " ").title()
            
            # Atualiza o resumo total (a partir da refeição principal do bloco)
            # A lógica de cálculo de macros totais precisa ser implementada aqui
            summary_macros["kcal"] += meal_block["kcal_total_refeicao"]
            final_refeicoes.append(meal_block)

    # ** PONTO DE OTIMIZAÇÃO **
    # Aqui entraria um loop que compara `summary_macros` com as metas totais
    # e ajustaria as porções dentro dos `meal_block` para convergir para a solução ideal.
    # Por enquanto, retornamos o plano montado.

    # Monta a resposta final
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
