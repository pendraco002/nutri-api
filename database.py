def get_food_data():
    # Esta é uma versão expandida, mas você precisará adicionar TODOS os alimentos
    # de 'equivalencias_nutricionais_corretas_v14.txt' com seus macros.
    return {
        "file_de_frango_grelhado": {"kcal_por_g": 1.65, "proteina_por_g": 0.31, "gordura_por_g": 0.04, "carb_por_g": 0.0},
        "arroz_branco_cozido": {"kcal_por_g": 1.3, "proteina_por_g": 0.025, "gordura_por_g": 0.002, "carb_por_g": 0.28},
        "azeite_extra_virgem": {"kcal_por_g": 8.8, "proteina_por_g": 0.0, "gordura_por_g": 1.0, "carb_por_g": 0.0},
        "ovo_de_galinha_inteiro": {"kcal_por_g": 1.55, "proteina_por_g": 0.13, "gordura_por_g": 0.11, "carb_por_g": 0.01},
        "pao_de_forma_integral": {"kcal_por_g": 2.5, "proteina_por_g": 0.09, "gordura_por_g": 0.03, "carb_por_g": 0.45},
        "requeijao_light": {"kcal_por_g": 1.88, "proteina_por_g": 0.08, "gordura_por_g": 0.15, "carb_por_g": 0.03},
        "iogurte_natural_desnatado": {"kcal_por_g": 0.55, "proteina_por_g": 0.05, "gordura_por_g": 0.0, "carb_por_g": 0.07},
        "mamao": {"kcal_por_g": 0.39, "proteina_por_g": 0.01, "gordura_por_g": 0.0, "carb_por_g": 0.1},
        "chia": {"kcal_por_g": 4.86, "proteina_por_g": 0.17, "gordura_por_g": 0.31, "carb_por_g": 0.42},
        "whey_protein": {"kcal_por_g": 4.0, "proteina_por_g": 0.8, "gordura_por_g": 0.05, "carb_por_g": 0.1},
        "batata_inglesa": {"kcal_por_g": 0.87, "proteina_por_g": 0.02, "gordura_por_g": 0.0, "carb_por_g": 0.2},
        "batata_doce": {"kcal_por_g": 0.86, "proteina_por_g": 0.02, "gordura_por_g": 0.0, "carb_por_g": 0.2},
        "macarrao_cozido": {"kcal_por_g": 1.4, "proteina_por_g": 0.05, "gordura_por_g": 0.01, "carb_por_g": 0.3},
        "aipim_mandioca": {"kcal_por_g": 1.6, "proteina_por_g": 0.01, "gordura_por_g": 0.0, "carb_por_g": 0.38},
        "inhame": {"kcal_por_g": 1.17, "proteina_por_g": 0.01, "gordura_por_g": 0.0, "carb_por_g": 0.27},
        "cuscuz": {"kcal_por_g": 1.12, "proteina_por_g": 0.03, "gordura_por_g": 0.0, "carb_por_g": 0.25},
        "tapioca_seca": {"kcal_por_g": 3.4, "proteina_por_g": 0.0, "gordura_por_g": 0.0, "carb_por_g": 0.85},
        "pao_frances": {"kcal_por_g": 2.86, "proteina_por_g": 0.08, "gordura_por_g": 0.01, "carb_por_g": 0.58},
        "biscoitos_de_arroz": {"kcal_por_g": 4.0, "proteina_por_g": 0.07, "gordura_por_g": 0.04, "carb_por_g": 0.85},
        "patinho_magro": {"kcal_por_g": 2.04, "proteina_por_g": 0.36, "gordura_por_g": 0.06, "carb_por_g": 0.0},
        "alcatra": {"kcal_por_g": 1.98, "proteina_por_g": 0.34, "gordura_por_g": 0.06, "carb_por_g": 0.0},
        "file_mignon": {"kcal_por_g": 2.04, "proteina_por_g": 0.36, "gordura_por_g": 0.06, "carb_por_g": 0.0},
        "file_suino": {"kcal_por_g": 2.12, "proteina_por_g": 0.35, "gordura_por_g": 0.07, "carb_por_g": 0.0},
        "salmao_fresco": {"kcal_por_g": 2.06, "proteina_por_g": 0.2, "gordura_por_g": 0.13, "carb_por_g": 0.0},
        "atum_fresco": {"kcal_por_g": 1.67, "proteina_por_g": 0.23, "gordura_por_g": 0.08, "carb_por_g": 0.0},
        "peixe_branco": {"kcal_por_g": 1.5, "proteina_por_g": 0.2, "gordura_por_g": 0.07, "carb_por_g": 0.0},
        "camarao": {"kcal_por_g": 1.4, "proteina_por_g": 0.24, "gordura_por_g": 0.03, "carb_por_g": 0.0},
        "queijo_cottage": {"kcal_por_g": 0.65, "proteina_por_g": 0.11, "gordura_por_g": 0.01, "carb_por_g": 0.03},
        "queijo_minas_frescal": {"kcal_por_g": 1.08, "proteina_por_g": 0.17, "gordura_por_g": 0.04, "carb_por_g": 0.02},
        "queijo_mussarela": {"kcal_por_g": 3.5, "proteina_por_g": 0.22, "gordura_por_g": 0.28, "carb_por_g": 0.01},
        "feijao_cozido": {"kcal_por_g": 0.61, "proteina_por_g": 0.05, "gordura_por_g": 0.0, "carb_por_g": 0.11},
        "lentilha_cozida": {"kcal_por_g": 0.7, "proteina_por_g": 0.09, "gordura_por_g": 0.0, "carb_por_g": 0.16},
        "grao_de_bico_cozido": {"kcal_por_g": 0.72, "proteina_por_g": 0.09, "gordura_por_g": 0.01, "carb_por_g": 0.12},
        "ervilha_cozida": {"kcal_por_g": 0.6, "proteina_por_g": 0.05, "gordura_por_g": 0.0, "carb_por_g": 0.11},
        "milho_cozido": {"kcal_por_g": 0.9, "proteina_por_g": 0.03, "gordura_por_g": 0.01, "carb_por_g": 0.2},
        "psyllium": {"kcal_por_g": 0.7, "proteina_por_g": 0.0, "gordura_por_g": 0.0, "carb_por_g": 0.0},
        "cacau_em_po_100": {"kcal_por_g": 2.8, "proteina_por_g": 0.2, "gordura_por_g": 0.14, "carb_por_g": 0.1},
        "canela_em_po": {"kcal_por_g": 2.6, "proteina_por_g": 0.04, "gordura_por_g": 0.01, "carb_por_g": 0.8},
        "legumes_variados": {"kcal_por_g": 0.25, "proteina_por_g": 0.01, "gordura_por_g": 0.0, "carb_por_g": 0.05},
        "frutas_variadas": {"kcal_por_g": 0.48, "proteina_por_g": 0.01, "gordura_por_g": 0.0, "carb_por_g": 0.12},
        "gelatina_diet": {"kcal_por_g": 0.1, "proteina_por_g": 0.02, "gordura_por_g": 0.0, "carb_por_g": 0.0},
        "pao_sirio_integral": {"kcal_por_g": 3.0, "proteina_por_g": 0.1, "gordura_por_g": 0.02, "carb_por_g": 0.6},
        "molho_de_tomate": {"kcal_por_g": 0.5, "proteina_por_g": 0.02, "gordura_por_g": 0.0, "carb_por_g": 0.1},
        "peito_de_peru": {"kcal_por_g": 1.7, "proteina_por_g": 0.25, "gordura_por_g": 0.07, "carb_por_g": 0.0},
        "champignon": {"kcal_por_g": 0.22, "proteina_por_g": 0.03, "gordura_por_g": 0.0, "carb_por_g": 0.03},
        "creme_de_leite_light": {"kcal_por_g": 1.5, "proteina_por_g": 0.02, "gordura_por_g": 0.12, "carb_por_g": 0.03},
        "mostarda": {"kcal_por_g": 1.0, "proteina_por_g": 0.05, "gordura_por_g": 0.07, "carb_por_g": 0.03},
        "ketchup": {"kcal_por_g": 1.2, "proteina_por_g": 0.01, "gordura_por_g": 0.0, "carb_por_g": 0.25},
        "pao_de_hamburguer_integral": {"kcal_por_g": 2.2, "proteina_por_g": 0.08, "gordura_por_g": 0.03, "carb_por_g": 0.4},
        "patinho_moido": {"kcal_por_g": 1.8, "proteina_por_g": 0.2, "gordura_por_g": 0.1, "carb_por_g": 0.0},
        "molho_especial": {"kcal_por_g": 3.0, "proteina_por_g": 0.01, "gordura_por_g": 0.25, "carb_por_g": 0.1},
        "salmao_fresco_grelhado": {"kcal_por_g": 2.0, "proteina_por_g": 0.2, "gordura_por_g": 0.13, "carb_por_g": 0.0},
        "brocolis": {"kcal_por_g": 0.25, "proteina_por_g": 0.03, "gordura_por_g": 0.0, "carb_por_g": 0.05},
        "abobrinha": {"kcal_por_g": 0.16, "proteina_por_g": 0.01, "gordura_por_g": 0.0, "carb_por_g": 0.03},
        "limao": {"kcal_por_g": 0.3, "proteina_por_g": 0.01, "gordura_por_g": 0.0, "carb_por_g": 0.09},
        "ervas_finas": {"kcal_por_g": 0.6, "proteina_por_g": 0.03, "gordura_por_g": 0.01, "carb_por_g": 0.1},
        "claras": {"kcal_por_g": 0.34, "proteina_por_g": 0.11, "gordura_por_g": 0.0, "carb_por_g": 0.0},
        "espinafre": {"kcal_por_g": 0.23, "proteina_por_g": 0.03, "gordura_por_g": 0.0, "carb_por_g": 0.04},
        "tomate_cereja": {"kcal_por_g": 0.17, "proteina_por_g": 0.01, "gordura_por_g": 0.0, "carb_por_g": 0.04},
        "tilapia": {"kcal_por_g": 1.2, "proteina_por_g": 0.26, "gordura_por_g": 0.02, "carb_por_g": 0.0},
        "cebola": {"kcal_por_g": 0.4, "proteina_por_g": 0.01, "gordura_por_g": 0.0, "carb_por_g": 0.09},
        "pimentao": {"kcal_por_g": 0.26, "proteina_por_g": 0.01, "gordura_por_g": 0.0, "carb_por_g": 0.06},
        "tortilha_integral": {"kcal_por_g": 2.6, "proteina_por_g": 0.08, "gordura_por_g": 0.05, "carb_por_g": 0.5},
        "frango_desfiado": {"kcal_por_g": 1.65, "proteina_por_g": 0.31, "gordura_por_g": 0.04, "carb_por_g": 0.0},
        "cream_cheese_light": {"kcal_por_g": 2.0, "proteina_por_g": 0.06, "gordura_por_g": 0.18, "carb_por_g": 0.03},
        "alface_americana": {"kcal_por_g": 0.13, "proteina_por_g": 0.01, "gordura_por_g": 0.0, "carb_por_g": 0.02},
        "tomate": {"kcal_por_g": 0.17, "proteina_por_g": 0.01, "gordura_por_g": 0.0, "carb_por_g": 0.04},
        "quinoa": {"kcal_por_g": 3.6, "proteina_por_g": 0.14, "gordura_por_g": 0.06, "carb_por_g": 0.64},
        "cogumelos_variados": {"kcal_por_g": 0.22, "proteina_por_g": 0.03, "gordura_por_g": 0.0, "carb_por_g": 0.03},
        "caldo_de_legumes": {"kcal_por_g": 0.05, "proteina_por_g": 0.0, "gordura_por_g": 0.0, "carb_por_g": 0.01},
        "queijo_parmesao": {"kcal_por_g": 4.0, "proteina_por_g": 0.35, "gordura_por_g": 0.28, "carb_por_g": 0.03},
        "banana_nanica": {"kcal_por_g": 0.9, "proteina_por_g": 0.01, "gordura_por_g": 0.0, "carb_por_g": 0.23},
        "leite_desnatado": {"kcal_por_g": 0.34, "proteina_por_g": 0.03, "gordura_por_g": 0.0, "carb_por_g": 0.05},
        "iogurte_grego_natural": {"kcal_por_g": 0.9, "proteina_por_g": 0.1, "gordura_por_g": 0.0, "carb_por_g": 0.07},
        "granola_caseira": {"kcal_por_g": 4.3, "proteina_por_g": 0.1, "gordura_por_g": 0.15, "carb_por_g": 0.6},
        "frutas_vermelhas": {"kcal_por_g": 0.4, "proteina_por_g": 0.01, "gordura_por_g": 0.0, "carb_por_g": 0.1},
        "pasta_de_amendoim": {"kcal_por_g": 6.2, "proteina_por_g": 0.25, "gordura_por_g": 0.5, "carb_por_g": 0.15},
        "agua_de_coco": {"kcal_por_g": 0.27, "proteina_por_g": 0.0, "gordura_por_g": 0.0, "carb_por_g": 0.06},
        "leite_condensado_diet": {"kcal_por_g": 2.0, "proteina_por_g": 0.05, "gordura_por_g": 0.05, "carb_por_g": 0.4},
        "coco_ralado": {"kcal_por_g": 6.6, "proteina_por_g": 0.07, "gordura_por_g": 0.65, "carb_por_g": 0.24},
        "aveia_em_flocos": {"kcal_por_g": 3.8, "proteina_por_g": 0.13, "gordura_por_g": 0.07, "carb_por_g": 0.66},
        "mel": {"kcal_por_g": 3.0, "proteina_por_g": 0.0, "gordura_por_g": 0.0, "carb_por_g": 0.8},
    }

def get_recipes():
    # Adicione todas as receitas de 'substituicoes_jantar_padrao(1).txt'
    # e 'substituicoes_lanche_padrao(1).txt' aqui, com seus macros detalhados.
    return {
        "hamburguer_artesanal": {
            "kcal": 780,
            "proteina_g": 42,
            "carb_g": 38,
            "gordura_g": 48,
            "itens": [
                {"item": "patinho_moido", "qtd": 120, "unidade": "g"},
                {"item": "pao_de_hamburguer_integral", "qtd": 1, "unidade": "un"},
                {"item": "queijo_mussarela", "qtd": 30, "unidade": "g"},
                {"item": "molho_especial", "qtd": 15, "unidade": "g"},
                {"item": "alface_americana", "qtd": 20, "unidade": "g"},
                {"item": "tomate", "qtd": 30, "unidade": "g"}
            ]
        },
        "pizza_fake_integral": {
            "kcal": 322,
            "proteina_g": 33,
            "carb_g": 28,
            "gordura_g": 10,
            "itens": [
                {"item": "pao_sirio_integral", "qtd": 1, "unidade": "un"},
                {"item": "molho_de_tomate", "qtd": 30, "unidade": "g"},
                {"item": "queijo_mussarela", "qtd": 40, "unidade": "g"},
                {"item": "peito_de_peru", "qtd": 50, "unidade": "g"}
            ]
        },
        "strogonoff_light_de_frango": {
            "kcal": 261,
            "proteina_g": 40,
            "carb_g": 10,
            "gordura_g": 7,
            "itens": [
                {"item": "file_de_frango_grelhado", "qtd": 120, "unidade": "g"},
                {"item": "champignon", "qtd": 50, "unidade": "g"},
                {"item": "creme_de_leite_light", "qtd": 30, "unidade": "g"},
                {"item": "mostarda", "qtd": 5, "unidade": "g"},
                {"item": "ketchup", "qtd": 10, "unidade": "g"}
            ]
        },
        "salmao_grelhado_com_legumes": {
            "kcal": 344,
            "proteina_g": 26,
            "carb_g": 10,
            "gordura_g": 24,
            "itens": [
                {"item": "salmao_fresco_grelhado", "qtd": 130, "unidade": "g"},
                {"item": "brocolis", "qtd": 100, "unidade": "g"},
                {"item": "abobrinha", "qtd": 80, "unidade": "g"},
                {"item": "azeite_extra_virgem", "qtd": 5, "unidade": "ml"},
                {"item": "limao", "qtd": 10, "unidade": "g"},
                {"item": "ervas_finas", "qtd": 5, "unidade": "g"}
            ]
        },
        "omelete_de_forno_recheada": {
            "kcal": 310,
            "proteina_g": 30,
            "carb_g": 5,
            "gordura_g": 20,
            "itens": [
                {"item": "ovo_de_galinha_inteiro", "qtd": 3, "unidade": "un"},
                {"item": "claras", "qtd": 2, "unidade": "un"},
                {"item": "queijo_cottage", "qtd": 50, "unidade": "g"},
                {"item": "espinafre", "qtd": 40, "unidade": "g"},
                {"item": "tomate_cereja", "qtd": 30, "unidade": "g"}
            ]
        },
        "peixe_assado_com_batata_doce": {
            "kcal": 311,
            "proteina_g": 36,
            "carb_g": 30,
            "gordura_g": 10,
            "itens": [
                {"item": "tilapia", "qtd": 140, "unidade": "g"},
                {"item": "batata_doce", "qtd": 100, "unidade": "g"},
                {"item": "cebola", "qtd": 30, "unidade": "g"},
                {"item": "pimentao", "qtd": 40, "unidade": "g"},
                {"item": "azeite_extra_virgem", "qtd": 5, "unidade": "ml"}
            ]
        },
        "wrap_de_frango_integral": {
            "kcal": 370,
            "proteina_g": 35,
            "carb_g": 30,
            "gordura_g": 12,
            "itens": [
                {"item": "tortilha_integral", "qtd": 1, "unidade": "un"},
                {"item": "frango_desfiado", "qtd": 100, "unidade": "g"},
                {"item": "cream_cheese_light", "qtd": 20, "unidade": "g"},
                {"item": "alface_americana", "qtd": 20, "unidade": "g"},
                {"item": "tomate", "qtd": 30, "unidade": "g"}
            ]
        },
        "risotto_de_quinoa_com_cogumelos": {
            "kcal": 344,
            "proteina_g": 18,
            "carb_g": 50,
            "gordura_g": 10,
            "itens": [
                {"item": "quinoa", "qtd": 60, "unidade": "g"},
                {"item": "cogumelos_variados", "qtd": 80, "unidade": "g"},
                {"item": "caldo_de_legumes", "qtd": 200, "unidade": "ml"},
                {"item": "queijo_parmesao", "qtd": 15, "unidade": "g"},
                {"item": "cebola", "qtd": 20, "unidade": "g"}
            ]
        },
        "panqueca_de_banana": {
            "kcal": 264,
            "proteina_g": 30,
            "carb_g": 25,
            "gordura_g": 7,
            "itens": [
                {"item": "banana_nanica", "qtd": 60, "unidade": "g"},
                {"item": "ovo_de_galinha_inteiro", "qtd": 1, "unidade": "un"},
                {"item": "whey_protein", "qtd": 35, "unidade": "g"}
            ]
        },
        "crepioca_proteica": {
            "kcal": 264,
            "proteina_g": 18,
            "carb_g": 30,
            "gordura_g": 10,
            "itens": [
                {"item": "tapioca_seca", "qtd": 30, "unidade": "g"},
                {"item": "ovo_de_galinha_inteiro", "qtd": 1, "unidade": "un"},
                {"item": "claras", "qtd": 2, "unidade": "un"},
                {"item": "requeijao_light", "qtd": 15, "unidade": "g"}
            ]
        },
        "vitamina_proteica": {
            "kcal": 262,
            "proteina_g": 30,
            "carb_g": 25,
            "gordura_g": 5,
            "itens": [
                {"item": "leite_desnatado", "qtd": 200, "unidade": "ml"},
                {"item": "whey_protein", "qtd": 35, "unidade": "g"},
                {"item": "banana_nanica", "qtd": 60, "unidade": "g"}
            ]
        },
        "iogurte_com_granola": {
            "kcal": 284,
            "proteina_g": 15,
            "carb_g": 40,
            "gordura_g": 10,
            "itens": [
                {"item": "iogurte_grego_natural", "qtd": 150, "unidade": "g"},
                {"item": "granola_caseira", "qtd": 30, "unidade": "g"},
                {"item": "frutas_vermelhas", "qtd": 50, "unidade": "g"}
            ]
        },
        "pao_integral_com_pasta": {
            "kcal": 300,
            "proteina_g": 15,
            "carb_g": 35,
            "gordura_g": 12,
            "itens": [
                {"item": "pao_de_forma_integral", "qtd": 2, "unidade": "fatia"},
                {"item": "pasta_de_amendoim", "qtd": 20, "unidade": "g"},
                {"item": "banana_nanica", "qtd": 40, "unidade": "g"}
            ]
        },
        "smoothie_verde": {
            "kcal": 254,
            "proteina_g": 30,
            "carb_g": 20,
            "gordura_g": 5,
            "itens": [
                {"item": "espinafre", "qtd": 30, "unidade": "g"},
                {"item": "abacaxi", "qtd": 80, "unidade": "g"},
                {"item": "whey_protein", "qtd": 35, "unidade": "g"},
                {"item": "agua_de_coco", "qtd": 150, "unidade": "ml"}
            ]
        },
        "tapioca_doce": {
            "kcal": 250,
            "proteina_g": 5,
            "carb_g": 50,
            "gordura_g": 5,
            "itens": [
                {"item": "tapioca_seca", "qtd": 40, "unidade": "g"},
                {"item": "leite_condensado_diet", "qtd": 20, "unidade": "g"},
                {"item": "coco_ralado", "qtd": 10, "unidade": "g"},
                {"item": "canela_em_po", "qtd": 2, "unidade": "g"}
            ]
        },
        "mingau_de_aveia": {
            "kcal": 238,
            "proteina_g": 10,
            "carb_g": 40,
            "gordura_g": 5,
            "itens": [
                {"item": "aveia_em_flocos", "qtd": 40, "unidade": "g"},
                {"item": "leite_desnatado", "qtd": 150, "unidade": "ml"},
                {"item": "mel", "qtd": 10, "unidade": "g"},
                {"item": "canela_em_po", "qtd": 2, "unidade": "g"}
            ]
        }
    }
