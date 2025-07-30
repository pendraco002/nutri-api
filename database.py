# database.py (Versão Final 3.0 - Enciclopédia Nutricional Completa)

def get_food_data():
    """
    Base de dados de alimentos otimizada com fontes de proteína magra.
    Valores por 1 grama do alimento.
    """
    return {
        # PROTEÍNAS ESTRATÉGICAS (BAIXÍSSIMA GORDURA)
        "peito_frango_grelhado_sem_pele": {"kcal": 1.65, "p": 0.31, "c": 0, "g": 0.036},
        "clara_ovo_pasteurizada": {"kcal": 0.52, "p": 0.11, "c": 0.007, "g": 0.002},
        "whey_protein_isolado_hidrolisado": {"kcal": 3.7, "p": 0.9, "c": 0.01, "g": 0.01},
        "tilapia_assada": {"kcal": 1.28, "p": 0.26, "c": 0, "g": 0.026},
        "atum_solido_em_agua": {"kcal": 1.1, "p": 0.25, "c": 0, "g": 0.01},

        # PROTEÍNAS COM GORDURA MODERADA
        "patinho_moido_95_5": {"kcal": 1.5, "p": 0.22, "c": 0, "g": 0.06},
        "ovo_inteiro": {"kcal": 1.49, "p": 0.125, "c": 0.01, "g": 0.10},
        
        # CARBOIDRATOS
        "arroz_branco_cozido": {"kcal": 1.3, "p": 0.025, "c": 0.28, "g": 0.002},
        "batata_doce_cozida": {"kcal": 0.86, "p": 0.016, "c": 0.2, "g": 0.001},
        "batata_inglesa_cozida": {"kcal": 0.8, "p": 0.02, "c": 0.18, "g": 0.001},
        "aipim_cozido": {"kcal": 1.6, "p": 0.014, "c": 0.38, "g": 0.003},
        "macarrao_cozido": {"kcal": 1.58, "p": 0.05, "c": 0.31, "g": 0.01},
        "quinoa_cozida": {"kcal": 1.2, "p": 0.044, "c": 0.21, "g": 0.019},
        "pao_forma_integral": {"kcal": 2.65, "p": 0.13, "c": 0.49, "g": 0.04},
        "pao_frances_sem_miolo": {"kcal": 3.0, "p": 0.09, "c": 0.63, "g": 0.03},
        "tapioca_seca": {"kcal": 3.5, "p": 0, "c": 0.87, "g": 0},
        "aveia_flocos": {"kcal": 3.89, "p": 0.17, "c": 0.66, "g": 0.07},
        "banana": {"kcal": 0.89, "p": 0.01, "c": 0.23, "g": 0.003},
        "pao_hamburguer_light": {"kcal": 2.5, "p": 0.09, "c": 0.48, "g": 0.02},
        "rap10_integral": {"kcal": 3.1, "p": 0.09, "c": 0.6, "g": 0.03},

        # GORDURAS E LATICÍNIOS
        "mussarela_light": {"kcal": 2.5, "p": 0.25, "c": 0.01, "g": 0.15},
        "requeijao_light": {"kcal": 1.88, "p": 0.1, "c": 0.05, "g": 0.15},
        "creme_ricota_light": {"kcal": 1.4, "p": 0.11, "c": 0.04, "g": 0.09},
        "queijo_cottage": {"kcal": 0.98, "p": 0.11, "c": 0.03, "g": 0.04},
        "iogurte_desnatado_zero": {"kcal": 0.4, "p": 0.05, "c": 0.06, "g": 0},
        "azeite_extra_virgem": {"kcal": 8.84, "p": 0, "c": 0, "g": 1.0},

        # FIBRAS E OUTROS
        "chia": {"kcal": 4.86, "p": 0.17, "c": 0.42, "g": 0.31},
        "psyllium": {"kcal": 3.7, "p": 0.015, "c": 0.8, "g": 0.005},
        "legumes_variados": {"kcal": 0.25, "p": 0.015, "c": 0.05, "g": 0.002},
        "feijao_carioca_cozido": {"kcal": 0.76, "p": 0.05, "c": 0.14, "g": 0.005},
        "lentilha_cozida": {"kcal": 1.16, "p": 0.09, "c": 0.2, "g": 0.004},
        "grao_de_bico_cozido": {"kcal": 1.39, "p": 0.08, "c": 0.27, "g": 0.02},
    }

def get_substitution_rules():
    """ Regras de substituição com equivalência de gramatura. """
    return {
        "pao_forma_integral": [
            {"nome": "Pão francês sem miolo", "gramas": 40},
            {"nome": "Tapioca", "gramas": 40},
            {"nome": "Aveia em flocos", "gramas": 35},
        ],
        "requeijao_light": [
            {"nome": "Creme de ricota light", "gramas": 20},
            {"nome": "Queijo cottage", "gramas": 20},
        ],
        "arroz_branco_cozido": [
            {"nome": "Batata inglesa cozida", "gramas": 150},
            {"nome": "Batata doce cozida", "gramas": 120},
            {"nome": "Aipim cozido", "gramas": 100},
            {"nome": "Macarrão cozido", "gramas": 100},
            {"nome": "Quinoa cozida", "gramas": 100},
        ],
        "feijao_carioca_cozido": [
            {"nome": "Lentilha cozida", "gramas": 100},
            {"nome": "Grão de bico cozido", "gramas": 100},
        ],
        "peito_frango_grelhado_sem_pele": [
            {"nome": "Patinho moído 95/5", "gramas": 120},
            {"nome": "Tilápia assada", "gramas": 130},
            {"nome": "Ovo inteiro", "gramas": 150},
        ]
    }

def get_static_lists():
    """ Listas estáticas para adicionar ao plano. """
    return {
        "legumes_variados": "Tomate, Berinjela, Alho Poró, Brócolis, Rabanete, Chuchu, Couve, Beterraba, Pepino, Couve-Flor, Abobrinha, Repolho, Palmito, Quiabo, Cenoura, Vagem."
    }

def get_full_recipes():
    """ Receitas completas para as substituições. """
    return {
        "strogonoff_light": {
            "nome_completo": "Strogonoff Light de Frango",
            "ingredientes": [
                {"item": "Filé de frango em cubos", "qtd": "120g"},
                {"item": "Creme de ricota light", "qtd": "30g"},
                {"item": "Ketchup (zero açúcar)", "qtd": "10g"},
                {"item": "Mostarda", "qtd": "5g"},
                {"item": "Champignon fatiado", "qtd": "40g"},
            ]
        },
        "hamburguer_artesanal": {
            "nome_completo": "Hambúrguer Artesanal Controlado",
            "ingredientes": [
                {"item": "Patinho moído 95/5", "qtd": "120g"},
                {"item": "Pão de hambúrguer light", "qtd": "1 unidade"},
                {"item": "Mussarela light", "qtd": "20g"},
                {"item": "Alface e Tomate", "qtd": "à vontade"},
            ]
        },
        "panqueca_proteica": {
            "nome_completo": "Panqueca Proteica de Banana",
            "ingredientes": [
                {"item": "Banana", "qtd": "60g"},
                {"item": "Ovo", "qtd": "1 unidade"},
                {"item": "Whey Protein", "qtd": "25g"},
                {"item": "Cacau em pó", "qtd": "5g"},
                {"item": "Psyllium", "qtd": "5g"},
            ]
        }
    }
