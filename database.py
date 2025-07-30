def get_food_data():
    """Base de dados nutricional completa - Método Pedro Barros"""
    return {
        # PROTEÍNAS - Base: Frango 100g = 184 kcal
        "file_de_frango_grelhado": {
            "kcal_por_g": 1.84,
            "proteina_por_g": 0.31,
            "gordura_por_g": 0.04,
            "carb_por_g": 0.0
        },
        "patinho_magro": {
            "kcal_por_g": 2.04,
            "proteina_por_g": 0.29,
            "gordura_por_g": 0.09,
            "carb_por_g": 0.0
        },
        "alcatra": {
            "kcal_por_g": 1.98,
            "proteina_por_g": 0.28,
            "gordura_por_g": 0.09,
            "carb_por_g": 0.0
        },
        "file_mignon": {
            "kcal_por_g": 2.04,
            "proteina_por_g": 0.29,
            "gordura_por_g": 0.09,
            "carb_por_g": 0.0
        },
        "file_suino": {
            "kcal_por_g": 2.12,
            "proteina_por_g": 0.27,
            "gordura_por_g": 0.11,
            "carb_por_g": 0.0
        },
        "salmao_fresco": {
            "kcal_por_g": 2.06,
            "proteina_por_g": 0.22,
            "gordura_por_g": 0.13,
            "carb_por_g": 0.0
        },
        "atum_fresco": {
            "kcal_por_g": 1.67,
            "proteina_por_g": 0.29,
            "gordura_por_g": 0.05,
            "carb_por_g": 0.0
        },
        "peixe_branco": {
            "kcal_por_g": 1.50,
            "proteina_por_g": 0.28,
            "gordura_por_g": 0.04,
            "carb_por_g": 0.0
        },
        "camarao": {
            "kcal_por_g": 1.40,
            "proteina_por_g": 0.27,
            "gordura_por_g": 0.03,
            "carb_por_g": 0.0
        },
        "ovo_inteiro": {
            "kcal_por_g": 1.40,
            "proteina_por_g": 0.12,
            "gordura_por_g": 0.10,
            "carb_por_g": 0.01
        },
        "clara_de_ovo": {
            "kcal_por_g": 0.52,
            "proteina_por_g": 0.11,
            "gordura_por_g": 0.0,
            "carb_por_g": 0.01
        },
        
        # CARBOIDRATOS - Base: Arroz 50g = 62 kcal
        "arroz_branco_cozido": {
            "kcal_por_g": 1.24,
            "proteina_por_g": 0.025,
            "gordura_por_g": 0.003,
            "carb_por_g": 0.28
        },
        "batata_inglesa": {
            "kcal_por_g": 0.87,
            "proteina_por_g": 0.02,
            "gordura_por_g": 0.001,
            "carb_por_g": 0.20
        },
        "batata_doce": {
            "kcal_por_g": 0.86,
            "proteina_por_g": 0.016,
            "gordura_por_g": 0.001,
            "carb_por_g": 0.20
        },
        "macarrao_cozido": {
            "kcal_por_g": 1.40,
            "proteina_por_g": 0.05,
            "gordura_por_g": 0.009,
            "carb_por_g": 0.28
        },
        "aipim_mandioca": {
            "kcal_por_g": 1.60,
            "proteina_por_g": 0.014,
            "gordura_por_g": 0.003,
            "carb_por_g": 0.38
        },
        "inhame": {
            "kcal_por_g": 1.17,
            "proteina_por_g": 0.015,
            "gordura_por_g": 0.002,
            "carb_por_g": 0.28
        },
        "cuscuz": {
            "kcal_por_g": 1.12,
            "proteina_por_g": 0.037,
            "gordura_por_g": 0.002,
            "carb_por_g": 0.23
        },
        "tapioca_seca": {
            "kcal_por_g": 3.40,
            "proteina_por_g": 0.005,
            "gordura_por_g": 0.002,
            "carb_por_g": 0.85
        },
        "pao_frances": {
            "kcal_por_g": 2.86,
            "proteina_por_g": 0.10,
            "gordura_por_g": 0.04,
            "carb_por_g": 0.55
        },
        "pao_forma_integral": {
            "kcal_por_g": 2.50,
            "proteina_por_g": 0.09,
            "gordura_por_g": 0.03,
            "carb_por_g": 0.48
        },
        
        # GORDURAS
        "azeite_extra_virgem": {
            "kcal_por_g": 8.8,
            "proteina_por_g": 0.0,
            "gordura_por_g": 1.0,
            "carb_por_g": 0.0
        },
        "pasta_amendoim": {
            "kcal_por_g": 5.88,
            "proteina_por_g": 0.25,
            "gordura_por_g": 0.50,
            "carb_por_g": 0.20
        },
        
        # LATICÍNIOS
        "iogurte_natural_desnatado": {
            "kcal_por_g": 0.55,
            "proteina_por_g": 0.04,
            "gordura_por_g": 0.001,
            "carb_por_g": 0.08
        },
        "queijo_cottage": {
            "kcal_por_g": 0.65,
            "proteina_por_g": 0.11,
            "gordura_por_g": 0.01,
            "carb_por_g": 0.04
        },
        "queijo_minas_frescal": {
            "kcal_por_g": 1.08,
            "proteina_por_g": 0.14,
            "gordura_por_g": 0.05,
            "carb_por_g": 0.03
        },
        "requeijao_light": {
            "kcal_por_g": 1.88,
            "proteina_por_g": 0.10,
            "gordura_por_g": 0.15,
            "carb_por_g": 0.03
        },
        "queijo_mussarela": {
            "kcal_por_g": 2.80,
            "proteina_por_g": 0.22,
            "gordura_por_g": 0.20,
            "carb_por_g": 0.03
        },
        
        # LEGUMINOSAS
        "feijao_cozido": {
            "kcal_por_g": 0.61,
            "proteina_por_g": 0.04,
            "gordura_por_g": 0.003,
            "carb_por_g": 0.11
        },
        "lentilha_cozida": {
            "kcal_por_g": 0.70,
            "proteina_por_g": 0.09,
            "gordura_por_g": 0.004,
            "carb_por_g": 0.12
        },
        "grao_de_bico_cozido": {
            "kcal_por_g": 0.72,
            "proteina_por_g": 0.08,
            "gordura_por_g": 0.03,
            "carb_por_g": 0.12
        },
        
        # SUPLEMENTOS
        "whey_protein": {
            "kcal_por_g": 4.06,
            "proteina_por_g": 0.80,
            "gordura_por_g": 0.05,
            "carb_por_g": 0.10
        },
        
        # FIBRAS E TEMPEROS
        "chia": {
            "kcal_por_g": 3.80,
            "proteina_por_g": 0.17,
            "gordura_por_g": 0.31,
            "carb_por_g": 0.08
        },
        "psyllium": {
            "kcal_por_g": 0.80,
            "proteina_por_g": 0.01,
            "gordura_por_g": 0.01,
            "carb_por_g": 0.85
        },
        "cacau_po": {
            "kcal_por_g": 2.80,
            "proteina_por_g": 0.20,
            "gordura_por_g": 0.14,
            "carb_por_g": 0.35
        },
        "canela_po": {
            "kcal_por_g": 2.61,
            "proteina_por_g": 0.04,
            "gordura_por_g": 0.01,
            "carb_por_g": 0.54
        },
        
        # VEGETAIS (média)
        "legumes_variados": {
            "kcal_por_g": 0.25,
            "proteina_por_g": 0.02,
            "gordura_por_g": 0.002,
            "carb_por_g": 0.05
        },
        "salada_verde": {
            "kcal_por_g": 0.18,
            "proteina_por_g": 0.015,
            "gordura_por_g": 0.002,
            "carb_por_g": 0.03
        },
        
        # FRUTAS
        "banana": {
            "kcal_por_g": 0.92,
            "proteina_por_g": 0.01,
            "gordura_por_g": 0.003,
            "carb_por_g": 0.23
        },
        "mamao": {
            "kcal_por_g": 0.39,
            "proteina_por_g": 0.005,
            "gordura_por_g": 0.001,
            "carb_por_g": 0.10
        },
        "frutas_gerais": {
            "kcal_por_g": 0.48,
            "proteina_por_g": 0.008,
            "gordura_por_g": 0.003,
            "carb_por_g": 0.12
        }
    }

def get_recipes():
    """Receitas padrão do método Pedro Barros"""
    return {
        # HAMBÚRGUER ARTESANAL (PADRÃO)
        "hamburguer_artesanal": {
            "nome": "Hambúrguer Artesanal Completo",
            "kcal": 536,
            "proteina_g": 35,
            "carb_g": 52,
            "gordura_g": 18,
            "itens": [
                {"item": "Pão de hambúrguer", "qtd": 1, "unidade": "unidade", "kcal": 180},
                {"item": "Patinho moído", "qtd": 120, "unidade": "g", "kcal": 245},
                {"item": "Queijo mussarela", "qtd": 30, "unidade": "g", "kcal": 84},
                {"item": "Molho especial", "qtd": 15, "unidade": "g", "kcal": 22},
                {"item": "Alface e tomate", "qtd": 40, "unidade": "g", "kcal": 5}
            ]
        },
        
        # STROGONOFF LIGHT
        "strogonoff_light": {
            "nome": "Strogonoff Light de Frango",
            "kcal": 374,
            "proteina_g": 38,
            "carb_g": 24,
            "gordura_g": 12,
            "itens": [
                {"item": "Filé-mignon", "qtd": 100, "unidade": "g", "kcal": 204},
                {"item": "Ketchup", "qtd": 10, "unidade": "g", "kcal": 10},
                {"item": "Mostarda", "qtd": 10, "unidade": "g", "kcal": 8},
                {"item": "Arroz branco (cozido)", "qtd": 75, "unidade": "g", "kcal": 94},
                {"item": "Champignon", "qtd": 50, "unidade": "g", "kcal": 12},
                {"item": "Creme de Leite Light", "qtd": 40, "unidade": "g", "kcal": 46}
            ]
        },
        
        # PANQUECA PROTEICA (LANCHE PADRÃO)
        "panqueca_proteica": {
            "nome": "Panqueca de Banana com Whey",
            "kcal": 247,
            "proteina_g": 27,
            "carb_g": 25,
            "gordura_g": 5,
            "itens": [
                {"item": "Banana", "qtd": 60, "unidade": "g", "kcal": 55},
                {"item": "Ovo inteiro", "qtd": 1, "unidade": "unidade", "kcal": 70},
                {"item": "Whey Protein", "qtd": 20, "unidade": "g", "kcal": 81},
                {"item": "Cacau em Pó 100%", "qtd": 10, "unidade": "g", "kcal": 28},
                {"item": "Canela em pó", "qtd": 5, "unidade": "g", "kcal": 13}
            ]
        },
        
        # CREPIOCA
        "crepioca": {
            "nome": "Crepioca Proteica",
            "kcal": 210,
            "proteina_g": 19,
            "carb_g": 18,
            "gordura_g": 6,
            "itens": [
                {"item": "Tapioca seca", "qtd": 20, "unidade": "g", "kcal": 68},
                {"item": "Ovo inteiro", "qtd": 1, "unidade": "unidade", "kcal": 70},
                {"item": "Clara de ovo", "qtd": 2, "unidade": "unidade", "kcal": 34},
                {"item": "Requeijão Light", "qtd": 20, "unidade": "g", "kcal": 38}
            ]
        }
    }

def get_meal_templates():
    """Templates de refeições padrão"""
    return {
        # LANCHES PADRÃO (6 opções)
        "lanches_padrao": [
            {
                "nome": "Panqueca de Banana",
                "kcal": 264,
                "proteina_g": 29,
                "carb_g": 26,
                "gordura_g": 5
            },
            {
                "nome": "Crepioca Proteica",
                "kcal": 264,
                "proteina_g": 23,
                "carb_g": 20,
                "gordura_g": 8
            },
            {
                "nome": "Vitamina Proteica",
                "kcal": 262,
                "proteina_g": 30,
                "carb_g": 28,
                "gordura_g": 3
            },
            {
                "nome": "Iogurte com Granola",
                "kcal": 284,
                "proteina_g": 12,
                "carb_g": 35,
                "gordura_g": 10
            },
            {
                "nome": "Pão Integral com Pasta",
                "kcal": 300,
                "proteina_g": 14,
                "carb_g": 34,
                "gordura_g": 12
            },
            {
                "nome": "Shake Proteico Pronto",
                "kcal": 165,
                "proteina_g": 25,
                "carb_g": 12,
                "gordura_g": 2
            }
        ],
        
        # JANTARES PADRÃO (4 opções principais)
        "jantares_padrao": [
            {
                "nome": "Pizza Fake Integral",
                "kcal": 372,
                "proteina_g": 35,
                "carb_g": 38,
                "gordura_g": 10
            },
            {
                "nome": "Strogonoff Light de Frango",
                "kcal": 271,
                "proteina_g": 32,
                "carb_g": 21,
                "gordura_g": 8
            },
            {
                "nome": "Hambúrguer Artesanal Completo",
                "kcal": 536,
                "proteina_g": 35,
                "carb_g": 52,
                "gordura_g": 18
            },
            {
                "nome": "Salmão Grelhado com Legumes",
                "kcal": 346,
                "proteina_g": 38,
                "carb_g": 8,
                "gordura_g": 18
            }
        ],
        
        # CEIA PADRÃO (sempre fixa)
        "ceia_padrao": {
            "nome": "Ceia Padrão",
            "componentes": [
                "Whey Protein (15-35g)",
                "Iogurte natural (100-150g)",
                "Fruta (exceto banana/abacate) (75-100g)",
                "Fibra: Chia ou psyllium (5-10g)"
            ]
        }
    }

def get_substitution_rules():
    """Regras de substituição do método Pedro Barros"""
    return {
        "proteinas": {
            "base": "file_de_frango_grelhado",
            "substitutos": [
                "Carne Vermelha Magra (patinho, acém, alcatra, filé mignon)",
                "Filé Suíno (pernil, mignon, lombo)",
                "Salmão ou Atum Fresco",
                "Peixe Branco",
                "Camarão Cozido"
            ]
        },
        "carboidratos": {
            "base": "arroz_branco_cozido",
            "equivalencias": {
                "100g arroz": [
                    "200g batata inglesa",
                    "140g batata doce",
                    "100g aipim",
                    "100g macarrão",
                    "100g inhame"
                ]
            }
        },
        "leguminosas": {
            "base": "feijao_cozido",
            "substitutos": [
                "Lentilha",
                "Grão de bico",
                "Ervilha",
                "Milho cozido"
            ]
        },
        "legumes_variados": [
            "Tomate", "Beringela", "Alho Poró", "Maxixe", "Brócolis",
            "Rabanete", "Chuchu", "Couve", "Beterraba", "Pepino",
            "Couve Flor", "Abobrinha", "Repolho", "Palmito", "Quiabo",
            "Cenoura", "Vagem", "Jiló"
        ]
    }
