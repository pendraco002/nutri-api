# Arquivo: planner.py (Versão Final)

from database import get_food_data, get_standard_recipes
from datetime import datetime
import random

def format_meal_items(items):
    """ Formata a lista de itens de uma refeição para texto. """
    text = ""
    for item in items:
        # Usamos tabs (\t) para tentar alinhar, mas o alinhamento perfeito depende da fonte.
        # O espaçamento é uma forma de garantir a separação visual.
        line = f"• {item['item']} ({item['unidade']}): {item['qtd']} {item['unidade']}\t\t\t[{item['kcal']} kcal]\n"
        text += line
    return text

def format_substitutions(sub_list):
    """ Formata a lista de substituições de uma refeição. """
    text = ""
    for i, sub in enumerate(sub_list):
        text += f"### Substituição {i+1} – {sub['nome']} ({sub['kcal']} kcal)\n"
        text += f"• {sub['itens']}\n\n"
    return text

def create_formatted_plan(objetivo, restricoes):
    """
    Cria o plano alimentar completo como uma única string de texto formatada,
    seguindo os padrões "Pedro Barros".
    """
    # Simulação de cálculo de metas - em um sistema real, isso seria mais complexo
    # e usaria os inputs 'objetivo' e 'restricoes'.
    metas = {"cafe": 450, "almoco": 700, "lanche": 350, "jantar": 600}
    
    # Pega os dados e receitas do nosso banco de dados
    db = get_food_data()
    recipes = get_standard_recipes()

    # --- Montagem do Plano Fixo (Exemplo) ---
    # Em um sistema real, os itens seriam selecionados dinamicamente.
    
    cafe_da_manha_itens = [
        {"item": "Ovos mexidos", "qtd": 3, "unidade": "unid", "kcal": 210},
        {"item": "Pão integral", "qtd": 2, "unidade": "fatias", "kcal": 140},
        {"item": "Abacate", "qtd": 50, "unidade": "g", "kcal": 80}
    ]

    almoco_itens = [
        {"item": "Filé de frango grelhado", "qtd": 150, "unidade": "g", "kcal": 248},
        {"item": "Arroz branco cozido", "qtd": 150, "unidade": "g", "kcal": 195},
        {"item": "Batata doce cozida", "qtd": 200, "unidade": "g", "kcal": 172}
    ]

    lanche_principal_itens = [
        {"item": "Iogurte Desnatado", "qtd": 200, "unidade": "g", "kcal": 110},
        {"item": "Banana", "qtd": 1, "unidade": "unid", "kcal": 90},
        {"item": "Whey Protein", "qtd": 30, "unidade": "g", "kcal": 120}
    ]

    jantar_principal_itens = [
        {"item": "Tilápia Grelhada", "qtd": 200, "unidade": "g", "kcal": 240},
        {"item": "Azeite Extra Virgem", "qtd": 10, "unidade": "g", "kcal": 88},
        {"item": "Legumes no vapor", "qtd": 200, "unidade": "g", "kcal": 50}
    ]

    ceia_fixa = recipes["ceia"]

    # Seleciona as substituições aleatoriamente (ou poderia ser uma lógica fixa)
    substituicoes_lanche = random.sample(recipes["lanche"], k=6)
    substituicoes_jantar = random.sample(recipes["jantar"], k=4)

    # --- Montagem da String Final ---
    data_atual = datetime.now().strftime("%d/%m/%Y")
    
    # Usamos f-strings para montar o texto final com a formatação exata.
    plano_formatado = f"""
Plano Alimentar
[NOME DO PACIENTE]
Data: {data_atual}

Todos os dias
Dieta única

---

## 🕗 08:00 – Café da Manhã ({metas['cafe']} kcal)
{format_meal_items(cafe_da_manha_itens)}
Obs:*Substituições:*
- Ovos por: 4 Claras de Ovo ou 100g de Tofu mexido.
- Pão integral por: 2 fatias de Pão sem glúten ou 60g de Tapioca.

---

## 🕛 12:30 – Almoço ({metas['almoco']} kcal)
{format_meal_items(almoco_itens)}
Obs:*Substituições:*
- **Proteína** por: Patinho Moído (150g), Tilápia (200g), Salmão (120g).
- **Carboidrato** por: Arroz Integral (150g), Mandioca (180g), Cuscuz (120g).
- **Leguminosa** por: Feijão (1 concha), Lentilha (100g), Grão de Bico (100g).
- ***Legumes Variados:*** Tomate, Chuchu, Abobrinha, Brócolis, Couve-Flor, etc.

---

## 🕓 16:00 – Lanche da Tarde ({metas['lanche']} kcal)
{format_meal_items(lanche_principal_itens)}

{format_substitutions(substituicoes_lanche)}
---

## 🕗 20:00 – Jantar ({metas['jantar']} kcal)
{format_meal_items(jantar_principal_itens)}

{format_substitutions(substituicoes_jantar)}
---

## 🌙 22:00 – Ceia ({ceia_fixa['kcal']} kcal)
{format_meal_items(ceia_fixa['itens'])}

---

> Este documento é de uso exclusivo do destinatário e pode ter conteúdo confidencial.
> Qualquer uso, cópia, divulgação ou distribuição não autorizada é estritamente proibido.
"""
    return plano_formatado
