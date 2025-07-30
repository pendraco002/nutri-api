# ATENÇÃO: Esta é uma base de dados de exemplo.
# A tarefa principal é expandir massivamente esta base com todos os alimentos e receitas
# dos planos de exemplo para que o motor lógico funcione corretamente.

def get_food_data():
    """Retorna dados nutricionais por grama para alimentos básicos."""
    return {
        "frango_grelhado": {"kcal": 1.65, "p": 0.31, "c": 0, "g": 0.04},
        "arroz_branco_cozido": {"kcal": 1.3, "p": 0.025, "c": 0.28, "g": 0.002},
        "batata_doce_cozida": {"kcal": 0.86, "p": 0.016, "c": 0.2, "g": 0.001},
        "ovo_inteiro": {"kcal": 1.49, "p": 0.125, "c": 0.01, "g": 0.10}, # Média por 50g de ovo -> 1.49/g
        "whey_protein": {"kcal": 4.0, "p": 0.8, "c": 0.05, "g": 0.05}, # Exemplo genérico
        "pao_hamburguer": {"kcal": 2.8, "p": 0.09, "c": 0.52, "g": 0.04},
        "patinho_moido_cru": {"kcal": 1.33, "p": 0.21, "c": 0, "g": 0.05},
        "mussarela": {"kcal": 3.0, "p": 0.22, "c": 0.02, "g": 0.22},
        "iogurte_desnatado": {"kcal": 0.42, "p": 0.04, "c": 0.06, "g": 0},
        "mamao": {"kcal": 0.43, "p": 0.005, "c": 0.11, "g": 0.001},
        "chia": {"kcal": 4.86, "p": 0.17, "c": 0.42, "g": 0.31}
    }

def get_recipes():
    """Retorna templates de receitas (componentes modulares)."""
    db = get_food_data()
    
    # Exemplo de como calcular uma receita dinamicamente
    pao_g = 60
    carne_g = 120
    queijo_g = 30
    
    hamburguer_kcal = (db["pao_hamburguer"]["kcal"] * pao_g) + \
                      (db["patinho_moido_cru"]["kcal"] * carne_g) + \
                      (db["mussarela"]["kcal"] * queijo_g)
    
    return {
        "hamburguer_artesanal_v1": {
            "kcal": hamburguer_kcal,
            "itens": [
                {"item": "Pão de Hambúrguer", "qtd": pao_g, "unidade": "g"},
                {"item": "Carne de Patinho", "qtd": carne_g, "unidade": "g"},
                {"item": "Queijo Mussarela", "qtd": queijo_g, "unidade": "g"}
            ]
        },
        "panqueca_proteica_v1": {
            "kcal": 350, # Valor de exemplo
            "itens": [
                {"item": "Ovo de Galinha", "qtd": 1, "unidade": "un"},
                {"item": "Whey Protein", "qtd": 25, "unidade": "g"},
                {"item": "Banana", "qtd": 60, "unidade": "g"}
            ]
        }
    }
