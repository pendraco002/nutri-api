# Arquivo: database.py (Versão Pedro Barros)

def get_food_data():
    """ Retorna dados nutricionais básicos. """
    return {
        "ovo_inteiro": {"kcal": 70},
        "clara_de_ovo": {"kcal": 17},
        "whey_protein": {"kcal_por_g": 4.0},
        "pao_integral": {"kcal_por_fatia": 70},
        "arroz_branco_cozido": {"kcal_por_g": 1.3},
        "file_de_frango_grelhado": {"kcal_por_g": 1.65},
        "batata_doce_cozida": {"kcal_por_g": 0.86},
        "azeite_extra_virgem": {"kcal_por_g": 8.8},
        "iogurte_desnatado": {"kcal_por_g": 0.55},
        "chia_em_graos": {"kcal_por_g": 4.8},
        "frutas_gerais": {"kcal_por_g": 0.5},
        "banana": {"kcal": 90},
        "tapioca_seca": {"kcal_por_g": 3.4},
        "requeijao_light": {"kcal_por_g": 1.8},
        "patinho_moido_grelhado": {"kcal_por_g": 2.05},
        "queijo_mussarela": {"kcal_por_g": 3.0},
        "salmao_grelhado": {"kcal_por_g": 2.06},
        "tilapia_grelhada": {"kcal_por_g": 1.20},
        "pao_de_hamburguer": {"kcal": 195},
        "molho_de_tomate": {"kcal_por_g": 0.5},
        "peito_de_peru": {"kcal_por_g": 1.7},
        "cacau_po": {"kcal_por_g": 2.8},
        "canela_po": {"kcal_por_g": 2.4}
    }

def get_pedro_barros_recipes():
    """ Retorna as receitas específicas e obrigatórias do padrão. """
    return {
        "lanche": [
            {
                "nome": "Panqueca Proteica",
                "itens": [
                    {"item": "Banana", "medida": "Grama", "qtd": 60, "kcal": 55},
                    {"item": "Ovo de galinha", "medida": "Unidade", "qtd": 1, "kcal": 70},
                    {"item": "Whey Protein", "medida": "Grama", "qtd": 20, "kcal": 81},
                    {"item": "Cacau em Pó 100%", "medida": "Grama", "qtd": 10, "kcal": 28},
                    {"item": "Canela em pó", "medida": "Grama", "qtd": 5, "kcal": 13}
                ],
                "obs": "Basta misturar tudo e jogar na frigideira ou fazer um bolinho no micro-ondas."
            },
            {
                "nome": "Crepioca",
                "itens": [
                    {"item": "Tapioca seca", "medida": "Grama", "qtd": 20, "kcal": 68},
                    {"item": "Ovo de galinha", "medida": "Unidade", "qtd": 1, "kcal": 70},
                    {"item": "Clara de ovo de galinha", "medida": "Unidade", "qtd": 2, "kcal": 34},
                    {"item": "Requeijão Light", "medida": "Grama", "qtd": 20, "kcal": 38}
                ],
                "obs": "Fazer Crepioca."
            },
            # Adicionar mais 4 receitas de lanche para totalizar 6
            {"nome": "Vitamina Simples", "itens": [{"item": "Fruta", "medida": "Grama", "qtd": 150, "kcal": 75}, {"item": "Whey Protein", "medida": "Grama", "qtd": 30, "kcal": 120}], "obs": "Bater tudo no liquidificador."},
            {"nome": "Iogurte Proteico", "itens": [{"item": "Iogurte Desnatado", "medida": "Grama", "qtd": 170, "kcal": 94}, {"item": "Whey Protein", "medida": "Grama", "qtd": 20, "kcal": 80}], "obs": "Misturar bem."},
            {"nome": "Sanduíche Leve", "itens": [{"item": "Pão Integral", "medida": "Fatia", "qtd": 2, "kcal": 140}, {"item": "Peito de Peru", "medida": "Grama", "qtd": 50, "kcal": 85}], "obs": "Montar o sanduíche."},
            {"nome": "Ovos com Torrada", "itens": [{"item": "Ovo de galinha", "medida": "Unidade", "qtd": 2, "kcal": 140}, {"item": "Pão Integral", "medida": "Fatia", "qtd": 1, "kcal": 70}], "obs": "Pode cozinhar ou fritar os ovos sem gordura."}
        ],
        "jantar": [
            {
                "nome": "Strogonoff Light",
                "itens": [
                    {"item": "Filé-mignon Cozido(a)", "medida": "Grama", "qtd": 100, "kcal": 204},
                    {"item": "Ketchup", "medida": "Grama", "qtd": 10, "kcal": 10},
                    {"item": "Mostarda", "medida": "Grama", "qtd": 10, "kcal": 8},
                    {"item": "Arroz branco (cozido)", "medida": "Grama", "qtd": 75, "kcal": 94},
                    {"item": "Champignon (cogumelo paris)", "medida": "Grama", "qtd": 50, "kcal": 13},
                    {"item": "Creme de Leite Light", "medida": "Grama", "qtd": 40, "kcal": 46}
                ]
            },
            {
                "nome": "Hambúrguer Artesanal",
                "itens": [
                    {"item": "Pão de hambúrguer", "medida": "Unidade", "qtd": 1, "kcal": 195},
                    {"item": "Carne de Hambúrguer (Patinho 120g Cru)", "medida": "Unidade", "qtd": 1, "kcal": 199},
                    {"item": "Queijo tipo mussarela", "medida": "Grama", "qtd": 20, "kcal": 56},
                    {"item": "Ketchup/Mostarda/Maionese Light", "medida": "Colher de sopa", "qtd": 1, "kcal": 15}
                ]
            },
            # Adicionar mais 2 receitas de jantar para totalizar 4
            {"nome": "Pizza Fake", "itens": [{"item": "Pão Sírio Integral", "medida": "Unidade", "qtd": 1, "kcal": 150}, {"item": "Molho de Tomate", "medida": "Grama", "qtd": 40, "kcal": 20}, {"item": "Queijo Mussarela", "medida": "Grama", "qtd": 60, "kcal": 180}]},
            {"nome": "Salmão com Batata Doce", "itens": [{"item": "Salmão Grelhado", "medida": "Grama", "qtd": 150, "kcal": 309}, {"item": "Batata Doce Cozida", "medida": "Grama", "qtd": 200, "kcal": 172}]}
        ],
        "ceia": {
            "kcal": 150, # Valor de exemplo
            "itens": [
                {"item": "Whey Protein", "medida": "Gramas", "qtd": "15", "kcal": 60},
                {"item": "Iogurte natural", "medida": "Gramas", "qtd": "100", "kcal": 55},
                {"item": "Fruta (menos banana e abacate)", "medida": "Gramas", "qtd": "50", "kcal": 25},
                {"item": "Fibra: Chia ou psyllium", "medida": "Gramas", "qtd": "5", "kcal": 10}
            ]
        }
    }
