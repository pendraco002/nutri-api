# database.py (Versão Final 9.0 - Completo e Sincronizado)

def get_food_data():
    """ Base de dados de alimentos com notas de preparo. Valores por 1 grama. """
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
        "requeijao_light": {"kcal": 1.88, "p": 0.1, "c": 0.05, "g": 0.15, "obs": "ou porção equivalente de creme de ricota light ou queijo cottage"},
        "chia": {"kcal": 4.86, "p": 0.17, "c": 0.42, "g": 0.31, "obs": "Hidratar no iogurte antes de consumir"},
        "psyllium": {"kcal": 3.7, "p": 0.015, "c": 0.8, "g": 0.005, "obs": "Tomar como remédio com 100ml de água"},
        "legumes_variados": {"kcal": 0.25, "p": 0.015, "c": 0.05, "g": 0.002},
        "feijao_carioca_cozido": {"kcal": 0.76, "p": 0.05, "c": 0.14, "g": 0.005},
        "tapioca_seca": {"kcal": 3.5, "p": 0, "c": 0.87, "g": 0},
        "aveia_flocos": {"kcal": 3.89, "p": 0.17, "c": 0.66, "g": 0.07},
        "banana": {"kcal": 0.89, "p": 0.01, "c": 0.23, "g": 0.003},
        "iogurte_desnatado_zero": {"kcal": 0.4, "p": 0.05, "c": 0.06, "g": 0},
        "mussarela_light": {"kcal": 2.5, "p": 0.25, "c": 0.01, "g": 0.15},
        "pao_hamburguer_light": {"kcal": 2.5, "p": 0.09, "c": 0.48, "g": 0.02},
        "rap10_integral": {"kcal": 3.1, "p": 0.09, "c": 0.6, "g": 0.03},
        "molho_tomate_caseiro": {"kcal": 0.3, "p": 0.01, "c": 0.07, "g": 0.001},
        "ketchup_zero": {"kcal": 0.4, "p": 0.01, "c": 0.1, "g": 0},
        "azeite_extra_virgem": {"kcal": 8.84, "p": 0, "c": 0, "g": 1.0},
        "doce_de_leite_light": {"kcal": 3.1, "p": 0.07, "c": 0.55, "g": 0.07},
        "cafe_preto": {"kcal": 0.02, "p": 0, "c": 0, "g": 0},
        "champignon": {"kcal": 0.22, "p": 0.03, "c": 0.03, "g": 0.003},
        "tomate_cereja": {"kcal": 0.18, "p": 0.009, "c": 0.039, "g": 0.002},
        "oregano": {"kcal": 2.65, "p": 0.09, "c": 0.68, "g": 0.04},
    }

def get_meal_templates():
    """ Biblioteca de Componentes Modulares com tipos e detalhes. """
    return {
        "cafe_da_manha": [
            {"id": "cafe_completo_1", "type": "base", "nome_template": "Café da Manhã Completo", "ingredientes": ["ovo_inteiro:100", "pao_forma_integral:50", "requeijao_light:20", "banana:100"]},
        ],
        "lanche": [
            {"id": "panqueca_proteica", "type": "receita", "nome_template": "Panqueca Proteica de Banana", "ingredientes": ["banana:60", "ovo_inteiro:50", "whey_protein_isolado_hidrolisado:25", "aveia_flocos:20"]},
            {"id": "crepioca_proteica", "type": "receita", "nome_template": "Crepioca com Requeijão", "ingredientes": ["tapioca_seca:20", "ovo_inteiro:50", "clara_ovo_pasteurizada:68", "requeijao_light:20"]},
            {"id": "iogurte_turbinado", "type": "base", "nome_template": "Iogurte com Whey e Frutas", "ingredientes": ["iogurte_desnatado_zero:150", "whey_protein_isolado_hidrolisado:30", "banana:100", "chia:10"]},
            {"id": "omelete_completo", "type": "receita", "nome_template": "Omelete com Queijo e Legumes", "ingredientes": ["ovo_inteiro:100", "clara_ovo_pasteurizada:68", "mussarela_light:30", "legumes_variados:50"]},
            {"id": "sanduiche_proteico", "type": "base", "nome_template": "Sanduíche de Frango", "ingredientes": ["pao_forma_integral:50", "peito_frango_grelhado_sem_pele:80", "requeijao_light:20"]},
        ],
        "jantar": [
            {"id": "refeicao_padrao_peixe", "type": "base", "nome_template": "Tilápia com Arroz e Legumes", "ingredientes": ["tilapia_assada:150", "arroz_branco_cozido:100", "legumes_variados:150", "azeite_extra_virgem:5"]},
            {"id": "refeicao_padrao_frango", "type": "base", "nome_template": "Frango com Batata Doce", "ingredientes": ["peito_frango_grelhado_sem_pele:150", "batata_doce_cozida:200", "legumes_variados:150"]},
            {"id": "strogonoff_light", "type": "receita", "nome_template": "Strogonoff Light de Frango", "ingredientes": ["peito_frango_grelhado_sem_pele:120", "requeijao_light:30", "ketchup_zero:10", "champignon:40"]},
            {"id": "hamburguer_artesanal", "type": "receita", "nome_template": "Hambúrguer Artesanal Controlado", "ingredientes": ["pao_hamburguer_light:50", "patinho_moido_95_5:120", "mussarela_light:20", "ketchup_zero:10"]},
            {"id": "pizza_fake", "type": "receita", "nome_template": "Pizza Fake de Rap10", "ingredientes": ["rap10_integral:35", "peito_frango_grelhado_sem_pele:80", "mussarela_light:30", "molho_tomate_caseiro:20", "tomate_cereja:30", "oregano:2"]},
        ],
        "ceia": [
            {"id": "ceia_padrao", "type": "base", "nome_template": "Ceia Proteica", "ingredientes": ["iogurte_desnatado_zero:150", "whey_protein_isolado_hidrolisado:20", "chia:5", "psyllium:5"]},
        ]
    }

def get_substitution_rules():
    """ Regras de substituição textuais. """
    return {
        "peito_frango_grelhado_sem_pele": "porção equivalente de Patinho Moído, Tilápia, Atum ou 3 Ovos",
        "arroz_branco_cozido": "porção equivalente de Batata Inglesa, Batata Doce, Aipim, Macarrão ou Quinoa",
        "feijao_carioca_cozido": "1 concha (substituível por porção equivalente de Lentilha, Grão de Bico ou Ervilha)",
    }

def get_static_info():
    """ Informações estáticas, como orientações especiais. """
    return {
        "legumes_variados": "Tomate, Berinjela, Alho Poró, Brócolis, Rabanete, Chuchu, Couve, Beterraba, Pepino, Couve-Flor, Abobrinha, Repolho, Palmito, Quiabo, Cenoura, Vagem.",
        "orientacao_refeicao_livre": "Nos fins de semana, é permitida 1 refeição livre e controlada. Exemplos: 1 hambúrguer artesanal + sobremesa; 3 fatias de pizza; 1 combinado de 20 peças de comida japonesa."
    }
