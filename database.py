# Arquivo: database.py (Versão Final)

def get_food_data():
    """ Retorna dados nutricionais básicos por grama ou unidade. """
    return {
        "ovo_inteiro": {"kcal": 70, "proteina_g": 6, "carb_g": 0.5, "gordura_g": 5},
        "clara_de_ovo": {"kcal": 17, "proteina_g": 4, "carb_g": 0.2, "gordura_g": 0},
        "whey_protein": {"kcal_por_g": 4.0, "proteina_por_g": 0.8},
        "pao_integral": {"kcal_por_fatia": 70},
        "arroz_branco_cozido": {"kcal_por_g": 1.3},
        "file_de_frango_grelhado": {"kcal_por_g": 1.65, "proteina_por_g": 0.31},
        "batata_doce_cozida": {"kcal_por_g": 0.86},
        "azeite_extra_virgem": {"kcal_por_g": 8.8},
        "iogurte_desnatado": {"kcal_por_g": 0.55},
        "chia_em_graos": {"kcal_por_g": 4.8},
        "frutas_vermelhas": {"kcal_por_g": 0.5},
        "banana": {"kcal_por_unidade": 90},
        "tapioca_seca": {"kcal_por_g": 3.4},
        "requeijao_light": {"kcal_por_g": 1.8},
        "patinho_moido_grelhado": {"kcal_por_g": 2.05},
        "queijo_mussarela": {"kcal_por_g": 3.0},
        "salmao_grelhado": {"kcal_por_g": 2.06},
        "tilapia_grelhada": {"kcal_por_g": 1.20},
        "pao_de_hamburguer": {"kcal_por_unidade": 180},
        "molho_de_tomate": {"kcal_por_g": 0.5},
        "peito_de_peru": {"kcal_por_g": 1.7}
    }

def get_standard_recipes():
    """ Retorna um dicionário de receitas padronizadas para substituições. """
    return {
        "lanche": [
            {
                "nome": "Panqueca de Banana Proteica",
                "kcal": 285,
                "itens": "1 Banana, 1 Ovo, 20g de Whey Protein. Misturar tudo e grelhar."
            },
            {
                "nome": "Crepioca Recheada",
                "kcal": 260,
                "itens": "30g de Tapioca, 1 Ovo, 2 Claras, 30g de Queijo Cottage. Fazer a crepioca e rechear."
            },
            {
                "nome": "Vitamina Hipercalórica",
                "kcal": 310,
                "itens": "1 Banana, 30g de Aveia, 20g de Pasta de Amendoim, 200ml de Leite (ou vegetal)."
            },
            {
                "nome": "Sanduíche de Frango",
                "kcal": 300,
                "itens": "2 fatias de Pão Integral, 80g de Frango desfiado, 30g de Requeijão Light."
            },
            {
                "nome": "Bowl de Açaí Proteico (sem xarope)",
                "kcal": 320,
                "itens": "150g de Polpa de Açaí, 1 Banana, 20g de Whey Protein."
            },
            {
                "nome": "Ovos Mexidos com Batata Doce",
                "kcal": 290,
                "itens": "2 Ovos inteiros, 100g de Batata Doce cozida em cubos."
            }
        ],
        "jantar": [
            {
                "nome": "Pizza Fake Integral",
                "kcal": 450,
                "itens": "1 Pão Sírio Integral (ou Rap10), 40g de Molho de Tomate, 60g de Queijo Mussarela, 50g de Peito de Peru."
            },
            {
                "nome": "Hambúrguer Artesanal Fit",
                "kcal": 550,
                "itens": "1 Pão de Hambúrguer, 120g de Patinho moído, 30g de Queijo, Salada a gosto."
            },
            {
                "nome": "Salmão Grelhado com Purê",
                "kcal": 520,
                "itens": "150g de Salmão, 200g de Batata Doce (para o purê), Legumes."
            },
            {
                "nome": "Omelete de Forno Completo",
                "kcal": 480,
                "itens": "3 Ovos, 50g de Queijo, 50g de Frango desfiado, Legumes variados."
            }
        ],
        "ceia": {
            "nome": "Ceia Padrão",
            "kcal": 180,
            "itens": [
                {"item": "Iogurte Desnatado", "qtd": 150, "unidade": "g", "kcal": 82},
                {"item": "Whey Protein", "qtd": 15, "unidade": "g", "kcal": 60},
                {"item": "Chia em Grãos", "qtd": 5, "unidade": "g", "kcal": 24},
                {"item": "Frutas Vermelhas", "qtd": 30, "unidade": "g", "kcal": 15}
            ]
        }
    }
