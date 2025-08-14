# -*- coding: utf-8 -*-
"""
Módulo de Lógica e Dados para o Sistema de Nutrição.

Este arquivo centraliza toda a informação e a lógica de negócio necessárias
para a geração de planos alimentares.

Arquitetura:
1.  **Dados e Lógica Unificados:** Contém as bases de dados de alimentos, a
    biblioteca de componentes de refeição e a função principal que gera
    os planos.
2.  **Precisão Numérica:** Utiliza `Decimal` para todos os valores nutricionais
    para evitar erros de arredondamento de ponto flutuante.
3.  **Função Geradora (`generate_complete_meal_plan`):** Orquestra a seleção
    de refeições, a formatação da saída e a criação do objeto de resposta
    final, incluindo um plano formatado em Markdown para fácil exibição.
"""
import random
from uuid import uuid4
from datetime import date
from decimal import Decimal, getcontext
from typing import Dict, List, TypedDict

# Define a precisão global para todos os cálculos decimais.
getcontext().prec = 10

# -----------------------------------------------------------------------------
# SEÇÃO 1: ESTRUTURAS DE DADOS TIPADAS (DATA SCHEMAS)
# -----------------------------------------------------------------------------
class NutrientInfo(TypedDict):
    p: Decimal
    c: Decimal
    g: Decimal

class FoodItem(TypedDict):
    name: str
    kcal: Decimal
    nutrients: NutrientInfo

class Ingredient(TypedDict):
    food_id: str
    base_grams: Decimal

class MealComponent(TypedDict):
    name: str
    category: str
    ingredients: List[Ingredient]

# -----------------------------------------------------------------------------
# SEÇÃO 2: BASE DE DADOS NUTRICIONAL (`NUTRITIONAL_DATABASE`)
# -----------------------------------------------------------------------------
NUTRITIONAL_DATABASE: Dict[str, FoodItem] = {
    'ovo_inteiro': {'name': "Ovo Inteiro", 'kcal': Decimal('155'), 'nutrients': {'p': Decimal('13.0'), 'c': Decimal('1.1'), 'g': Decimal('11.0')}},
    'clara_de_ovo': {'name': "Clara de Ovo", 'kcal': Decimal('52'), 'nutrients': {'p': Decimal('11.0'), 'c': Decimal('0.7'), 'g': Decimal('0.2')}},
    'whey_isolado': {'name': "Whey Protein Isolado", 'kcal': Decimal('370'), 'nutrients': {'p': Decimal('85.0'), 'c': Decimal('4.0'), 'g': Decimal('1.0')}},
    'aveia_em_flocos': {'name': "Aveia em Flocos", 'kcal': Decimal('389'), 'nutrients': {'p': Decimal('16.9'), 'c': Decimal('66.3'), 'g': Decimal('6.9')}},
    'banana_prata': {'name': "Banana Prata", 'kcal': Decimal('89'), 'nutrients': {'p': Decimal('1.3'), 'c': Decimal('23.0'), 'g': Decimal('0.3')}},
    'peito_de_frango_grelhado': {'name': "Peito de Frango Grelhado", 'kcal': Decimal('165'), 'nutrients': {'p': Decimal('31.0'), 'c': Decimal('0.0'), 'g': Decimal('3.6')}},
    'arroz_branco_cozido': {'name': "Arroz Branco Cozido", 'kcal': Decimal('130'), 'nutrients': {'p': Decimal('2.7'), 'c': Decimal('28.0'), 'g': Decimal('0.3')}},
    'feijao_preto_cozido': {'name': "Feijão Preto Cozido", 'kcal': Decimal('131'), 'nutrients': {'p': Decimal('8.9'), 'c': Decimal('23.7'), 'g': Decimal('0.5')}},
    'pao_de_forma_integral': {'name': "Pão de Forma Integral", 'kcal': Decimal('246'), 'nutrients': {'p': Decimal('13.0'), 'c': Decimal('41.0'), 'g': Decimal('3.4')}},
    'queijo_mussarela_light': {'name': "Queijo Mussarela Light", 'kcal': Decimal('254'), 'nutrients': {'p': Decimal('24.0'), 'c': Decimal('1.0'), 'g': Decimal('16.0')}},
    'tomate': {'name': "Tomate", 'kcal': Decimal('18'), 'nutrients': {'p': Decimal('0.9'), 'c': Decimal('3.9'), 'g': Decimal('0.2')}},
    'leite_desnatado': {'name': "Leite Desnatado", 'kcal': Decimal('35'), 'nutrients': {'p': Decimal('3.4'), 'c': Decimal('5.0'), 'g': Decimal('0.1')}},
    'carne_moida_patinho': {'name': "Carne Moída (Patinho)", 'kcal': Decimal('219'), 'nutrients': {'p': Decimal('28.0'), 'c': Decimal('0.0'), 'g': Decimal('11.0')}},
    'batata_doce_cozida': {'name': "Batata Doce Cozida", 'kcal': Decimal('86'), 'nutrients': {'p': Decimal('1.6'), 'c': Decimal('20.1'), 'g': Decimal('0.1')}},
    'tilapia_grelhada': {'name': "Filé de Tilápia Grelhado", 'kcal': Decimal('128'), 'nutrients': {'p': Decimal('26.0'), 'c': Decimal('0.0'), 'g': Decimal('2.6')}},
    'massa_de_rap10': {'name': "Massa de Rap10 Integral", 'kcal': Decimal('298'), 'nutrients': {'p': Decimal('9.1'), 'c': Decimal('57.0'), 'g': Decimal('3.5')}},
    'requeijao_light': {'name': "Requeijão Light", 'kcal': Decimal('173'), 'nutrients': {'p': Decimal('11.0'), 'c': Decimal('3.3'), 'g': Decimal('12.0')}},
}

# -----------------------------------------------------------------------------
# SEÇÃO 3: BIBLIOTECA DE COMPONENTES DE REFEIÇÃO (`MEAL_COMPONENT_LIBRARY`)
# -----------------------------------------------------------------------------
MEAL_COMPONENT_LIBRARY: Dict[str, MealComponent] = {
    'lanche_panqueca_banana': {'name': "Panqueca de Banana e Aveia", 'category': 'panqueca', 'ingredients': [{'food_id': 'ovo_inteiro', 'base_grams': Decimal('100')}, {'food_id': 'aveia_em_flocos', 'base_grams': Decimal('30')}, {'food_id': 'banana_prata', 'base_grams': Decimal('50')}]},
    'lanche_shake_proteico': {'name': "Shake Proteico com Frutas", 'category': 'shake', 'ingredients': [{'food_id': 'whey_isolado', 'base_grams': Decimal('30')}, {'food_id': 'banana_prata', 'base_grams': Decimal('100')}, {'food_id': 'leite_desnatado', 'base_grams': Decimal('200')}]},
    'lanche_crepioca': {'name': "Crepioca com Queijo", 'category': 'crepioca', 'ingredients': [{'food_id': 'ovo_inteiro', 'base_grams': Decimal('50')}, {'food_id': 'clara_de_ovo', 'base_grams': Decimal('60')}, {'food_id': 'queijo_mussarela_light', 'base_grams': Decimal('30')}]},
    'lanche_sanduiche_frango': {'name': "Sanduíche de Frango", 'category': 'sanduiche', 'ingredients': [{'food_id': 'pao_de_forma_integral', 'base_grams': Decimal('50')}, {'food_id': 'peito_de_frango_grelhado', 'base_grams': Decimal('100')}, {'food_id': 'requeijao_light', 'base_grams': Decimal('20')}]},
    'refeicao_frango_arroz': {'name': "Frango com Arroz e Feijão", 'category': 'refeicao_solida', 'ingredients': [{'food_id': 'peito_de_frango_grelhado', 'base_grams': Decimal('150')}, {'food_id': 'arroz_branco_cozido', 'base_grams': Decimal('100')}, {'food_id': 'feijao_preto_cozido', 'base_grams': Decimal('80')}]},
    'refeicao_carne_batata_doce': {'name': "Carne Moída com Batata Doce", 'category': 'refeicao_solida', 'ingredients': [{'food_id': 'carne_moida_patinho', 'base_grams': Decimal('150')}, {'food_id': 'batata_doce_cozida', 'base_grams': Decimal('150')}]},
    'refeicao_tilapia_legumes': {'name': "Tilápia com Legumes", 'category': 'refeicao_solida', 'ingredients': [{'food_id': 'tilapia_grelhada', 'base_grams': Decimal('180')}, {'food_id': 'tomate', 'base_grams': Decimal('100')}]},
    'jantar_pizza_fake': {'name': "Pizza Fake de Frango", 'category': 'jantar_especial', 'ingredients': [{'food_id': 'massa_de_rap10', 'base_grams': Decimal('40')}, {'food_id': 'peito_de_frango_grelhado', 'base_grams': Decimal('120')}, {'food_id': 'queijo_mussarela_light', 'base_grams': Decimal('40')}, {'food_id': 'tomate', 'base_grams': Decimal('50')}]},
    'jantar_strogonoff_fit': {'name': "Strogonoff Fit de Frango", 'category': 'jantar_especial', 'ingredients': [{'food_id': 'peito_de_frango_grelhado', 'base_grams': Decimal('180')}, {'food_id': 'requeijao_light', 'base_grams': Decimal('50')}, {'food_id': 'arroz_branco_cozido', 'base_grams': Decimal('80')}]},
}

# -----------------------------------------------------------------------------
# SEÇÃO 4: GRUPOS DE SUBSTITUIÇÃO DE REFEIÇÕES (`MEAL_SUBSTITUTION_GROUPS`)
# -----------------------------------------------------------------------------
MEAL_SUBSTITUTION_GROUPS: Dict[str, List[str]] = {
    'cafe_da_manha': ['lanche_panqueca_banana', 'lanche_crepioca', 'lanche_sanduiche_frango'],
    'lanches_intermediarios': ['lanche_panqueca_banana', 'lanche_shake_proteico', 'lanche_crepioca', 'lanche_sanduiche_frango'],
    'almoco_jantar_padrao': ['refeicao_frango_arroz', 'refeicao_carne_batata_doce', 'refeicao_tilapia_legumes'],
    'jantares_especiais': ['jantar_pizza_fake', 'jantar_strogonoff_fit', 'refeicao_carne_batata_doce', 'refeicao_tilapia_legumes']
}

# -----------------------------------------------------------------------------
# SEÇÃO 5: LÓGICA DE GERAÇÃO DE PLANOS
# -----------------------------------------------------------------------------
def generate_complete_meal_plan(request_data: dict) -> dict:
    """
    Orquestra a criação de um plano alimentar completo com base nos dados da requisição.
    """
    paciente = request_data.get('paciente', {})
    metas = request_data.get('metas', {})
    
    nome_paciente = paciente.get('nome', 'Cliente')
    num_refeicoes = metas.get('num_refeicoes', 3)
    
    # Define a estrutura de refeições com base no número solicitado
    refeicoes_definidas = []
    if num_refeicoes >= 1:
        refeicoes_definidas.append(('Café da Manhã', 'cafe_da_manha'))
    if num_refeicoes >= 3:
        refeicoes_definidas.append(('Almoço', 'almoco_jantar_padrao'))
    if num_refeicoes >= 4:
        # Para 4 ou mais refeições, o jantar pode ser especial
        refeicoes_definidas.append(('Jantar', 'jantares_especiais'))
    elif num_refeicoes == 2:
        refeicoes_definidas.append(('Jantar', 'almoco_jantar_padrao'))

    lanches_necessarios = num_refeicoes - len(refeicoes_definidas)
    for i in range(lanches_necessarios):
        # Insere lanches entre as refeições principais
        refeicoes_definidas.insert(1 + i, (f'Lanche {i+1}', 'lanches_intermediarios'))

    # Constrói a string do plano em formato Markdown
    plano_md = f"# Plano Alimentar para {nome_paciente}\n\n"
    plano_md += f"**Data:** {date.today().strftime('%Y-%m-%d')}  \n"
    plano_md += f"**Meta Calórica:** {metas.get('kcal_total', 'N/A')} kcal  \n"
    plano_md += f"**Número de Refeições:** {num_refeicoes}\n\n---\n\n"

    for nome_refeicao, grupo_substituicao in refeicoes_definidas:
        opcoes_disponiveis = MEAL_SUBSTITUTION_GROUPS.get(grupo_substituicao, [])
        if not opcoes_disponiveis:
            continue
            
        id_opcao_principal = random.choice(opcoes_disponiveis)
        componente_principal = MEAL_COMPONENT_LIBRARY[id_opcao_principal]
        
        plano_md += f"### {nome_refeicao}: {componente_principal['name']}\n\n"
        plano_md += "**Ingredientes:**\n"
        
        total_kcal_refeicao = Decimal('0')
        for ingrediente in componente_principal['ingredients']:
            info_alimento = NUTRITIONAL_DATABASE[ingrediente['food_id']]
            plano_md += f"- {info_alimento['name']}: {ingrediente['base_grams']}g\n"
            total_kcal_refeicao += (info_alimento['kcal'] / 100) * ingrediente['base_grams']

        plano_md += f"\n*Total Calórico Aproximado (valores base): {round(total_kcal_refeicao)} kcal*\n\n"
        
        opcoes_substituicao = [comp_id for comp_id in opcoes_disponiveis if comp_id != id_opcao_principal]
        if opcoes_substituicao:
            plano_md += "**Opções de Substituição:**\n"
            for sub_id in random.sample(opcoes_substituicao, k=min(len(opcoes_substituicao), 3)): # Limita a 3 opções
                sub_componente = MEAL_COMPONENT_LIBRARY[sub_id]
                plano_md += f"- {sub_componente['name']}\n"
        
        plano_md += "\n---\n\n"
        
    plano_md += "### Recomendações Gerais\n"
    plano_md += "- Beba bastante água ao longo do dia.\n"
    plano_md += "- Os pesos dos alimentos referem-se ao alimento cru, salvo indicação contrária.\n"
    plano_md += "- Sinta-se à vontade para usar temperos naturais (alho, cebola, ervas) à vontade.\n"

    # Monta o objeto de resposta final
    return {
        "plano": {
            "paciente": nome_paciente,
            "data": date.today().strftime('%Y-%m-%d'),
            "peso_kg": paciente.get('peso_kg'),
            "resumo": {
                "meta_kcal": metas.get('kcal_total'),
                "total_kcal_calculado": "Cálculo exato não implementado (usa valores base).",
                "num_refeicoes": num_refeicoes,
            },
            "refeicoes": "Estrutura detalhada não incluída, use o plano_formatado.",
            "plano_formatado": plano_md
        },
        "request_id": str(uuid4())
    }
