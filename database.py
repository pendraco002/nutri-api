def get_food_data():
    return {
        "file_de_frango_grelhado": {
            "kcal_por_g": 1.65,
            "proteina_por_g": 0.31,
            "gordura_por_g": 0.04,
            "carb_por_g": 0.0
        },
        "arroz_branco_cozido": {
            "kcal_por_g": 1.3,
            "proteina_por_g": 0.025,
            "gordura_por_g": 0.002,
            "carb_por_g": 0.28
        },
        "azeite_extra_virgem": {
            "kcal_por_g": 8.8,
            "proteina_por_g": 0.0,
            "gordura_por_g": 1.0,
            "carb_por_g": 0.0
        }
    }

def get_recipes():
    return {
        "hamburguer_artesanal": {
            "kcal": 780,
            "proteina_g": 42,
            "carb_g": 38,
            "gordura_g": 48,
            "itens": [
                {"item": "Hambúrguer bovino", "qtd": 150, "unidade": "g", "kcal": 330},
                {"item": "Pão de hambúrguer", "qtd": 1, "unidade": "un", "kcal": 180},
                {"item": "Queijo muçarela", "qtd": 30, "unidade": "g", "kcal": 120},
                {"item": "Molho caseiro", "qtd": 20, "unidade": "g", "kcal": 50},
                {"item": "Alface e tomate", "qtd": 40, "unidade": "g", "kcal": 10},
                {"item": "Azeite extra virgem", "qtd": 10, "unidade": "g", "kcal": 90}
            ]
        }
    }
