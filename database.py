# database.py (Versão de Produção v2.0)

def get_food_data():
    """
    Base de dados de alimentos.
    Expandida para incluir mais itens dos planos de exemplo.
    Valores por 1 grama do alimento.
    """
    return {
        # Proteínas
        "frango_grelhado": {"kcal": 1.65, "p": 0.31, "c": 0, "g": 0.04},
        "patinho_moido_cru": {"kcal": 1.33, "p": 0.21, "c": 0, "g": 0.05},
        "tilapia_grelhada": {"kcal": 1.28, "p": 0.26, "c": 0, "g": 0.03},
        "ovo_inteiro": {"kcal": 1.49, "p": 0.125, "c": 0.01, "g": 0.10}, # 1 un = ~50g
        "clara_ovo": {"kcal": 0.52, "p": 0.11, "c": 0.007, "g": 0.002}, # 1 un = ~34g
        "whey_protein_isolado": {"kcal": 3.8, "p": 0.85, "c": 0.04, "g": 0.03},
        "atum_enlatado_agua": {"kcal": 1.16, "p": 0.26, "c": 0, "g": 0.01},

        # Carboidratos
        "arroz_branco_cozido": {"kcal": 1.3, "p": 0.025, "c": 0.28, "g": 0.002},
        "batata_doce_cozida": {"kcal": 0.86, "p": 0.016, "c": 0.2, "g": 0.001},
        "pao_forma_integral": {"kcal": 2.65, "p": 0.13, "c": 0.49, "g": 0.04},
        "tapioca_seca": {"kcal": 3.5, "p": 0, "c": 0.87, "g": 0},
        "aveia_flocos": {"kcal": 3.89, "p": 0.17, "c": 0.66, "g": 0.07},
        "banana": {"kcal": 0.89, "p": 0.01, "c": 0.23, "g": 0.003},
        "pao_hamburguer": {"kcal": 2.8, "p": 0.09, "c": 0.52, "g": 0.04},
        "rap10": {"kcal": 3.1, "p": 0.09, "c": 0.6, "g": 0.03}, # 1 un = ~33g

        # Gorduras e Laticínios
        "mussarela": {"kcal": 3.0, "p": 0.22, "c": 0.02, "g": 0.22},
        "requeijao_light": {"kcal": 1.8, "p": 0.11, "c": 0.04, "g": 0.14},
        "iogurte_desnatado": {"kcal": 0.42, "p": 0.04, "c": 0.06, "g": 0},
        "creme_leite_light": {"kcal": 1.16, "p": 0.02, "c": 0.04, "g": 0.1},

        # Fibras e Outros
        "chia": {"kcal": 4.86, "p": 0.17, "c": 0.42, "g": 0.31},
        "psyllium": {"kcal": 3.7, "p": 0.015, "c": 0.8, "g": 0.005},
        "legumes_variados": {"kcal": 0.25, "p": 0.015, "c": 0.05, "g": 0.002}, # Média
    }

def get_meal_components():
    """
    Biblioteca de Componentes Modulares de Refeição.
    Cada componente é uma receita ou uma opção de refeição completa.
    A lógica irá calcular as porções para atingir as metas.
    """
    return {
        "lanche": [
            {
                "id": "panqueca_proteica",
                "nome_template": "Panqueca de Banana e Whey",
                "ingredientes_base": ["ovo_inteiro", "whey_protein_isolado", "banana", "aveia_flocos"]
            },
            {
                "id": "crepioca_proteica",
                "nome_template": "Crepioca com Queijo",
                "ingredientes_base": ["ovo_inteiro", "tapioca_seca", "requeijao_light"]
            },
            {
                "id": "iogurte_turbinado",
                "nome_template": "Iogurte com Whey e Frutas",
                "ingredientes_base": ["iogurte_desnatado", "whey_protein_isolado", "banana", "chia"]
            },
            {
                "id": "refeicao_salgada_leve",
                "nome_template": "Frango com Legumes",
                "ingredientes_base": ["frango_grelhado", "legumes_variados"]
            },
            {
                "id": "omelete_recheado",
                "nome_template": "Omelete com Queijo",
                "ingredientes_base": ["ovo_inteiro", "clara_ovo", "mussarela"]
            }
        ],
        "jantar": [
            {
                "id": "refeicao_padrao",
                "nome_template": "Tilápia com Batata Doce e Legumes",
                "ingredientes_base": ["tilapia_grelhada", "batata_doce_cozida", "legumes_variados"]
            },
            {
                "id": "hamburguer_artesanal",
                "nome_template": "Hambúrguer Artesanal Controlado",
                "ingredientes_base": ["pao_hamburguer", "patinho_moido_cru", "mussarela"]
            },
            {
                "id": "pizza_fake",
                "nome_template": "Pizza Fake de Rap10",
                "ingredientes_base": ["rap10", "frango_grelhado", "mussarela"]
            },
            {
                "id": "strogonoff_light",
                "nome_template": "Strogonoff Light de Frango",
                "ingredientes_base": ["frango_grelhado", "creme_leite_light", "arroz_branco_cozido"]
            }
        ],
        "ceia": [
            {
                "id": "ceia_padrao",
                "nome_template": "Ceia Proteica",
                "ingredientes_base": ["iogurte_desnatado", "whey_protein_isolado", "chia", "psyllium"]
            }
        ]
    }
