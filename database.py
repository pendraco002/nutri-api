# database.py
def get_food_data():
    """ Base de dados de alimentos com notas de preparo. Valores por 1 grama. """
    return {
        # PROTEÍNAS PRINCIPAIS
        "peito_frango_grelhado_sem_pele": {"kcal": 1.65, "p": 0.31, "c": 0, "g": 0.036, "categoria": "proteina", "unidade_comum": "g", "obs": "Ideal grelhado ou cozido sem adição de gordura"},
        "clara_ovo_pasteurizada": {"kcal": 0.52, "p": 0.11, "c": 0.007, "g": 0.002, "categoria": "proteina", "unidade_comum": "ml", "obs": "1 ovo = 30ml de clara líquida"},
        "whey_protein_isolado_hidrolisado": {"kcal": 3.7, "p": 0.9, "c": 0.01, "g": 0.01, "categoria": "proteina", "unidade_comum": "g", "obs": "Diluir em água ou adoçante zero"},
        "tilapia_assada": {"kcal": 1.28, "p": 0.26, "c": 0, "g": 0.026, "categoria": "proteina", "unidade_comum": "g", "obs": "Temperar apenas com limão e ervas"},
        "patinho_moido_95_5": {"kcal": 1.5, "p": 0.22, "c": 0, "g": 0.06, "categoria": "proteina", "unidade_comum": "g", "obs": "Preferir extra magro (95% carne / 5% gordura)"},
        "file_mignon": {"kcal": 1.58, "p": 0.22, "c": 0, "g": 0.07, "categoria": "proteina", "unidade_comum": "g", "obs": "Cortar gorduras aparentes antes do preparo"},
        "salmao_grelhado": {"kcal": 2.08, "p": 0.22, "c": 0, "g": 0.13, "categoria": "proteina", "unidade_comum": "g", "obs": "Rica fonte de Ômega 3"},
        "atum_enlatado_agua": {"kcal": 1.16, "p": 0.26, "c": 0, "g": 0.01, "categoria": "proteina", "unidade_comum": "g", "obs": "Preferir em água, escorrer bem"},
        "peixe_branco_qualquer": {"kcal": 1.05, "p": 0.23, "c": 0, "g": 0.01, "categoria": "proteina", "unidade_comum": "g", "obs": "Exemplos: badejo, linguado, pescada, bacalhau fresco"},
        "file_suino_magro": {"kcal": 1.43, "p": 0.21, "c": 0, "g": 0.065, "categoria": "proteina", "unidade_comum": "g", "obs": "Remover gordura aparente antes do preparo"},
        
        # OVOS
        "ovo_inteiro": {"kcal": 1.49, "p": 0.125, "c": 0.01, "g": 0.10, "categoria": "proteina", "unidade_comum": "unidade", "obs": "Consumir inteiro, preferencialmente cozido ou mexido"},
        "gema_ovo": {"kcal": 3.54, "p": 0.16, "c": 0.003, "g": 0.32, "categoria": "gordura", "unidade_comum": "unidade", "obs": "Rica em nutrientes, moderação no consumo"},
        "clara_ovo": {"kcal": 0.52, "p": 0.11, "c": 0.007, "g": 0.002, "categoria": "proteina", "unidade_comum": "unidade", "obs": "Proteína de alto valor biológico"},
        
        # CARBOIDRATOS
        "arroz_branco_cozido": {"kcal": 1.3, "p": 0.025, "c": 0.28, "g": 0.002, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Medida: 4 colheres de sopa = 100g"},
        "arroz_integral_cozido": {"kcal": 1.1, "p": 0.026, "c": 0.23, "g": 0.01, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Rica fonte de fibras"},
        "batata_doce_cozida": {"kcal": 0.86, "p": 0.016, "c": 0.2, "g": 0.001, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Cozida ou assada com casca"},
        "batata_inglesa_cozida": {"kcal": 0.78, "p": 0.02, "c": 0.17, "g": 0.001, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Sem adição de gorduras"},
        "macarrao_integral_cozido": {"kcal": 1.58, "p": 0.06, "c": 0.31, "g": 0.01, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Preferir grano duro ou integral"},
        "aipim_macaxeira_cozido": {"kcal": 1.2, "p": 0.01, "c": 0.29, "g": 0.001, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Sem adição de gorduras"},
        "inhame_cozido": {"kcal": 0.97, "p": 0.02, "c": 0.23, "g": 0.001, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Sem adição de gorduras"},
        "abobora_japonesa_cozida": {"kcal": 0.36, "p": 0.012, "c": 0.08, "g": 0.001, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Rica em carotenoides"},
        
        # PÃES
        "pao_forma_integral": {"kcal": 2.65, "p": 0.13, "c": 0.49, "g": 0.04, "categoria": "carboidrato", "unidade_comum": "fatia", "obs": "1 fatia = 25g em média"},
        "pao_francês": {"kcal": 3.0, "p": 0.08, "c": 0.58, "g": 0.03, "categoria": "carboidrato", "unidade_comum": "unidade", "obs": "1 unidade pequena = 50g"},
        "pao_hamburguer_light": {"kcal": 2.5, "p": 0.09, "c": 0.48, "g": 0.02, "categoria": "carboidrato", "unidade_comum": "unidade", "obs": "1 unidade = 50g em média"},
        "rap10_integral": {"kcal": 3.1, "p": 0.09, "c": 0.6, "g": 0.03, "categoria": "carboidrato", "unidade_comum": "unidade", "obs": "Ideal para lanches e snacks"},
        "tapioca_seca": {"kcal": 3.5, "p": 0, "c": 0.87, "g": 0, "categoria": "carboidrato", "unidade_comum": "g", "obs": "20g = aproximadamente 2 colheres de sopa"},
        "aveia_flocos": {"kcal": 3.89, "p": 0.17, "c": 0.66, "g": 0.07, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Excelente fonte de fibras solúveis"},
        
        # LEGUMINOSAS
        "feijao_carioca_cozido": {"kcal": 0.76, "p": 0.05, "c": 0.14, "g": 0.005, "categoria": "carboidrato", "unidade_comum": "g", "obs": "1 concha média = 80g"},
        "feijao_preto_cozido": {"kcal": 0.77, "p": 0.05, "c": 0.14, "g": 0.005, "categoria": "carboidrato", "unidade_comum": "g", "obs": "1 concha média = 80g"},
        "lentilha_cozida": {"kcal": 1.16, "p": 0.09, "c": 0.2, "g": 0.004, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Rica em ferro, substituir feijão"},
        "grao_de_bico_cozido": {"kcal": 1.64, "p": 0.09, "c": 0.27, "g": 0.03, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Cozido al dente, sem adição de óleos"},
        "ervilha_cozida": {"kcal": 0.81, "p": 0.05, "c": 0.14, "g": 0.006, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Fresca ou congelada, sem enlatados"},
        
        # LATICÍNIOS
        "requeijao_light": {"kcal": 1.88, "p": 0.1, "c": 0.05, "g": 0.15, "categoria": "gordura", "unidade_comum": "g", "obs": "Ou porção equivalente de creme de ricota light ou queijo cottage"},
        "queijo_cottage": {"kcal": 1.01, "p": 0.11, "c": 0.03, "g": 0.04, "categoria": "proteina", "unidade_comum": "g", "obs": "Baixo teor de gordura, evitar versões com adição de creme"},
        "queijo_minas_light": {"kcal": 2.32, "p": 0.18, "c": 0.03, "g": 0.16, "categoria": "proteina", "unidade_comum": "g", "obs": "Preferir versão light, consumir moderadamente"},
        "ricota_fresca": {"kcal": 1.74, "p": 0.11, "c": 0.03, "g": 0.13, "categoria": "proteina", "unidade_comum": "g", "obs": "Baixo teor de sódio, boa opção proteica"},
        "iogurte_desnatado_zero": {"kcal": 0.4, "p": 0.05, "c": 0.06, "g": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Sem açúcar adicionado, versão natural"},
        "iogurte_natural_integral": {"kcal": 0.61, "p": 0.03, "c": 0.04, "g": 0.03, "categoria": "proteina", "unidade_comum": "g", "obs": "Sem açúcar adicionado"},
        "leite_desnatado": {"kcal": 0.32, "p": 0.03, "c": 0.05, "g": 0, "categoria": "proteina", "unidade_comum": "ml", "obs": "Versão com menor teor de gordura"},
        "mussarela_light": {"kcal": 2.5, "p": 0.25, "c": 0.01, "g": 0.15, "categoria": "proteina", "unidade_comum": "g", "obs": "Preferir versão light, consumir moderadamente"},
        
        # OLEAGINOSAS
        "castanha_do_para": {"kcal": 6.54, "p": 0.14, "c": 0.12, "g": 0.66, "categoria": "gordura", "unidade_comum": "unidade", "obs": "Rica em selênio, 1 unidade média = 5g"},
        "amendoim": {"kcal": 5.67, "p": 0.26, "c": 0.16, "g": 0.49, "categoria": "gordura", "unidade_comum": "g", "obs": "Sem sal e sem pele, consumir moderadamente"},
        "amendoa": {"kcal": 5.92, "p": 0.21, "c": 0.22, "g": 0.51, "categoria": "gordura", "unidade_comum": "unidade", "obs": "1 unidade média = 1,2g"},
        "castanha_de_caju": {"kcal": 5.53, "p": 0.18, "c": 0.30, "g": 0.44, "categoria": "gordura", "unidade_comum": "g", "obs": "Sem sal, consumir moderadamente"},
        "pasta_amendoim_integral": {"kcal": 6.13, "p": 0.24, "c": 0.22, "g": 0.50, "categoria": "gordura", "unidade_comum": "g", "obs": "100% amendoim, sem aditivos ou açúcares"},
        
        # SEMENTES
        "chia": {"kcal": 4.86, "p": 0.17, "c": 0.42, "g": 0.31, "categoria": "gordura", "unidade_comum": "g", "obs": "Hidratar no iogurte antes de consumir"},
        "linhaça_moída": {"kcal": 5.34, "p": 0.18, "c": 0.29, "g": 0.42, "categoria": "gordura", "unidade_comum": "g", "obs": "Moer antes de consumir para melhor absorção"},
        "psyllium": {"kcal": 3.7, "p": 0.015, "c": 0.8, "g": 0.005, "categoria": "fibra", "unidade_comum": "g", "obs": "Tomar como remédio com 100ml de água"},
        "semente_abobora": {"kcal": 5.59, "p": 0.30, "c": 0.10, "g": 0.49, "categoria": "gordura", "unidade_comum": "g", "obs": "Rica em zinco e magnésio"},
        "semente_girassol": {"kcal": 5.84, "p": 0.21, "c": 0.20, "g": 0.51, "categoria": "gordura", "unidade_comum": "g", "obs": "Sem sal, consumir moderadamente"},
        
        # FRUTAS
        "banana": {"kcal": 0.89, "p": 0.01, "c": 0.23, "g": 0.003, "categoria": "fruta", "unidade_comum": "unidade", "obs": "1 unidade média = 100g"},
        "maca": {"kcal": 0.52, "p": 0.003, "c": 0.14, "g": 0.002, "categoria": "fruta", "unidade_comum": "unidade", "obs": "1 unidade média = 120g"},
        "mamao_papaia": {"kcal": 0.43, "p": 0.005, "c": 0.11, "g": 0.001, "categoria": "fruta", "unidade_comum": "g", "obs": "Rico em enzimas digestivas"},
        "morango": {"kcal": 0.32, "p": 0.007, "c": 0.08, "g": 0.003, "categoria": "fruta", "unidade_comum": "g", "obs": "Rico em antioxidantes"},
        "melao": {"kcal": 0.34, "p": 0.009, "c": 0.08, "g": 0.001, "categoria": "fruta", "unidade_comum": "g", "obs": "Baixo índice glicêmico"},
        "abacaxi": {"kcal": 0.50, "p": 0.005, "c": 0.13, "g": 0.001, "categoria": "fruta", "unidade_comum": "g", "obs": "Rico em bromelina"},
        "laranja_pera": {"kcal": 0.47, "p": 0.009, "c": 0.12, "g": 0.001, "categoria": "fruta", "unidade_comum": "unidade", "obs": "1 unidade média = 130g"},
        "kiwi": {"kcal": 0.61, "p": 0.011, "c": 0.15, "g": 0.005, "categoria": "fruta", "unidade_comum": "unidade", "obs": "1 unidade média = 76g"},
        "uva": {"kcal": 0.69, "p": 0.007, "c": 0.18, "g": 0.002, "categoria": "fruta", "unidade_comum": "g", "obs": "Preferir uvas escuras"},
        
        # VEGETAIS
        "legumes_variados": {"kcal": 0.25, "p": 0.015, "c": 0.05, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "Mistura de vegetais cozidos no vapor"},
        "tomate": {"kcal": 0.18, "p": 0.009, "c": 0.039, "g": 0.002, "categoria": "vegetal", "unidade_comum": "unidade", "obs": "1 unidade média = 125g"},
        "pepino": {"kcal": 0.15, "p": 0.007, "c": 0.036, "g": 0.001, "categoria": "vegetal", "unidade_comum": "unidade", "obs": "1 unidade média = 300g"},
        "alface": {"kcal": 0.15, "p": 0.014, "c": 0.029, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "Consumir à vontade, lavar bem"},
        "brocolis": {"kcal": 0.35, "p": 0.029, "c": 0.07, "g": 0.004, "categoria": "vegetal", "unidade_comum": "g", "obs": "Cozinhar no vapor ou grelhado"},
        "abobrinha": {"kcal": 0.17, "p": 0.012, "c": 0.031, "g": 0.003, "categoria": "vegetal", "unidade_comum": "g", "obs": "Baixo índice glicêmico"},
        "cenoura": {"kcal": 0.41, "p": 0.009, "c": 0.096, "g": 0.002, "categoria": "vegetal", "unidade_comum": "unidade", "obs": "1 unidade média = 80g"},
        "espinafre": {"kcal": 0.23, "p": 0.029, "c": 0.036, "g": 0.004, "categoria": "vegetal", "unidade_comum": "g", "obs": "Rico em ferro, consumir cozido"},
        "rucula": {"kcal": 0.25, "p": 0.026, "c": 0.036, "g": 0.007, "categoria": "vegetal", "unidade_comum": "g", "obs": "Rica em antioxidantes"},
        
        # GORDURAS
        "azeite_extra_virgem": {"kcal": 8.84, "p": 0, "c": 0, "g": 1.0, "categoria": "gordura", "unidade_comum": "colher", "obs": "1 colher de sopa = 13ml"},
        "oleo_coco_extravirgem": {"kcal": 8.62, "p": 0, "c": 0, "g": 1.0, "categoria": "gordura", "unidade_comum": "colher", "obs": "1 colher de sopa = 13ml"},
        "abacate": {"kcal": 1.6, "p": 0.02, "c": 0.085, "g": 0.15, "categoria": "gordura", "unidade_comum": "g", "obs": "Rico em gorduras monoinsaturadas"},
        
        # DIVERSOS
        "cacau_po_100": {"kcal": 2.28, "p": 0.196, "c": 0.58, "g": 0.14, "categoria": "diversos", "unidade_comum": "g", "obs": "100% cacau, sem açúcar"},
        "canela_po": {"kcal": 2.47, "p": 0.04, "c": 0.81, "g": 0.01, "categoria": "diversos", "unidade_comum": "g", "obs": "Ajuda a regular a glicemia"},
        "molho_tomate_caseiro": {"kcal": 0.3, "p": 0.01, "c": 0.07, "g": 0.001, "categoria": "diversos", "unidade_comum": "g", "obs": "Preparado sem adição de açúcar ou óleo"},
        "ketchup_zero": {"kcal": 0.4, "p": 0.01, "c": 0.1, "g": 0, "categoria": "diversos", "unidade_comum": "g", "obs": "Versão sem açúcar adicionado"},
        "mostarda": {"kcal": 0.66, "p": 0.04, "c": 0.06, "g": 0.04, "categoria": "diversos", "unidade_comum": "g", "obs": "Preferir versão tradicional sem mel"},
        "doce_de_leite_light": {"kcal": 3.1, "p": 0.07, "c": 0.55, "g": 0.07, "categoria": "diversos", "unidade_comum": "g", "obs": "Consumir com moderação em ocasiões específicas"},
        "cafe_preto": {"kcal": 0.02, "p": 0, "c": 0, "g": 0, "categoria": "diversos", "unidade_comum": "ml", "obs": "Sem adição de açúcar ou adoçante"},
        "cha_verde": {"kcal": 0.01, "p": 0, "c": 0, "g": 0, "categoria": "diversos", "unidade_comum": "ml", "obs": "Sem adição de açúcar ou adoçante"},
        "champignon": {"kcal": 0.22, "p": 0.03, "c": 0.03, "g": 0.003, "categoria": "vegetal", "unidade_comum": "g", "obs": "Sem conservantes, preferir frescos"},
        "tomate_cereja": {"kcal": 0.18, "p": 0.009, "c": 0.039, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "Ideal para saladas e decoração de pratos"},
        "oregano": {"kcal": 2.65, "p": 0.09, "c": 0.68, "g": 0.04, "categoria": "diversos", "unidade_comum": "g", "obs": "Tempero para pizzas e massas"},
        "gelatina_diet": {"kcal": 0.25, "p": 0.06, "c": 0, "g": 0, "categoria": "diversos", "unidade_comum": "g", "obs": "Versão sem açúcar, boa fonte de colágeno"},
        "creme_leite_light": {"kcal": 1.87, "p": 0.03, "c": 0.05, "g": 0.17, "categoria": "gordura", "unidade_comum": "g", "obs": "Utilizar versão light apenas"},
    }

def get_meal_templates():
    """ Biblioteca de Componentes Modulares com tipos e detalhes. """
    return {
        "cafe_da_manha": [
            {"id": "cafe_completo_1", "type": "base", "nome_template": "Café da Manhã Completo", "ingredientes": ["ovo_inteiro:50", "pao_forma_integral:25", "whey_protein_isolado_hidrolisado:20", "iogurte_desnatado_zero:100", "chia:5", "mamao_papaia:100"]},
            {"id": "cafe_completo_2", "type": "base", "nome_template": "Café da Manhã com Frutas", "ingredientes": ["ovo_inteiro:100", "aveia_flocos:30", "whey_protein_isolado_hidrolisado:25", "banana:60", "linhaça_moída:10"]},
            {"id": "cafe_completo_3", "type": "base", "nome_template": "Café da Manhã Leve", "ingredientes": ["tapioca_seca:20", "ovo_inteiro:100", "queijo_cottage:50", "mamao_papaia:100", "chia:5"]},
        ],
        
        "almoco": [
            {"id": "almoco_padrao_frango", "type": "base", "nome_template": "Almoço com Frango", "ingredientes": ["peito_frango_grelhado_sem_pele:120", "arroz_branco_cozido:60", "feijao_carioca_cozido:80", "azeite_extra_virgem:5", "legumes_variados:120"]},
            {"id": "almoco_padrao_carne", "type": "base", "nome_template": "Almoço com Carne", "ingredientes": ["patinho_moido_95_5:120", "arroz_branco_cozido:60", "feijao_carioca_cozido:80", "azeite_extra_virgem:5", "legumes_variados:120"]},
            {"id": "almoco_padrao_peixe", "type": "base", "nome_template": "Almoço com Peixe", "ingredientes": ["tilapia_assada:150", "batata_doce_cozida:120", "feijao_carioca_cozido:80", "azeite_extra_virgem:5", "legumes_variados:120"]},
        ],
        
        "lanche": [
            {"id": "panqueca_proteica", "type": "receita", "nome_template": "Panqueca Proteica de Banana", 
             "ingredientes": ["banana:60", "ovo_inteiro:50", "whey_protein_isolado_hidrolisado:25", "cacau_po_100:5", "canela_po:2", "psyllium:5"],
             "modo_preparo": "Bater todos os ingredientes e assar em frigideira antiaderente"},
            
            {"id": "crepioca_proteica", "type": "receita", "nome_template": "Crepioca com Requeijão", 
             "ingredientes": ["tapioca_seca:20", "ovo_inteiro:50", "clara_ovo_pasteurizada:68", "requeijao_light:20"],
             "modo_preparo": "Misturar tapioca e ovos, grelhar em frigideira antiaderente, rechear com requeijão"},
            
            {"id": "iogurte_turbinado", "type": "base", "nome_template": "Iogurte com Whey e Frutas", 
             "ingredientes": ["iogurte_desnatado_zero:150", "whey_protein_isolado_hidrolisado:30", "morango:100", "chia:5"],
             "modo_preparo": "Misturar todos os ingredientes e deixar a chia hidratar por 5 minutos"},
            
            {"id": "omelete_completo", "type": "receita", "nome_template": "Omelete com Queijo e Legumes", 
             "ingredientes": ["ovo_inteiro:100", "clara_ovo_pasteurizada:68", "mussarela_light:30", "legumes_variados:50"],
             "modo_preparo": "Bater os ovos, acrescentar legumes picados finos, cozinhar em frigideira antiaderente"},
            
            {"id": "sanduiche_proteico", "type": "base", "nome_template": "Sanduíche de Frango", 
             "ingredientes": ["pao_forma_integral:50", "peito_frango_grelhado_sem_pele:80", "requeijao_light:20"],
             "modo_preparo": "Grelhar o frango temperado com ervas, montar o sanduíche com requeijão light"},
        ],
        
        "jantar": [
            {"id": "refeicao_padrao_peixe", "type": "base", "nome_template": "Tilápia com Arroz e Legumes", 
             "ingredientes": ["tilapia_assada:150", "arroz_branco_cozido:60", "legumes_variados:120", "azeite_extra_virgem:5"],
             "modo_preparo": "Grelhar o peixe com limão e ervas, servir com arroz e legumes ao vapor"},
            
            {"id": "refeicao_padrao_frango", "type": "base", "nome_template": "Frango com Batata Doce", 
             "ingredientes": ["peito_frango_grelhado_sem_pele:120", "batata_doce_cozida:120", "legumes_variados:120"],
             "modo_preparo": "Grelhar o frango temperado com ervas, servir com batata doce cozida e legumes"},
            
            {"id": "strogonoff_light", "type": "receita", "nome_template": "Strogonoff Light de Carne", 
             "ingredientes": ["file_mignon:100", "creme_leite_light:40", "ketchup_zero:10", "mostarda:5", "champignon:50", "arroz_branco_cozido:75"],
             "modo_preparo": "Refogar a carne em cubos, adicionar champignon, finalizar com creme de leite light e temperos"},
            
            {"id": "hamburguer_artesanal", "type": "receita", "nome_template": "Hambúrguer Artesanal Controlado", 
             "ingredientes": ["pao_hamburguer_light:50", "patinho_moido_95_5:120", "mussarela_light:20", "ketchup_zero:10"],
             "modo_preparo": "Temperar a carne moída com cebola e ervas, grelhar e montar o hambúrguer"},
            
            {"id": "pizza_fake", "type": "receita", "nome_template": "Pizza Fake de Rap10", 
             "ingredientes": ["rap10_integral:35", "peito_frango_grelhado_sem_pele:80", "mussarela_light:30", "molho_tomate_caseiro:20", "tomate_cereja:30", "oregano:2"],
             "modo_preparo": "Aquecer o rap10, cobrir com molho, frango desfiado, queijo e tomate, finalizar com orégano"},
            
            {"id": "salpicao_light", "type": "receita", "nome_template": "Salpicão Light", 
             "ingredientes": ["peito_frango_grelhado_sem_pele:100", "rap10_integral:35", "legumes_variados:50", "requeijao_light:20"],
             "modo_preparo": "Desfiar o frango, misturar com legumes cozidos em cubos e requeijão, servir com rap10"},
        ],
        
        "ceia": [
            {"id": "ceia_padrao", "type": "base", "nome_template": "Ceia Proteica", 
             "ingredientes": ["iogurte_desnatado_zero:100", "whey_protein_isolado_hidrolisado:15", "morango:75", "chia:5"],
             "modo_preparo": "Misturar todos os ingredientes e deixar a chia hidratar por 5 minutos"},
            
            {"id": "ceia_frutas", "type": "base", "nome_template": "Ceia com Frutas", 
             "ingredientes": ["iogurte_desnatado_zero:150", "whey_protein_isolado_hidrolisado:20", "banana:50"],
             "modo_preparo": "Bater o iogurte com whey e adicionar a fruta picada"}
        ]
    }

def get_substitution_rules():
    """ Regras de substituição detalhadas e padronizadas. """
    return {
        # PROTEÍNAS
        "peito_frango_grelhado_sem_pele": {
            "opcoes": [
                {"item": "patinho_moido_95_5", "qtd_g": 120, "obs": "Magro, preferir 95% carne / 5% gordura"},
                {"item": "tilapia_assada", "qtd_g": 150, "obs": "Grelhar apenas com limão e ervas"},
                {"item": "ovo_inteiro", "qtd_g": 150, "obs": "3 unidades médias"},
                {"item": "file_mignon", "qtd_g": 120, "obs": "Remover gordura aparente"},
                {"item": "atum_enlatado_agua", "qtd_g": 120, "obs": "Em água, bem escorrido"}
            ],
            "categoria": "proteina",
            "instrucao": "Escolher apenas uma opção por refeição"
        },
        
        # CARBOIDRATOS
        "arroz_branco_cozido": {
            "opcoes": [
                {"item": "batata_doce_cozida", "qtd_g": 120, "obs": "Sem adição de gordura"},
                {"item": "batata_inglesa_cozida", "qtd_g": 120, "obs": "Sem adição de gordura"},
                {"item": "arroz_integral_cozido", "qtd_g": 60, "obs": "Mais rico em fibras"},
                {"item": "macarrao_integral_cozido", "qtd_g": 60, "obs": "Al dente"},
                {"item": "aipim_macaxeira_cozido", "qtd_g": 100, "obs": "Sem adição de gordura"},
                {"item": "inhame_cozido", "qtd_g": 100, "obs": "Sem adição de gordura"}
            ],
            "categoria": "carboidrato",
            "instrucao": "Manter proporção similar de carboidratos"
        },
        
        # LEGUMINOSAS
        "feijao_carioca_cozido": {
            "opcoes": [
                {"item": "feijao_preto_cozido", "qtd_g": 80, "obs": "1 concha média"},
                {"item": "lentilha_cozida", "qtd_g": 80, "obs": "Rica em ferro"},
                {"item": "grao_de_bico_cozido", "qtd_g": 80, "obs": "Rico em fibras e proteínas"},
                {"item": "ervilha_cozida", "qtd_g": 80, "obs": "Fresca ou congelada"}
            ],
            "categoria": "leguminosa",
            "instrucao": "Manter volume similar na refeição"
        },
        
        # LATICÍNIOS
        "iogurte_desnatado_zero": {
            "opcoes": [
                {"item": "queijo_cottage", "qtd_g": 50, "obs": "Baixa gordura"},
                {"item": "ricota_fresca", "qtd_g": 50, "obs": "Baixo teor de gordura"},
                {"item": "leite_desnatado", "qtd_g": 200, "obs": "Baixo teor de gordura"}
            ],
            "categoria": "laticinio",
            "instrucao": "Escolher apenas uma opção por refeição"
        },
        
        # FRUTAS
        "banana": {
            "opcoes": [
                {"item": "maca", "qtd_g": 120, "obs": "1 unidade média"},
                {"item": "mamao_papaia", "qtd_g": 150, "obs": "Boa digestibilidade"},
                {"item": "morango", "qtd_g": 100, "obs": "Rico em antioxidantes"},
                {"item": "kiwi", "qtd_g": 100, "obs": "2 unidades pequenas"}
            ],
            "categoria": "fruta",
            "instrucao": "Preferir frutas frescas e da estação"
        }
    }

def get_static_info():
    """ Informações estáticas e orientações nutricionais detalhadas. """
    return {
        "legumes_variados": {
            "descricao": "Podem incluir: Tomate, Berinjela, Alho Poró, Brócolis, Rabanete, Chuchu, Couve, Beterraba, Pepino, Couve-Flor, Abobrinha, Repolho, Palmito, Quiabo, Cenoura, Vagem.",
            "instrucao": "Sempre preferir legumes da estação, orgânicos quando possível. Consumir preferencialmente cozidos no vapor ou grelhados para melhor digestibilidade e aproveitamento dos nutrientes.",
            "beneficios": "Ricos em vitaminas, minerais, antioxidantes e fibras. Ajudam na saciedade, saúde intestinal e fortalecimento do sistema imunológico."
        },
        
        "orientacao_refeicao_livre": {
            "descricao": "Nos fins de semana, é permitida 1 refeição livre e controlada.",
            "exemplos": [
                "1 hambúrguer artesanal + sobremesa pequena",
                "2-3 fatias de pizza + salada",
                "1 combinado de 20 peças de comida japonesa",
                "1 prato de massa com molho caseiro + 1 taça de vinho"
            ],
            "instrucao": "Mesmo na refeição livre, respeitar a sensação de saciedade e evitar excessos. Beber muita água durante o dia e retornar ao plano imediatamente após a refeição livre."
        },
        
        "orientacoes_gerais": {
            "hidratacao": "Consumir no mínimo 35ml de água por kg de peso corporal diariamente. Exemplo: para 70kg, ingerir 2,45 litros de água ao longo do dia.",
            "treino": "Realizar a refeição pós-treino em até 40 minutos após o término do exercício para melhor recuperação muscular.",
            "suplementos": "Whey Protein: consumir conforme recomendado no plano. Creatina (opcional): 5g diários, preferencialmente após o treino.",
            "alimentos_evitar": "Açúcar refinado, farinhas refinadas, alimentos ultraprocessados, frituras, embutidos, refrigerantes e bebidas alcoólicas em excesso."
        },
        
        "gramatura_padrao_grupos": {
            "proteinas": {
                "carne_vermelha": "120g por porção",
                "frango": "120g por porção",
                "peixe": "150g por porção",
                "ovos": "100g (2 unidades) por porção"
            },
            "carboidratos": {
                "arroz": "60g por porção",
                "batatas": "120g por porção",
                "massas": "60g por porção"
            },
            "gorduras": {
                "azeite": "5g (1 colher de chá) por porção",
                "oleaginosas": "30g por porção"
            }
        },
        
        "validacao_nutricional": {
            "proteina_por_kg": "Entre 1.8g e 2.5g por kg de peso corporal para praticantes de musculação",
            "distribuicao_carboidratos": "Maior concentração nas refeições pré e pós-treino",
            "gorduras_essenciais": "Incluir fontes de ômega-3 (peixes gordos, chia, linhaça) pelo menos 3x por semana",
            "fibras": "Mínimo de 25g diários para mulheres e 30g para homens"
        }
    }

# Função de validação de integridade dos dados
def validate_food_data():
    """Verifica e corrige possíveis inconsistências nos dados de alimentos."""
    foods = get_food_data()
    errors = []
    warnings = []
    
    for food_id, food_data in foods.items():
        # Verificações obrigatórias
        if 'kcal' not in food_data:
            errors.append(f"Alimento {food_id} não possui valor calórico!")
        
        if 'p' not in food_data or 'c' not in food_data or 'g' not in food_data:
            errors.append(f"Alimento {food_id} não possui todos os macronutrientes!")
        
        # Validação de consistência calórica
        calc_kcal = (food_data.get('p', 0) * 4) + (food_data.get('c', 0) * 4) + (food_data.get('g', 0) * 9)
        if abs(calc_kcal - food_data.get('kcal', 0)) > 0.5:
            warnings.append(f"Alimento {food_id} possui inconsistência calórica. Calculado: {calc_kcal:.2f}, Informado: {food_data.get('kcal', 0):.2f}")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    }
