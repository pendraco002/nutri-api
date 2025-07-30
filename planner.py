from database import get_food_data, get_recipes
import math

def calculate_macros(weight_kg, height_cm, age_years, gender, activity_factor, goal, total_kcal_input=None):
    # Implementação da fórmula de Harris-Benedict para TMB (Taxa Metabólica Basal)
    if gender == "masculino":
        tmb = 66.5 + (13.75 * weight_kg) + (5.003 * height_cm) - (6.75 * age_years)
    elif gender == "feminino":
        tmb = 655.1 + (9.563 * weight_kg) + (1.850 * height_cm) - (4.676 * age_years)
    else:
        raise ValueError("Gênero inválido. Use 'masculino' ou 'feminino'.")

    # Ajuste para nível de atividade
    kcal_base = tmb * activity_factor

    # Ajuste para objetivo (emagrecimento/ganho de massa)
    if goal == "emagrecimento":
        total_kcal = kcal_base - 500  # Déficit de 500 kcal
    elif goal == "ganho_de_massa":
        total_kcal = kcal_base + 400  # Superávit de 400 kcal
    else: # Manutenção ou outro objetivo
        total_kcal = kcal_base

    # Se o usuário forneceu um total de kcal, priorize-o
    if total_kcal_input is not None:
        total_kcal = total_kcal_input

    return round(total_kcal)

def create_meal_plan(patient_data):
    # Dados do paciente
    nome = patient_data.get("nome", "Paciente")
    sexo = patient_data.get("sexo", "feminino").lower()
    peso = patient_data.get("peso", 70)
    altura = patient_data.get("altura", 170)
    idade = patient_data.get("idade", 30) # Idade não estava nos inputs, adicionar como default ou solicitar
    objetivo = patient_data.get("objetivo", "manutencao").lower()
    restricoes = patient_data.get("restricoes", "").lower()
    num_refeicoes = patient_data.get("num_refeicoes", 4)
    dias_treino = patient_data.get("dias_treino", []).lower()
    total_kcal_input = patient_data.get("meta_calorias", None)
    proteina_min_g_input = patient_data.get("proteina_min_g", None)
    carb_max_perc_input = patient_data.get("carb_max_perc", None)
    gordura_max_perc_input = patient_data.get("gordura_max_perc", None)
    fibras_min_g_input = patient_data.get("fibras_min_g", None)

    # Fator de atividade (simplificado para este exemplo, idealmente seria mais detalhado)
    activity_factor = 1.5 # Assumindo atividade moderada

    # 1. Calcular as calorias totais
    total_kcal = calculate_macros(peso, altura, idade, sexo, activity_factor, objetivo, total_kcal_input)

    # 2. Calcular macros com base nas regras de Pedro Barros
    # Proteína: 1.8g a 2.5g por kg de peso corporal
    proteina_g = max(1.8 * peso, proteina_min_g_input if proteina_min_g_input else 0)
    proteina_g = min(proteina_g, 2.5 * peso) # Limite superior da faixa
    kcal_proteina = proteina_g * 4

    # Carboidrato e Gordura como residual
    kcal_restante = total_kcal - kcal_proteina

    # Distribuição padrão de carboidratos e gorduras (ajustável)
    # Regra: Carboidrato: 28% a 38% do total de calorias, nunca inferior a 80g
    # Gordura: Valor residual para completar calorias, entre 0.6g a 0.9g por kg, sempre abaixo de 30%

    # Tentativa inicial de distribuição
    carb_g_target = (total_kcal * 0.35) / 4 # 35% como ponto de partida
    gordura_g_target = (total_kcal * 0.25) / 9 # 25% como ponto de partida

    # Aplicar limites de input se existirem
    if carb_max_perc_input is not None:
        carb_g_target = min(carb_g_target, (total_kcal * carb_max_perc_input / 100) / 4)
    if gordura_max_perc_input is not None:
        gordura_g_target = min(gordura_g_target, (total_kcal * gordura_max_perc_input / 100) / 9)

    # Garantir mínimo de carboidrato
    carb_g_target = max(carb_g_target, 80) # Nunca inferior a 80g

    # Ajustar gordura como residual, respeitando limites
    gordura_g = (kcal_restante - (carb_g_target * 4)) / 9
    gordura_g = max(gordura_g, 0.6 * peso) # Mínimo de gordura
    gordura_g = min(gordura_g, 0.9 * peso) # Máximo de gordura
    gordura_g = min(gordura_g, (total_kcal * 0.30) / 9) # Abaixo de 30% das calorias totais

    # Recalcular carboidrato se gordura foi ajustada e sobrou kcal
    carb_g = (kcal_restante - (gordura_g * 9)) / 4
    carb_g = max(carb_g, 80) # Reforçar mínimo de carboidrato

    # Fibras: no mínimo, 15g para cada 1000 kcal do plano
    fibras_g = max((total_kcal / 1000) * 15, fibras_min_g_input if fibras_min_g_input else 0)

    # Arredondar macros
    proteina_g = round(proteina_g, 1)
    carb_g = round(carb_g, 1)
    gordura_g = round(gordura_g, 1)
    fibras_g = round(fibras_g, 1)

    # 3. Distribuição Padrão de Calorias por Refeição
    # Regras de `regras_calculos_nutricionais.txt`
    distribuicao_padrao = {
        "cafe_da_manha": 0.20, # 20-25%
        "almoco": 0.30,      # 30-35%
        "lanche": 0.15,      # 15-20%
        "jantar": 0.25,      # 25-30%
        "ceia": 0.05         # 5-10%
    }

    # Ajustar distribuição se o número de refeições for diferente
    # Esta é uma simplificação. Idealmente, o GPT faria isso de forma mais inteligente.
    refeicoes_nomes = []
    if num_refeicoes == 3:
        refeicoes_nomes = ["Almoço", "Lanche", "Jantar"]
        # Ajustar % para 3 refeições
        distribuicao_padrao["almoco"] = 0.40
        distribuicao_padrao["lanche"] = 0.20
        distribuicao_padrao["jantar"] = 0.40
    elif num_refeicoes == 4:
        refeicoes_nomes = ["Café da manhã", "Almoço", "Lanche", "Jantar"]
        # Ajustar % para 4 refeições
        distribuicao_padrao["cafe_da_manha"] = 0.20
        distribuicao_padrao["almoco"] = 0.35
        distribuicao_padrao["lanche"] = 0.15
        distribuicao_padrao["jantar"] = 0.30
    elif num_refeicoes == 5:
        refeicoes_nomes = ["Café da manhã", "Almoço", "Lanche", "Jantar", "Ceia"]
    else:
        # Default para 4 refeições se não especificado ou inválido
        refeicoes_nomes = ["Café da manhã", "Almoço", "Lanche", "Jantar"]
        num_refeicoes = 4

    # Adicionar pré-treino se aplicável (sempre 120 kcal de carboidrato)
    if patient_data.get("incluir_pre_treino", False):
        # Assumindo que o pré-treino é uma refeição adicional e não conta no num_refeicoes principal
        # e que é apenas carboidrato
        pre_treino_kcal = 120
        pre_treino_carb_g = pre_treino_kcal / 4
        total_kcal -= pre_treino_kcal # Reduzir do total para distribuir o restante
        # Adicionar o pré-treino como uma refeição separada no plano final

    # 4. Seleção e Ajuste de Alimentos (Lógica Simplificada)
    # Esta é a parte mais complexa e onde o GPT fará a maior parte do trabalho
    # Aqui, vamos simular a seleção de alguns itens para demonstrar a estrutura

    food_db = get_food_data()
    recipes_db = get_recipes()

    # Exemplo de como montar uma refeição (Almoço)
    # A lógica real precisaria iterar sobre os alimentos e ajustar porções
    # para atingir as metas de macro e kcal para cada refeição, respeitando P>=C

    # Este é um placeholder. A lógica real de seleção de alimentos e ajuste de porções
    # para atingir as metas de macro e kcal por refeição, respeitando P>=C, é o cerne
    # do que o Custom GPT fará com a base de conhecimento e suas instruções.
    # A API aqui apenas fornece a estrutura e os macros calculados.

    # Para este exemplo, vamos retornar um plano genérico com os macros calculados
    # e algumas refeições de exemplo, esperando que o GPT preencha os detalhes.

    # Estrutura de retorno para o GPT preencher
    plano_gerado = {
        "nome_paciente": nome,
        "data": "{}".format(patient_data.get("data", "DD/MM/AAAA")),
        "total_kcal_calculado": total_kcal,
        "proteina_g_calculado": proteina_g,
        "carb_g_calculado": carb_g,
        "gordura_g_calculado": gordura_g,
        "fibras_g_calculado": fibras_g,
        "refeicoes": []
    }

    # Adicionar pré-treino se aplicável
    if patient_data.get("incluir_pre_treino", False):
        plano_gerado["refeicoes"].append({
            "nome": "Pré-treino",
            "horario": "Horário do Treino - 30min",
            "kcal_estimado": 120,
            "macros_estimados": {"carb": pre_treino_carb_g, "prot": 0, "gord": 0},
            "itens": [
                {"item": "Carboidrato de rápida absorção", "qtd": "variável", "unidade": "g", "kcal": 120}
            ],
            "observacoes": "Apenas carboidrato. Consumir 30 minutos antes do treino."
        })

    # Simular a criação de refeições com base na distribuição padrão
    for ref_nome_curto, percentual in distribuicao_padrao.items():
        if ref_nome_curto == "cafe_da_manha" and "Café da manhã" not in refeicoes_nomes: continue
        if ref_nome_curto == "almoco" and "Almoço" not in refeicoes_nomes: continue
        if ref_nome_curto == "lanche" and "Lanche" not in refeicoes_nomes: continue
        if ref_nome_curto == "jantar" and "Jantar" not in refeicoes_nomes: continue
        if ref_nome_curto == "ceia" and "Ceia" not in refeicoes_nomes: continue

        kcal_refeicao = round(total_kcal * percentual)
        # A lógica real aqui seria preencher com alimentos do food_db e recipes_db
        # para atingir kcal_refeicao e respeitar os macros gerais e P>=C
        # Para este exemplo, vamos apenas indicar que o GPT deve preencher

        # Placeholder para itens e macros. O GPT usará a base de conhecimento para preencher isso.
        itens_placeholder = []
        observacoes_placeholder = "O GPT deve preencher esta refeição com alimentos da base de conhecimento, respeitando as regras de Pedro Barros (P>=C, etc.)."

        if ref_nome_curto == "jantar" and "hamburguer_artesanal" in restricoes: # Exemplo de caso especial
            jantar_hamburguer = recipes_db["hamburguer_artesanal"]
            itens_placeholder = jantar_hamburguer["itens"]
            kcal_refeicao = jantar_hamburguer["kcal"]
            observacoes_placeholder = "Hambúrguer artesanal conforme solicitação. O GPT deve adicionar substituições."

        if ref_nome_curto == "ceia" and "ceia_padrao" in restricoes: # Exemplo de caso especial
            # A ceia padrão é mais fixa, o GPT pode preencher diretamente
            itens_placeholder = [
                {"item": "whey_protein", "qtd": "15-35", "unidade": "g"},
                {"item": "iogurte_natural_desnatado", "qtd": "100-150", "unidade": "g"},
                {"item": "frutas_variadas", "qtd": "75-100", "unidade": "g"},
                {"item": "psyllium", "qtd": "5-10", "unidade": "g"}
            ]
            observacoes_placeholder = "Ceia padrão obrigatória. O GPT deve adicionar substituições."

        plano_gerado["refeicoes"].append({
            "nome": ref_nome_curto.replace("_", " ").title(),
            "horario": "Horário a definir", # O GPT pode inferir ou perguntar
            "kcal_estimado": kcal_refeicao,
            "macros_estimados": {"prot": "variável", "carb": "variável", "gord": "variável"},
            "itens": itens_placeholder,
            "observacoes": observacoes_placeholder
        })

    # Ajuste final para garantir precisão de +/- 10 kcal (o GPT fará isso na formatação)
    # Aqui, apenas garantimos que os totais estejam próximos
    # A lógica de ajuste fino para +/- 10 kcal será feita pelo GPT na camada de formatação

    return plano_gerado
