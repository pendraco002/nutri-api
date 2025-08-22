# logic.py

def gerar_plano_personalizado(dados):
    """
    Função simulada que retorna um plano nutricional formatado,
    um resumo nutricional e uma estrutura de substituições.
    """

    paciente = dados["paciente"]
    metas = dados["metas"]
    config = dados["configuracoes"]

    # Aqui você pode usar lógica real de geração de plano (isto é só simulação)
    plano_formatado = f"""
    Plano alimentar para {paciente['nome']}:
    - Peso: {paciente['peso_kg']} kg
    - Altura: {paciente['altura_cm']} cm
    - Calorias totais: {metas['kcal_total']} kcal
    - Refeições por dia: {config['num_refeicoes']}
    """

    resumo_nutricional = {
        "calorias": metas["kcal_total"],
        "proteina_minima": metas["proteina_min_g_por_kg"] * paciente["peso_kg"],
        "carboidrato_max_percent": metas["carboidrato_max_percent"],
        "gordura_max_percent": metas["gordura_max_percent"],
        "fibras_min_g": metas["fibras_min_g"]
    }

    substituicoes = [
        {
            "nome": "Café da Manhã",
            "alimentos": [
                {"alimento": "Ovos", "quantidade_g": 100},
                {"alimento": "Aveia", "quantidade_g": 50}
            ],
            "substituicoes": {
                "Ovos": ["Tofu", "Frango desfiado"],
                "Aveia": ["Pão integral", "Batata doce"]
            }
        },
        {
            "nome": "Almoço",
            "alimentos": [
                {"alimento": "Arroz", "quantidade_g": 100},
                {"alimento": "Frango", "quantidade_g": 150}
            ],
            "substituicoes": {
                "Arroz": ["Quinoa", "Macarrão integral"],
                "Frango": ["Peixe", "Carne magra"]
            }
        }
    ]

    return plano_formatado, resumo_nutricional, substituicoes
