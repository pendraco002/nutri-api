# -*- coding: utf-8 -*-
from decimal import Decimal, getcontext
from typing import Dict, List, TypedDict

getcontext().prec = 10

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

NUTRITIONAL_DATABASE: Dict[str, FoodItem] = {
    'ovo_inteiro': {'name': "Ovo Inteiro", 'kcal': Decimal('155'), 'nutrients': {'p': Decimal('13.0'), 'c': Decimal('1.1'), 'g': Decimal('11.0')}},
    'whey_isolado': {'name': "Whey Protein Isolado", 'kcal': Decimal('370'), 'nutrients': {'p': Decimal('85.0'), 'c': Decimal('4.0'), 'g': Decimal('1.0')}},
    'aveia_em_flocos': {'name': "Aveia em Flocos", 'kcal': Decimal('389'), 'nutrients': {'p': Decimal('16.9'), 'c': Decimal('66.3'), 'g': Decimal('6.9')}},
    'banana_prata': {'name': "Banana Prata", 'kcal': Decimal('89'), 'nutrients': {'p': Decimal('1.3'), 'c': Decimal('23.0'), 'g': Decimal('0.3')}},
    'peito_de_frango_grelhado': {'name': "Peito de Frango Grelhado", 'kcal': Decimal('165'), 'nutrients': {'p': Decimal('31.0'), 'c': Decimal('0.0'), 'g': Decimal('3.6')}},
    'arroz_branco_cozido': {'name': "Arroz Branco Cozido", 'kcal': Decimal('130'), 'nutrients': {'p': Decimal('2.7'), 'c': Decimal('28.0'), 'g': Decimal('0.3')}},
    'feijao_preto_cozido': {'name': "Feijão Preto Cozido", 'kcal': Decimal('131'), 'nutrients': {'p': Decimal('8.9'), 'c': Decimal('23.7'), 'g': Decimal('0.5')}},
    'pao_de_forma_integral': {'name': "Pão de Forma Integral", 'kcal': Decimal('246'), 'nutrients': {'p': Decimal('13.0'), 'c': Decimal('41.0'), 'g': Decimal('3.4')}},
    'queijo_mussarela_light': {'name': "Queijo Mussarela Light", 'kcal': Decimal('254'), 'nutrients': {'p': Decimal('24.0'), 'c': Decimal('1.0'), 'g': Decimal('16.0')}},
    'massa_de_rap10': {'name': "Massa de Rap10 Integral", 'kcal': Decimal('298'), 'nutrients': {'p': Decimal('9.1'), 'c': Decimal('57.0'), 'g': Decimal('3.5')}},
    'tomate': {'name': "Tomate", 'kcal': Decimal('18'), 'nutrients': {'p': Decimal('0.9'), 'c': Decimal('3.9'), 'g': Decimal('0.2')}},
}

MEAL_COMPONENT_LIBRARY: Dict[str, MealComponent] = {
    'lanche_panqueca_banana': {
        'name': "Panqueca de Banana e Aveia", 'category': 'panqueca',
        'ingredients': [
            {'food_id': 'ovo_inteiro', 'base_grams': Decimal('100')},
            {'food_id': 'aveia_em_flocos', 'base_grams': Decimal('30')},
            {'food_id': 'banana_prata', 'base_grams': Decimal('50')},
        ]
    },
    'refeicao_frango_arroz': {
        'name': "Frango com Arroz e Feijão", 'category': 'refeicao_solida',
        'ingredients': [
            {'food_id': 'peito_de_frango_grelhado', 'base_grams': Decimal('150')},
            {'food_id': 'arroz_branco_cozido', 'base_grams': Decimal('100')},
            {'food_id': 'feijao_preto_cozido', 'base_grams': Decimal('80')},
        ]
    },
    'jantar_pizza_fake': {
        'name': "Pizza Fake de Frango", 'category': 'jantar_especial',
        'ingredients': [
            {'food_id': 'massa_de_rap10', 'base_grams': Decimal('40')},
            {'food_id': 'peito_de_frango_grelhado', 'base_grams': Decimal('120')},
            {'food_id': 'queijo_mussarela_light', 'base_grams': Decimal('40')},
            {'food_id': 'tomate', 'base_grams': Decimal('50')},
        ]
    },
}

MEAL_SUBSTITUTION_GROUPS: Dict[str, List[str]] = {
    'cafe_da_manha': ['lanche_panqueca_banana'],
    'almoco_jantar_padrao': ['refeicao_frango_arroz'],
    'jantares_especiais': ['jantar_pizza_fake']
}
