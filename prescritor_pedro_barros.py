
# prescritor_pedro_barros.py
# Prescrições manuais simulando as decisões do nutricionista Pedro Barros

def prescrever_cafe(paciente, metas):
    return [
        {"alimento": "Pão integral", "quantidade_g": 50, "categoria": "carbo"},
        {"alimento": "Ovo inteiro", "quantidade_g": 100, "categoria": "proteina"},
        {"alimento": "Requeijão light", "quantidade_g": 15, "categoria": "gordura"},
        {"alimento": "Banana", "quantidade_g": 80, "categoria": "fruta"}
    ]

def prescrever_almoco(paciente, metas):
    return [
        {"alimento": "Arroz integral cozido", "quantidade_g": 120, "categoria": "carbo"},
        {"alimento": "Feijão carioca cozido", "quantidade_g": 100, "categoria": "carbo"},
        {"alimento": "Frango grelhado", "quantidade_g": 120, "categoria": "proteina"},
        {"alimento": "Brócolis cozido", "quantidade_g": 50, "categoria": "vegetal"},
        {"alimento": "Azeite de oliva", "quantidade_g": 10, "categoria": "gordura"}
    ]

def prescrever_lanche(paciente, metas):
    return [
        {"alimento": "Iogurte natural desnatado", "quantidade_g": 150, "categoria": "proteina"},
        {"alimento": "Granola sem açúcar", "quantidade_g": 30, "categoria": "carbo"},
        {"alimento": "Frutas vermelhas", "quantidade_g": 100, "categoria": "fruta"}
    ]

def prescrever_jantar(paciente, metas):
    return prescrever_almoco(paciente, metas)

def prescrever_ceia(paciente, metas):
    return [
        {"alimento": "Iogurte grego natural", "quantidade_g": 150, "categoria": "proteina"},
        {"alimento": "Chia", "quantidade_g": 10, "categoria": "fibra"},
        {"alimento": "Maçã", "quantidade_g": 80, "categoria": "fruta"}
    ]

def gerar_substituicoes(refeicao):
    substituicoes = {
        "carbo": ["Pão integral", "Batata doce", "Tapioca", "Aveia"],
        "proteina": ["Frango", "Ovo", "Iogurte", "Patinho moído", "Tofu"],
        "gordura": ["Azeite", "Pasta de amendoim", "Requeijão light", "Abacate"],
        "fruta": ["Banana", "Maçã", "Mamão", "Frutas vermelhas"],
        "vegetal": ["Brócolis", "Cenoura", "Abobrinha", "Vagem"]
    }
    return substituicoes
