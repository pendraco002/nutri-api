# -*- coding: utf-8 -*-
"""
Módulo de Dados para o Sistema de Nutrição Pedro Barros.

Este arquivo centraliza toda a informação estática necessária para a geração
de planos alimentares. Ele foi projetado para ser a única fonte de verdade
para dados nutricionais e componentes de refeição, seguindo as melhores
práticas de engenharia de software para garantir manutenibilidade, precisão e
clareza.

Arquitetura de Dados:
1.  **Precisão Numérica:** Utiliza o tipo `Decimal` para todos os valores
    nutricionais (calorias, macronutrientes) para evitar erros de
    arredondamento de ponto flutuante, uma recomendação crítica da
    auditoria de código.
2.  **Estruturas Tipadas:** Emprega `TypedDict` para definir schemas de dados
    claros e robustos, melhorando a legibilidade e permitindo a verificação
    estática de tipos.
3.  **Base de Dados de Alimentos (`NUTRITIONAL_DATABASE`):** Um dicionário
    que mapeia um ID de alimento padronizado para seus dados nutricionais por
    100g. Esta é a camada fundamental de dados brutos.
4.  **Biblioteca de Componentes de Refeição (`MEAL_COMPONENT_LIBRARY`):**
    Implementa a filosofia de "componentes modulares". Cada componente é uma
    "receita" com ingredientes e suas quantidades base, referenciando
    alimentos da `NUTRITIONAL_DATABASE`. Isso desacopla a lógica de
    criação de planos da definição das próprias refeições.
5.  **Grupos de Substituição (`MEAL_SUBSTITUTION_GROUPS`):** Mapeia tipos de
    refeição (ex: "lanches", "jantares_especiais") para listas de
    componentes da biblioteca, permitindo a geração dinâmica de opções de
    substituição, como as vistas nos planos de exemplo.

Este módulo é a implementação direta das recomendações de auditoria,
transformando lógica de negócio hardcoded em estruturas de dados gerenciáveis
e extensíveis.
"""

from decimal import Decimal, getcontext
from typing import Dict, List, TypedDict

# Define a precisão global para todos os cálculos decimais no sistema.
# Uma precisão de 10 casas é mais do que suficiente para cálculos nutricionais.
getcontext().prec = 10

# -----------------------------------------------------------------------------
# SEÇÃO 1: ESTRUTURAS DE DADOS TIPADAS (DATA SCHEMAS)
# -----------------------------------------------------------------------------
# Define schemas claros para os dados, melhorando a manutenibilidade e
# prevenindo erros através da verificação estática de tipos.

class NutrientInfo(TypedDict):
    """Representa a composição de macronutrientes (proteína, carbo, gordura)."""
    p: Decimal  # Proteínas em gramas
    c: Decimal  # Carboidratos em gramas
    g: Decimal  # Gorduras em gramas


class FoodItem(TypedDict):
    """
    Define a estrutura para um item na base de dados de alimentos.
    Todos os valores são baseados em uma porção de 100g.
    """
    name: str
    kcal: Decimal
    nutrients: NutrientInfo


class Ingredient(TypedDict):
    """
    Representa um ingrediente dentro de um componente de refeição,
    vinculando um alimento a uma quantidade base.
    """
    food_id: str
    base_grams: Decimal


class MealComponent(TypedDict):
    """
    Define um componente de refeição modular (uma "receita" ou "bloco").
    É a unidade fundamental da Biblioteca de Componentes.
    """
    name: str
    category: str  # Ex: 'panqueca', 'shake', 'refeicao_solida'
    ingredients: List[Ingredient]


# -----------------------------------------------------------------------------
# SEÇÃO 2: BASE DE DADOS NUTRICIONAL (`NUTRITIONAL_DATABASE`)
# -----------------------------------------------------------------------------
# Fonte de verdade para os dados nutricionais de cada alimento.
# Chaves: ID de alimento único e padronizado.
# Valores: Dicionário `FoodItem` com dados por 100g.

NUTRITIONAL_DATABASE: Dict[str, FoodItem] = {
    'ovo_inteiro': {
        'name': "Ovo Inteiro",
        'kcal': Decimal('155'),
        'nutrients': {'p': Decimal('13.0'), 'c': Decimal('1.1'), 'g': Decimal('11.0')}
    },
    'clara_de_ovo': {
        'name': "Clara de Ovo",
        'kcal': Decimal('52'),
        'nutrients': {'p': Decimal('11.0'), 'c': Decimal('0.7'), 'g': Decimal('0.2')}
    },
    'whey_isolado': {
        'name': "Whey Protein Isolado",
        'kcal': Decimal('370'),
        'nutrients': {'p': Decimal('85.0'), 'c': Decimal('4.0'), 'g': Decimal('1.0')}
    },
    'aveia_em_flocos': {
        'name': "Aveia em Flocos",
        'kcal': Decimal('389'),
        'nutrients': {'p': Decimal('16.9'), 'c': Decimal('66.3'), 'g': Decimal('6.9')}
    },
    'banana_prata': {
        'name': "Banana Prata",
        'kcal': Decimal('89'),
        'nutrients': {'p': Decimal('1.3'), 'c': Decimal('23.0'), 'g': Decimal('0.3')}
    },
    'peito_de_frango_grelhado': {
        'name': "Peito de Frango Grelhado",
        'kcal': Decimal('165'),
        'nutrients': {'p': Decimal('31.0'), 'c': Decimal('0.0'), 'g': Decimal('3.6')}
    },
    'arroz_branco_cozido': {
        'name': "Arroz Branco Cozido",
        'kcal': Decimal('130'),
        'nutrients': {'p': Decimal('2.7'), 'c': Decimal('28.0'), 'g': Decimal('0.3')}
    },
    'feijao_preto_cozido': {
        'name': "Feijão Preto Cozido",
        'kcal': Decimal('131'),
        'nutrients': {'p': Decimal('8.9'), 'c': Decimal('23.7'), 'g': Decimal('0.5')}
    },
    'pao_de_forma_integral': {
        'name': "Pão de Forma Integral",
        'kcal': Decimal('246'),
        'nutrients': {'p': Decimal('13.0'), 'c': Decimal('41.0'), 'g': Decimal('3.4')}
    },
    'queijo_mussarela_light': {
        'name': "Queijo Mussarela Light",
        'kcal': Decimal('254'),
        'nutrients': {'p': Decimal('24.0'), 'c': Decimal('1.0'), 'g': Decimal('16.0')}
    },
    'tomate': {
        'name': "Tomate",
        'kcal': Decimal('18'),
        'nutrients': {'p': Decimal('0.9'), 'c': Decimal('3.9'), 'g': Decimal('0.2')}
    },
    'leite_desnatado': {
        'name': "Leite Desnatado",
        'kcal': Decimal('35'),
        'nutrients': {'p': Decimal('3.4'), 'c': Decimal('5.0'), 'g': Decimal('0.1')}
    },
    'carne_moida_patinho': {
        'name': "Carne Moída (Patinho)",
        'kcal': Decimal('219'),
        'nutrients': {'p': Decimal('28.0'), 'c': Decimal('0.0'), 'g': Decimal('11.0')}
    },
    'batata_doce_cozida': {
        'name': "Batata Doce Cozida",
        'kcal': Decimal('86'),
        'nutrients': {'p': Decimal('1.6'), 'c': Decimal('20.1'), 'g': Decimal('0.1')}
    },
    'tilapia_grelhada': {
        'name': "Filé de Tilápia Grelhado",
        'kcal': Decimal('128'),
        'nutrients': {'p': Decimal('26.0'), 'c': Decimal('0.0'), 'g': Decimal('2.6')}
    },
    'massa_de_rap10': {
        'name': "Massa de Rap10 Integral",
        'kcal': Decimal('298'),
        'nutrients': {'p': Decimal('9.1'), 'c': Decimal('57.0'), 'g': Decimal('3.5')}
    },
    'requeijao_light': {
        'name': "Requeijão Light",
        'kcal': Decimal('173'),
        'nutrients': {'p': Decimal('11.0'), 'c': Decimal('3.3'), 'g': Decimal('12.0')}
    },
}

# -----------------------------------------------------------------------------
# SEÇÃO 3: BIBLIOTECA DE COMPONENTES DE REFEIÇÃO (`MEAL_COMPONENT_LIBRARY`)
# -----------------------------------------------------------------------------
# Coleção de "blocos de Lego" nutricionais. Cada item é uma receita base que
# pode ser escalada para atingir metas calóricas específicas.

MEAL_COMPONENT_LIBRARY: Dict[str, MealComponent] = {
    # --- Componentes para Café da Manhã e Lanches ---
    'lanche_panqueca_banana': {
        'name': "Panqueca de Banana e Aveia",
        'category': 'panqueca',
        'ingredients': [
            {'food_id': 'ovo_inteiro', 'base_grams': Decimal('100')}, # 2 ovos
            {'food_id': 'aveia_em_flocos', 'base_grams': Decimal('30')},
            {'food_id': 'banana_prata', 'base_grams': Decimal('50')}, # Meia banana
        ]
    },
    'lanche_shake_proteico': {
        'name': "Shake Proteico com Frutas",
        'category': 'shake',
        'ingredients': [
            {'food_id': 'whey_isolado', 'base_grams': Decimal('30')},
            {'food_id': 'banana_prata', 'base_grams': Decimal('100')},
            {'food_id': 'leite_desnatado', 'base_grams': Decimal('200')},
        ]
    },
    'lanche_crepioca': {
        'name': "Crepioca com Queijo",
        'category': 'crepioca',
        'ingredients': [
            {'food_id': 'ovo_inteiro', 'base_grams': Decimal('50')},
            {'food_id': 'clara_de_ovo', 'base_grams': Decimal('60')},
            {'food_id': 'queijo_mussarela_light', 'base_grams': Decimal('30')},
        ]
    },
    'lanche_sanduiche_frango': {
        'name': "Sanduíche de Frango",
        'category': 'sanduiche',
        'ingredients': [
            {'food_id': 'pao_de_forma_integral', 'base_grams': Decimal('50')}, # 2 fatias
            {'food_id': 'peito_de_frango_grelhado', 'base_grams': Decimal('100')},
            {'food_id': 'requeijao_light', 'base_grams': Decimal('20')},
        ]
    },

    # --- Componentes para Almoço e Jantar (Refeições Sólidas) ---
    'refeicao_frango_arroz': {
        'name': "Frango com Arroz e Feijão",
        'category': 'refeicao_solida',
        'ingredients': [
            {'food_id': 'peito_de_frango_grelhado', 'base_grams': Decimal('150')},
            {'food_id': 'arroz_branco_cozido', 'base_grams': Decimal('100')},
            {'food_id': 'feijao_preto_cozido', 'base_grams': Decimal('80')},
        ]
    },
    'refeicao_carne_batata_doce': {
        'name': "Carne Moída com Batata Doce",
        'category': 'refeicao_solida',
        'ingredients': [
            {'food_id': 'carne_moida_patinho', 'base_grams': Decimal('150')},
            {'food_id': 'batata_doce_cozida', 'base_grams': Decimal('150')},
        ]
    },
    'refeicao_tilapia_legumes': {
        'name': "Tilápia com Legumes",
        'category': 'refeicao_solida',
        'ingredients': [
            {'food_id': 'tilapia_grelhada', 'base_grams': Decimal('180')},
            {'food_id': 'tomate', 'base_grams': Decimal('100')}, # Tomate como exemplo de legume
        ]
    },

    # --- Componentes para Jantares Especiais (Exemplo "Daniela") ---
    'jantar_pizza_fake': {
        'name': "Pizza Fake de Frango",
        'category': 'jantar_especial',
        'ingredients': [
            {'food_id': 'massa_de_rap10', 'base_grams': Decimal('40')},
            {'food_id': 'peito_de_frango_grelhado', 'base_grams': Decimal('120')},
            {'food_id': 'queijo_mussarela_light', 'base_grams': Decimal('40')},
            {'food_id': 'tomate', 'base_grams': Decimal('50')},
        ]
    },
    'jantar_strogonoff_fit': {
        'name': "Strogonoff Fit de Frango",
        'category': 'jantar_especial',
        'ingredients': [
            {'food_id': 'peito_de_frango_grelhado', 'base_grams': Decimal('180')},
            {'food_id': 'requeijao_light', 'base_grams': Decimal('50')},
            {'food_id': 'arroz_branco_cozido', 'base_grams': Decimal('80')},
        ]
    },
}

# -----------------------------------------------------------------------------
# SEÇÃO 4: GRUPOS DE SUBSTITUIÇÃO DE REFEIÇÕES (`MEAL_SUBSTITUTION_GROUPS`)
# -----------------------------------------------------------------------------
# Define quais componentes podem ser usados como substitutos em diferentes
# refeições. Isso alimenta a lógica de geração de opções, como as "6 opções de
# lanche" do exemplo "Juliana".

MEAL_SUBSTITUTION_GROUPS: Dict[str, List[str]] = {
    'cafe_da_manha': [
        'lanche_panqueca_banana',
        'lanche_crepioca',
        'lanche_sanduiche_frango'
    ],
    'lanches_intermediarios': [
        'lanche_panqueca_banana',
        'lanche_shake_proteico',
        'lanche_crepioca',
        'lanche_sanduiche_frango'
        # Adicionar mais 2 para completar as 6 opções do exemplo Juliana
    ],
    'almoco_jantar_padrao': [
        'refeicao_frango_arroz',
        'refeicao_carne_batata_doce',
        'refeicao_tilapia_legumes',
    ],
    'jantares_especiais': [
        'jantar_pizza_fake',
        'jantar_strogonoff_fit',
        'refeicao_carne_batata_doce', # Uma refeição padrão pode ser uma opção
        'refeicao_tilapia_legumes'
    ]
}

if __name__ == '__main__':
    # Este bloco serve como um teste de sanidade e demonstração de uso.
    # Ele verifica se os IDs de alimentos nos componentes existem na base de dados
    # e imprime um resumo das estruturas de dados.
    print("--- INICIANDO VERIFICAÇÃO DE SANIDADE DOS DADOS ---")

    # 1. Verificar integridade dos componentes
    errors = []
    for comp_id, component in MEAL_COMPONENT_LIBRARY.items():
        for ingredient in component['ingredients']:
            if ingredient['food_id'] not in NUTRITIONAL_DATABASE:
                error_msg = (
                    f"[ERRO] Componente '{comp_id}' ({component['name']}) "
                    f"refere-se a um food_id inexistente: '{ingredient['food_id']}'"
                )
                errors.append(error_msg)

    # 2. Verificar integridade dos grupos de substituição
    for group_name, comp_ids in MEAL_SUBSTITUTION_GROUPS.items():
        for comp_id in comp_ids:
            if comp_id not in MEAL_COMPONENT_LIBRARY:
                error_msg = (
                    f"[ERRO] Grupo de substituição '{group_name}' "
                    f"refere-se a um component_id inexistente: '{comp_id}'"
                )
                errors.append(error_msg)

    if errors:
        print("\nENCONTRADOS ERROS DE INTEGRIDADE REFERENCIAL:")
        for error in errors:
            print(error)
    else:
        print("\n[SUCESSO] Todas as referências de ingredientes e componentes são válidas.")

    # 3. Imprimir resumo dos dados carregados
    print("\n--- RESUMO DOS DADOS CARREGADOS ---")
    print(f"Total de alimentos na base de dados: {len(NUTRITIONAL_DATABASE)}")
    print(f"Total de componentes de refeição na biblioteca: {len(MEAL_COMPONENT_LIBRARY)}")
    print(f"Total de grupos de substituição definidos: {len(MEAL_SUBSTITUTION_GROUPS)}")

    # Exemplo de acesso a um dado
    try:
        panqueca = MEAL_COMPONENT_LIBRARY['lanche_panqueca_banana']
        primeiro_ingrediente_id = panqueca['ingredients'][0]['food_id']
        nome_ingrediente = NUTRITIONAL_DATABASE[primeiro_ingrediente_id]['name']
        print(f"\nExemplo de acesso: O primeiro ingrediente da panqueca é '{nome_ingrediente}'.")
    except KeyError as e:
        print(f"\nErro ao acessar dado de exemplo: {e}")

    print("\n--- VERIFICAÇÃO DE SANIDADE CONCLUÍDA ---")
