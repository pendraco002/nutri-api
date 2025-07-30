# database.py (Versão Final 2.0 - Otimizada para Baixa Gordura)

def get_food_data():
    """
    Base de dados de alimentos otimizada com fontes de proteína magra.
    Valores por 1 grama do alimento.
    """
    return {
        # --- PROTEÍNAS ESTRATÉGICAS (BAIXÍSSIMA GORDURA) ---
        "peito_frango_grelhado_sem_pele": {"kcal": 1.65, "p": 0.31, "c": 0, "g": 0.036},
        "clara_ovo_pasteurizada": {"kcal": 0.52, "p": 0.11, "c": 0.007, "g": 0.002},
        "whey_protein_isolado_hidrolisado": {"kcal": 3.7, "p": 0.9, "c": 0.01, "g": 0.01}, # Whey de altíssima pureza
        "tilapia_assada": {"kcal": 1.28, "p": 0.26, "c": 0, "g": 0.026},
        "atum_solido_em_agua": {"kcal": 1.1, "p": 0.25, "c": 0, "g": 0.01},

        # --- PROTEÍNAS COM GORDURA MODERADA ---
        "patinho_moido_95_5": {"kcal": 1.5, "p": 0.22, "c": 0, "g": 0.06}, # Patinho com 5% de gordura
        "ovo_inteiro": {"kcal": 1.49, "p": 0.125, "c": 0.01, "g": 0.10},
        
        # --- CARBOIDRATOS ---
        "arroz_branco_cozido": {"kcal": 1.3, "p": 0.025, "c": 0.28, "g": 0.002},
        "batata_doce_cozida": {"kcal": 0.86, "p": 0.016, "c": 0.2, "g": 0.001},
        "pao_forma_integral": {"kcal": 2.65, "p": 0.13, "c": 0.49, "g": 0.04},
        "tapioca_seca": {"kcal": 3.5, "p": 0, "c": 0.87, "g": 0},
        "aveia_flocos": {"kcal": 3.89, "p": 0.17, "c": 0.66, "g": 0.07},
        "banana": {"kcal": 0.89, "p": 0.01, "c": 0.23, "g": 0.003},
        "pao_hamburguer_light": {"kcal": 2.5, "p": 0.09, "c": 0.48, "g": 0.02},
        "rap10_integral": {"kcal": 3.1, "p": 0.09, "c": 0.6, "g": 0.03},

        # --- GORDURAS E LATICÍNIOS ---
        "mussarela_light": {"kcal": 2.5, "p": 0.25, "c": 0.01, "g": 0.15},
        "requeijao_zero_gordura": {"kcal": 1.2, "p": 0.15, "c": 0.05, "g": 0.01},
        "iogurte_desnatado_zero": {"kcal": 0.4, "p": 0.05, "c": 0.06, "g": 0},
        "azeite_extra_virgem": {"kcal": 8.84, "p": 0, "c": 0, "g": 1.0},

        # --- FIBRAS E OUTROS ---
        "chia": {"kcal": 4.86, "p": 0.17, "c": 0.42, "g": 0.31},
        "psyllium": {"kcal": 3.7, "p": 0.015, "c": 0.8, "g": 0.005},
        "legumes_variados": {"kcal": 0.25, "p": 0.015, "c": 0.05, "g": 0.002},
    }

def get_meal_components():
    """
    Biblioteca de Componentes Modulares de Refeição.
    Atualizada para usar os ingredientes otimizados.
    """
    return {
        "lanche": [
            {"id": "panqueca_proteica", "nome_template": "Panqueca de Banana e Whey", "ingredientes_base": ["clara_ovo_pasteurizada", "whey_protein_isolado_hidrolisado", "banana", "aveia_flocos"]},
            {"id": "crepioca_proteica", "nome_template": "Crepioca com Requeijão Zero", "ingredientes_base": ["clara_ovo_pasteurizada", "tapioca_seca", "requeijao_zero_gordura"]},
            {"id": "iogurte_turbinado", "nome_template": "Iogurte com Whey e Frutas", "ingredientes_base": ["iogurte_desnatado_zero", "whey_protein_isolado_hidrolisado", "banana", "chia"]},
        ],
        "jantar": [
            {"id": "refeicao_padrao", "nome_template": "Tilápia com Batata Doce", "ingredientes_base": ["tilapia_assada", "batata_doce_cozida", "legumes_variados"]},
            {"id": "hamburguer_artesanal", "nome_template": "Hambúrguer Artesanal Magro", "ingredientes_base": ["pao_hamburguer_light", "patinho_moido_95_5", "mussarela_light"]},
            {"id": "pizza_fake", "nome_template": "Pizza Fake de Rap10", "ingredientes_base": ["rap10_integral", "peito_frango_grelhado_sem_pele", "mussarela_light"]},
        ],
        # ... outras refeições ...
    }
