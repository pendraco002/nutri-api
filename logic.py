
import re
from typing import Dict, Any

def gerar_plano_personalizado(dados: Dict[str, Any]) -> Dict[str, Any]:
    paciente = dados.get("paciente", {})
    metas = dados.get("metas", {})
    configuracoes = dados.get("configuracoes", {})

    nome = paciente.get("nome", "Paciente")
    peso = paciente.get("peso_kg", 0)
    altura = paciente.get("altura_cm", 0)
    sexo = paciente.get("sexo", "N")

    kcal_total = metas.get("kcal_total", 0)
    proteina_min = metas.get("proteina_min_g_por_kg", 0) * peso
    carbo_max_percent = metas.get("carboidrato_max_percent", 0)
    gordura_max_percent = metas.get("gordura_max_percent", 0)
    fibras_min = metas.get("fibras_min_g", 0)

    num_refeicoes = configuracoes.get("num_refeicoes", 5)
    pre_treino = configuracoes.get("pre_treino", {})
    preferencias = configuracoes.get("preferencias", {})

    plano_formatado = (
        f"Plano alimentar para {nome}:\n"
        f"- Peso: {peso} kg\n"
        f"- Altura: {altura} cm\n"
        f"- Calorias totais: {kcal_total} kcal\n"
        f"- Refeições por dia: {num_refeicoes}\n"
    )

    refeicoes = [
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
        },
        {
            "nome": "Jantar",
            "alimentos": [
                {"alimento": "Tilápia", "quantidade_g": 150},
                {"alimento": "Batata Doce", "quantidade_g": 100}
            ],
            "substituicoes": {
                "Tilápia": ["Frango", "Tofu"],
                "Batata Doce": ["Arroz", "Inhame"]
            }
        }
    ]

    if preferencias.get("hamburguer_jantar"):
        refeicoes.append({
            "nome": "Receita Especial - Hambúrguer Artesanal",
            "alimentos": [
                {"alimento": "Pão de hambúrguer", "quantidade_g": 70},
                {"alimento": "Hambúrguer de patinho", "quantidade_g": 120},
                {"alimento": "Queijo mussarela", "quantidade_g": 30}
            ]
        })

    if preferencias.get("sobremesa_final"):
        refeicoes.append({
            "nome": "Sobremesa",
            "alimentos": [
                {"alimento": "Iogurte natural", "quantidade_g": 100},
                {"alimento": "Frutas", "quantidade_g": 75},
                {"alimento": "Whey", "quantidade_g": 20}
            ]
        })

    return {
        "plano_formatado": plano_formatado,
        "refeicoes": refeicoes,
        "resumo_nutricional": {
            "calorias": kcal_total,
            "proteina_minima": round(proteina_min, 2),
            "carboidrato_max_percent": carbo_max_percent,
            "gordura_max_percent": gordura_max_percent,
            "fibras_min_g": fibras_min
        }
    }
