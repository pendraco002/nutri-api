# Arquivo: planner.py (Versão Pedro Barros)

from database import get_pedro_barros_recipes
from datetime import datetime
import random

def format_meal_items(items):
    """ Formata os itens de uma refeição com alinhamento. """
    lines = []
    for item in items:
        # Cria a parte esquerda da linha
        left_part = f"• {item['item']} ({item['medida']}: {item['qtd']})"
        # Cria a parte direita da linha
        right_part = f"[{item['kcal']} kcal]"
        # Calcula o espaçamento necessário para o alinhamento
        # O número 110 é um valor ajustado para tentar alinhar bem em fontes monoespaçadas.
        # Pode precisar de ajuste dependendo da fonte de exibição.
        spacing = " " * (110 - len(left_part) - len(right_part))
        lines.append(f"{left_part}{spacing}{right_part}")
    return "\n".join(lines)

def format_substitutions(sub_list, type):
    """ Formata a lista de substituições. """
    text = ""
    if type == "lanche":
        for i, sub in enumerate(sub_list):
            total_kcal = sum(item['kcal'] for item in sub['itens'])
            text += f"### Substituição {i+1}{' ' * 95}Kcal\n"
            text += f"{format_meal_items(sub['itens'])}\n"
            if sub.get('obs'):
                text += f"Obs: {sub['obs']}\n"
            text += "\n"
    elif type == "jantar":
        for i, sub in enumerate(sub_list):
            total_kcal = sum(item['kcal'] for item in sub['itens'])
            text += f"### Substituição {i+1} – {sub['nome']}{' ' * (80 - len(sub['nome']))}Kcal\n"
            text += f"{format_meal_items(sub['itens'])}\n\n"
    return text

def create_pedro_barros_plan(user_name="[NOME COMPLETO DO PACIENTE]"):
    """
    Gera o plano alimentar completo no formato exato de Pedro Barros.
    """
    recipes = get_pedro_barros_recipes()
    data_atual = datetime.now().strftime("%d/%m/%Y")

    # --- Simulação de um plano principal ---
    # Em um sistema real, estes itens seriam calculados dinamicamente.
    cafe_da_manha = {"kcal": 450, "itens": [{"item": "Ovo de galinha", "medida": "Unidade", "qtd": 2, "kcal": 140}, {"item": "Pão de forma", "medida": "Fatia", "qtd": 2, "kcal": 140}, {"item": "Requeijão Light", "medida": "Grama", "qtd": 30, "kcal": 54}, {"item": "Mamão", "medida": "Grama", "qtd": 150, "kcal": 58}]}
    almoco = {"kcal": 600, "itens": [{"item": "Filé de frango grelhado", "medida": "Grama", "qtd": 150, "kcal": 248}, {"item": "Arroz branco (cozido)", "medida": "Grama", "qtd": 120, "kcal": 156}, {"item": "Feijão cozido", "medida": "Concha", "qtd": 1, "kcal": 52}, {"item": "Legumes Variados", "medida": "Grama", "qtd": 150, "kcal": 38}]}
    lanche_principal = {"kcal": 300, "itens": [{"item": "Iogurte Desnatado", "medida": "Grama", "qtd": 170, "kcal": 94}, {"item": "Whey Protein", "medida": "Grama", "qtd": 30, "kcal": 120}, {"item": "Banana", "medida": "Unidade", "qtd": 1, "kcal": 90}], "obs": "Misturar o whey no iogurte."}
    jantar_principal = {"kcal": 500, "itens": [{"item": "Tilápia Grelhada", "medida": "Grama", "qtd": 200, "kcal": 240}, {"item": "Batata Doce Cozida", "medida": "Grama", "qtd": 200, "kcal": 172}, {"item": "Azeite Extra Virgem", "medida": "Grama", "qtd": 10, "kcal": 88}]}
    ceia = recipes["ceia"]

    # Seleciona as 6 substituições de lanche e 4 de jantar
    substituicoes_lanche = random.sample(recipes["lanche"], k=6)
    substituicoes_jantar = random.sample(recipes["jantar"], k=4)

    # --- Montagem da String Final ---
    plano_formatado = f"""
                                                           Plano Alimentar
                                                    {user_name}
                                                         Data: {data_atual}



Todos os dias  
Dieta única

---

## 🕗 08:00 – Café da manhã{' ' * 95}Kcal
{format_meal_items(cafe_da_manha['itens'])}
Obs:*Substituições:*
- Pão de forma por: 40g de tapioca ou 2 biscoitos de arroz grandes ou 30g de aveia.
- Requeijão Light por: Queijo minas ou cottage ou 25g de mussarela.

---

## 🕛 12:00 – Almoço{' ' * 102}Kcal
{format_meal_items(almoco['itens'])}
Obs:*Substituições:*  
- Proteína por: Carne Vermelha Magra (120g) ou Peixe Branco (180g) ou Ovos (3 unidades).
- Carboidrato por: Batata Inglesa (250g) ou Mandioca (150g) ou Macarrão (120g).
- Feijão por: Lentilha ou grão de bico ou ervilha.
- Legumes Variados: Tomate, Chuchu, Abobrinha, Brócolis, etc.  

---

## 🕓 16:00 – Lanche da Tarde{' ' * 92}Kcal
{format_meal_items(lanche_principal['itens'])}
Obs: {lanche_principal['obs']}

---

{format_substitutions(substituicoes_lanche, "lanche")}
---

## 🕗 20:00 – Jantar{' ' * 105}Kcal
{format_meal_items(jantar_principal['itens'])}
Obs:*Substituições:*  
- Proteína por: Carne Vermelha Magra (150g) ou Salmão (120g) ou Frango (180g).
- Carboidrato por: Arroz (100g) ou Mandioca (200g) ou Inhame (200g).
- Legumes Variados: Tomate, Chuchu, Abobrinha, Brócolis, etc.  

---

{format_substitutions(substituicoes_jantar, "jantar")}
---

## 🌙 22:00 – Ceia{' ' * 109}Kcal
{format_meal_items(ceia['itens'])}

---

> Este documento é de uso exclusivo do destinatário e pode ter conteúdo confidencial.  
> Qualquer uso, cópia, divulgação ou distribuição não autorizada é estritamente proibido.
"""
    return plano_formatado
