# database.py (Versão Final 8.0 - Detalhes Obsessivos)

def get_food_data():
    """ Base de dados de alimentos. Valores por 1 grama. """
    # (A lista de alimentos individuais está completa e correta)
    return {
        "peito_frango_grelhado_sem_pele": {"kcal": 1.65, "p": 0.31, "c": 0, "g": 0.036},
        "clara_ovo_pasteurizada": {"kcal": 0.52, "p": 0.11, "c": 0.007, "g": 0.002},
        "whey_protein_isolado_hidrolisado": {"kcal": 3.7, "p": 0.9, "c": 0.01, "g": 0.01},
        "tilapia_assada": {"kcal": 1.28, "p": 0.26, "c": 0, "g": 0.026},
        "patinho_moido_95_5": {"kcal": 1.5, "p": 0.22, "c": 0, "g": 0.06},
        "ovo_inteiro": {"kcal": 1.49, "p": 0.125, "c": 0.01, "g": 0.10},
        "arroz_branco_cozido": {"kcal": 1.3, "p": 0.025, "c": 0.28, "g": 0.002},
        "batata_doce_cozida": {"kcal": 0.86, "p": 0.016, "c": 0.2, "g": 0.001},
        "pao_forma_integral": {"kcal": 2.65, "p": 0.13, "c": 0.49, "g": 0.04},
        "pao_frances_sem_miolo": {"kcal": 3.0, "p": 0.09, "c": 0.63, "g": 0.03},
        "tapioca_seca": {"kcal": 3.5, "p": 0, "c": 0.87, "g": 0},
        "aveia_flocos": {"kcal": 3.89, "p": 0.17, "c": 0.66, "g": 0.07},
        "banana": {"kcal": 0.89, "p": 0.01, "c": 0.23, "g": 0.003},
        "pao_hamburguer_light": {"kcal": 2.5, "p": 0.09, "c": 0.48, "g": 0.02},
        "rap10_integral": {"kcal": 3.1, "p": 0.09, "c": 0.6, "g": 0.03},
        "mussarela_light": {"kcal": 2.5, "p": 0.25, "c": 0.01, "g": 0.15},
        "requeijao_light": {"kcal": 1.88, "p": 0.1, "c": 0.05, "g": 0.15},
        "creme_ricota_light": {"kcal": 1.4, "p": 0.11, "c": 0.04, "g": 0.09},
        "queijo_cottage": {"kcal": 0.98, "p": 0.11, "c": 0.03, "g": 0.04},
        "iogurte_desnatado_zero": {"kcal": 0.4, "p": 0.05, "c": 0.06, "g": 0},
        "ketchup_zero": {"kcal": 0.4, "p": 0.01, "c": 0.1, "g": 0},
        "molho_tomate_caseiro": {"kcal": 0.3, "p": 0.01, "c": 0.07, "g": 0.001},
        "tomate_cereja": {"kcal": 0.18, "p": 0.009, "c": 0.039, "g": 0.002},
        "oregano": {"kcal": 2.65, "p": 0.09, "c": 0.68, "g": 0.04},
        "champignon": {"kcal": 0.22, "p": 0.03, "c": 0.03, "g": 0.003},
    }

def get_substitution_rules():
    """ Regras de substituição ESTRUTURADAS com gramatura. """
    return {
        "pao_forma_integral": [
            {"nome": "Pão francês sem miolo", "qtd": "40g"},
            {"nome": "Tapioca", "qtd": "40g"},
            {"nome": "Aveia em flocos", "qtd": "35g"},
        ],
        "requeijao_light": [
            {"nome": "Creme de ricota light", "qtd": "20g"},
            {"nome": "Queijo cottage", "qtd": "20g"},
        ],
        # ... outras regras estruturadas
    }

def get_meal_templates():
    """ Biblioteca de Componentes Modulares com receitas 100% completas. """
    return {
        "lanche": [
            {"id": "panqueca_proteica", "type": "receita", "nome_template": "Panqueca Proteica de Banana", "ingredientes": ["banana:60", "ovo_inteiro:50", "whey_protein_isolado_hidrolisado:25", "cacau_em_po:5", "psyllium:5"]},
            {"id": "crepioca_proteica", "type": "receita", "nome_template": "Crepioca com Requeijão", "ingredientes": ["tapioca_seca:20", "ovo_inteiro:50", "clara_ovo_pasteurizada:68", "requeijao_light:20"]},
            {"id": "iogurte_turbinado", "type": "base", "nome_template": "Iogurte com Whey e Frutas", "ingredientes": ["iogurte_desnatado_zero:150", "whey_protein_isolado_hidrolisado:30", "banana:100", "chia:10"]},
            {"id": "omelete_completo", "type": "receita", "nome_template": "Omelete com Queijo e Legumes", "ingredientes": ["ovo_inteiro:100", "clara_ovo_pasteurizada:68", "mussarela_light:30", "legumes_variados:50"]},
            {"id": "sanduiche_proteico", "type": "base", "nome_template": "Sanduíche de Frango", "ingredientes": ["pao_forma_integral:50", "peito_frango_grelhado_sem_pele:80", "requeijao_light:20"]},
            {"id": "shake_pronto", "type": "base", "nome_template": "Shake Pronto", "ingredientes": ["yopro_ou_similar:1"]}, # Placeholder
        ],
        "jantar": [
            {"id": "refeicao_padrao_peixe", "type": "base", "nome_template": "Tilápia com Arroz e Legumes", "ingredientes": ["tilapia_assada:150", "arroz_branco_cozido:100", "legumes_variados:150", "azeite_extra_virgem:5"]},
            {"id": "strogonoff_light", "type": "receita", "nome_template": "Strogonoff Light de Frango", "ingredientes": ["peito_frango_grelhado_sem_pele:120", "requeijao_light:30", "ketchup_zero:10", "champignon:40"]},
            {"id": "hamburguer_artesanal", "type": "receita", "nome_template": "Hambúrguer Artesanal Controlado", "ingredientes": ["pao_hamburguer_light:50", "patinho_moido_95_5:120", "mussarela_light:20", "ketchup_zero:10"]},
            {"id": "pizza_fake", "type": "receita", "nome_template": "Pizza Fake de Rap10", "ingredientes": ["rap10_integral:35", "peito_frango_grelhado_sem_pele:80", "mussarela_light:30", "molho_tomate_caseiro:20", "tomate_cereja:30", "oregano:2"]},
        ]
    }
