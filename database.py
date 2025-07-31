# database.py - VERSÃO COMPLETA E DEFINITIVA
def get_food_data():
   """Base de dados nutricional completa com valores por grama."""
   return {
       # PROTEÍNAS PRINCIPAIS - VALORES CORRIGIDOS
       "peito_frango_grelhado_sem_pele": {"kcal": 1.65, "p": 0.31, "c": 0, "g": 0.036, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Grelhado sem gordura"},
       "clara_ovo_pasteurizada": {"kcal": 0.52, "p": 0.11, "c": 0.007, "g": 0.002, "f": 0, "categoria": "proteina", "unidade_comum": "ml", "obs": "1 clara = 33g"},
       "whey_protein_isolado_hidrolisado": {"kcal": 3.68, "p": 0.9, "c": 0.02, "g": 0.01, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Diluir em água"},
       "tilapia_assada": {"kcal": 1.28, "p": 0.26, "c": 0, "g": 0.026, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Temperar com limão"},
       "patinho_moido_95_5": {"kcal": 1.5, "p": 0.22, "c": 0, "g": 0.06, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "95% carne/5% gordura"},
       "file_mignon": {"kcal": 1.95, "p": 0.22, "c": 0, "g": 0.11, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Sem gordura aparente"},
       "salmao_grelhado": {"kcal": 2.08, "p": 0.22, "c": 0, "g": 0.13, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Rico em Ômega 3"},
       "atum_enlatado_agua": {"kcal": 1.16, "p": 0.26, "c": 0, "g": 0.01, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Em água, escorrido"},
       "peixe_branco_qualquer": {"kcal": 1.05, "p": 0.23, "c": 0, "g": 0.01, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Badejo, linguado, pescada"},
       "file_suino_magro": {"kcal": 1.43, "p": 0.21, "c": 0, "g": 0.065, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Sem gordura aparente"},
       
       # OVOS - VALORES PADRONIZADOS
       "ovo_inteiro": {"kcal": 1.43, "p": 0.125, "c": 0.01, "g": 0.095, "f": 0, "categoria": "proteina", "unidade_comum": "unidade", "obs": "1 unidade = 50g"},
       "gema_ovo": {"kcal": 3.22, "p": 0.158, "c": 0.036, "g": 0.269, "f": 0, "categoria": "gordura", "unidade_comum": "unidade", "obs": "1 gema = 17g"},
       "clara_ovo": {"kcal": 0.52, "p": 0.11, "c": 0.007, "g": 0.002, "f": 0, "categoria": "proteina", "unidade_comum": "unidade", "obs": "1 clara = 33g"},
       
       # CARBOIDRATOS - VALORES PRECISOS
       "arroz_branco_cozido": {"kcal": 1.3, "p": 0.025, "c": 0.28, "g": 0.003, "f": 0.002, "categoria": "carboidrato", "unidade_comum": "g", "obs": "4 col sopa = 100g"},
       "arroz_integral_cozido": {"kcal": 1.13, "p": 0.026, "c": 0.23, "g": 0.01, "f": 0.025, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Rico em fibras"},
       "batata_doce_cozida": {"kcal": 0.86, "p": 0.016, "c": 0.2, "g": 0.001, "f": 0.03, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Com casca"},
       "batata_inglesa_cozida": {"kcal": 0.87, "p": 0.02, "c": 0.2, "g": 0.001, "f": 0.016, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Sem gordura"},
       "macarrao_integral_cozido": {"kcal": 1.24, "p": 0.05, "c": 0.25, "g": 0.005, "f": 0.025, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Al dente"},
       "aipim_macaxeira_cozido": {"kcal": 1.25, "p": 0.01, "c": 0.3, "g": 0.001, "f": 0.018, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Sem gordura"},
       "inhame_cozido": {"kcal": 0.97, "p": 0.02, "c": 0.23, "g": 0.001, "f": 0.017, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Sem gordura"},
       "abobora_japonesa_cozida": {"kcal": 0.4, "p": 0.012, "c": 0.1, "g": 0.001, "f": 0.017, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Rica em vitamina A"},
       
       # PÃES - VALORES CORRIGIDOS
       "pao_forma_integral": {"kcal": 2.5, "p": 0.13, "c": 0.41, "g": 0.04, "f": 0.06, "categoria": "carboidrato", "unidade_comum": "fatia", "obs": "1 fatia = 25g"},
       "pao_frances": {"kcal": 3.0, "p": 0.08, "c": 0.58, "g": 0.03, "f": 0.015, "categoria": "carboidrato", "unidade_comum": "unidade", "obs": "1 unidade = 50g"},
       "pao_hamburguer_light": {"kcal": 3.906, "p": 0.104, "c": 0.7, "g": 0.06, "f": 0.038, "categoria": "carboidrato", "unidade_comum": "unidade", "obs": "1 unidade = 50g"},
       "pao_integral": {"kcal": 2.6, "p": 0.12, "c": 0.48, "g": 0.04, "f": 0.05, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Integral verdadeiro"},
       "rap10_integral": {"kcal": 3.257, "p": 0.091, "c": 0.6, "g": 0.06, "f": 0.057, "categoria": "carboidrato", "unidade_comum": "unidade", "obs": "1 unidade = 35g"},
       "tapioca_seca": {"kcal": 3.41, "p": 0, "c": 0.85, "g": 0, "f": 0.002, "categoria": "carboidrato", "unidade_comum": "g", "obs": "2 col sopa = 20g"},
       "aveia_flocos": {"kcal": 3.94, "p": 0.17, "c": 0.66, "g": 0.07, "f": 0.11, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Rica em beta-glucana"},
       
       # LEGUMINOSAS - VALORES PRECISOS
       "feijao_carioca_cozido": {"kcal": 1.15, "p": 0.057, "c": 0.207, "g": 0.005, "f": 0.08, "categoria": "carboidrato", "unidade_comum": "g", "obs": "1 concha = 80g"},
       "feijao_preto_cozido": {"kcal": 1.15, "p": 0.059, "c": 0.204, "g": 0.005, "f": 0.085, "categoria": "carboidrato", "unidade_comum": "g", "obs": "1 concha = 80g"},
       "lentilha_cozida": {"kcal": 1.16, "p": 0.09, "c": 0.2, "g": 0.004, "f": 0.079, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Rica em ferro"},
       "grao_de_bico_cozido": {"kcal": 1.64, "p": 0.088, "c": 0.273, "g": 0.026, "f": 0.06, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Al dente"},
       "ervilha_cozida": {"kcal": 0.81, "p": 0.052, "c": 0.143, "g": 0.004, "f": 0.054, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Fresca ou congelada"},
       "milho_cozido": {"kcal": 1.32, "p": 0.035, "c": 0.289, "g": 0.015, "f": 0.024, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Sem manteiga"},
       
       # LATICÍNIOS - VALORES ATUALIZADOS
       "requeijao_light": {"kcal": 1.88, "p": 0.1, "c": 0.04, "g": 0.15, "f": 0, "categoria": "gordura", "unidade_comum": "g", "obs": "Versão light"},
       "requeijao_danubio_light": {"kcal": 1.88, "p": 0.1, "c": 0.04, "g": 0.15, "f": 0, "categoria": "laticinio", "unidade_comum": "g", "obs": "Light"},
       "queijo_cottage": {"kcal": 0.98, "p": 0.11, "c": 0.034, "g": 0.043, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Baixa gordura"},
       "queijo_minas_light": {"kcal": 2.4, "p": 0.17, "c": 0.03, "g": 0.18, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Versão light"},
       "queijo_minas_frescal": {"kcal": 2.64, "p": 0.177, "c": 0.032, "g": 0.205, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Frescal tradicional"},
       "ricota_fresca": {"kcal": 1.74, "p": 0.124, "c": 0.032, "g": 0.127, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Baixo sódio"},
       "iogurte_desnatado_zero": {"kcal": 0.37, "p": 0.042, "c": 0.068, "g": 0, "f": 0.005, "categoria": "proteina", "unidade_comum": "g", "obs": "Sem açúcar"},
       "iogurte_natural_desnatado": {"kcal": 0.418, "p": 0.047, "c": 0.057, "g": 0.002, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Natural"},
       "iogurte_natural": {"kcal": 0.55, "p": 0.04, "c": 0.075, "g": 0.015, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Natural"},
       "iogurte_natural_integral": {"kcal": 0.61, "p": 0.035, "c": 0.047, "g": 0.033, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Integral"},
       "iogurte_zero_lactose": {"kcal": 0.4, "p": 0.04, "c": 0.06, "g": 0.002, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Sem lactose"},
       "leite_desnatado": {"kcal": 0.35, "p": 0.034, "c": 0.049, "g": 0.001, "f": 0, "categoria": "proteina", "unidade_comum": "ml", "obs": "0% gordura"},
       "mussarela_light": {"kcal": 2.5, "p": 0.22, "c": 0.03, "g": 0.16, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Versão light"},
       "queijo_mussarela_light": {"kcal": 2.81, "p": 0.27, "c": 0.03, "g": 0.18, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Light"},
       "queijo_mussarela": {"kcal": 2.81, "p": 0.27, "c": 0.03, "g": 0.18, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Light"},
       "queijo_mussarela_sem_lactose": {"kcal": 3.91, "p": 0.25, "c": 0.01, "g": 0.32, "f": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Sem lactose"},
       
       # OLEAGINOSAS - VALORES CORRIGIDOS
       "castanha_do_para": {"kcal": 6.56, "p": 0.143, "c": 0.125, "g": 0.663, "f": 0.075, "categoria": "gordura", "unidade_comum": "unidade", "obs": "1 unidade = 5g"},
       "castanhas_do_para": {"kcal": 6.56, "p": 0.143, "c": 0.125, "g": 0.663, "f": 0.075, "categoria": "gordura", "unidade_comum": "g", "obs": "Rica em selênio"},
       "amendoim": {"kcal": 5.67, "p": 0.258, "c": 0.162, "g": 0.492, "f": 0.08, "categoria": "gordura", "unidade_comum": "g", "obs": "Sem sal"},
       "amendoa": {"kcal": 5.79, "p": 0.212, "c": 0.216, "g": 0.494, "f": 0.122, "categoria": "gordura", "unidade_comum": "unidade", "obs": "1 unidade = 1.2g"},
       "castanha_de_caju": {"kcal": 5.53, "p": 0.182, "c": 0.303, "g": 0.436, "f": 0.033, "categoria": "gordura", "unidade_comum": "g", "obs": "Sem sal"},
       "castanhas": {"kcal": 6.0, "p": 0.15, "c": 0.15, "g": 0.5, "f": 0.07, "categoria": "gordura", "unidade_comum": "g", "obs": "Mix variado"},
       "pasta_amendoim_integral": {"kcal": 5.88, "p": 0.25, "c": 0.2, "g": 0.5, "f": 0.06, "categoria": "gordura", "unidade_comum": "g", "obs": "100% amendoim"},
       "pasta_de_amendoim": {"kcal": 5.88, "p": 0.25, "c": 0.2, "g": 0.5, "f": 0.06, "categoria": "gordura", "unidade_comum": "g", "obs": "Sem açúcar"},
       
       # SEMENTES - VALORES PRECISOS
       "chia": {"kcal": 3.866, "p": 0.167, "c": 0.078, "g": 0.308, "f": 0.344, "categoria": "gordura", "unidade_comum": "g", "obs": "Hidratar antes"},
       "chia_em_graos": {"kcal": 3.866, "p": 0.167, "c": 0.078, "g": 0.308, "f": 0.344, "categoria": "gordura", "unidade_comum": "g", "obs": "Omega 3"},
       "linhaca_moida": {"kcal": 5.34, "p": 0.183, "c": 0.289, "g": 0.423, "f": 0.273, "categoria": "gordura", "unidade_comum": "g", "obs": "Moer na hora"},
       "psyllium": {"kcal": 0.7, "p": 0.015, "c": 0.016, "g": 0.006, "f": 0.8, "categoria": "fibra", "unidade_comum": "g", "obs": "Fibra solúvel"},
       "semente_abobora": {"kcal": 5.59, "p": 0.305, "c": 0.109, "g": 0.491, "f": 0.061, "categoria": "gordura", "unidade_comum": "g", "obs": "Rica em zinco"},
       "semente_girassol": {"kcal": 5.84, "p": 0.209, "c": 0.2, "g": 0.514, "f": 0.086, "categoria": "gordura", "unidade_comum": "g", "obs": "Sem sal"},
       
       # FRUTAS - VALORES ATUALIZADOS
       "banana": {"kcal": 0.92, "p": 0.011, "c": 0.229, "g": 0.003, "f": 0.026, "categoria": "fruta", "unidade_comum": "unidade", "obs": "1 média = 100g"},
       "banana_prata": {"kcal": 0.89, "p": 0.013, "c": 0.22, "g": 0.001, "f": 0.02, "categoria": "fruta", "unidade_comum": "g", "obs": "Prata"},
       "maca": {"kcal": 0.52, "p": 0.003, "c": 0.138, "g": 0.002, "f": 0.024, "categoria": "fruta", "unidade_comum": "unidade", "obs": "1 média = 150g"},
       "mamao_papaia": {"kcal": 0.39, "p": 0.005, "c": 0.102, "g": 0.001, "f": 0.018, "categoria": "fruta", "unidade_comum": "g", "obs": "Digestivo"},
       "mamao": {"kcal": 0.39, "p": 0.005, "c": 0.102, "g": 0.001, "f": 0.018, "categoria": "fruta", "unidade_comum": "g", "obs": "Papaia"},
       "morango": {"kcal": 0.3, "p": 0.007, "c": 0.077, "g": 0.003, "f": 0.02, "categoria": "fruta", "unidade_comum": "g", "obs": "Antioxidante"},
       "morangos": {"kcal": 0.3, "p": 0.007, "c": 0.077, "g": 0.003, "f": 0.02, "categoria": "fruta", "unidade_comum": "g", "obs": "Vitamina C"},
       "melao": {"kcal": 0.36, "p": 0.008, "c": 0.091, "g": 0.002, "f": 0.008, "categoria": "fruta", "unidade_comum": "g", "obs": "Hidratante"},
       "frutas_vermelhas": {"kcal": 0.4, "p": 0.01, "c": 0.09, "g": 0.004, "f": 0.038, "categoria": "fruta", "unidade_comum": "g", "obs": "Mix berries"},
       "abacaxi": {"kcal": 0.5, "p": 0.005, "c": 0.131, "g": 0.001, "f": 0.014, "categoria": "fruta", "unidade_comum": "g", "obs": "Bromelina"},
       "laranja_pera": {"kcal": 0.47, "p": 0.009, "c": 0.118, "g": 0.001, "f": 0.024, "categoria": "fruta", "unidade_comum": "unidade", "obs": "1 média = 130g"},
       "kiwi": {"kcal": 0.61, "p": 0.011, "c": 0.147, "g": 0.005, "f": 0.03, "categoria": "fruta", "unidade_comum": "unidade", "obs": "1 unidade = 76g"},
       "uva": {"kcal": 0.69, "p": 0.007, "c": 0.171, "g": 0.002, "f": 0.009, "categoria": "fruta", "unidade_comum": "g", "obs": "Sem semente"},
       "manga": {"kcal": 0.6, "p": 0.008, "c": 0.15, "g": 0.004, "f": 0.018, "categoria": "fruta", "unidade_comum": "g", "obs": "Tommy ou Palmer"},
       "goiaba": {"kcal": 0.68, "p": 0.026, "c": 0.143, "g": 0.01, "f": 0.054, "categoria": "fruta", "unidade_comum": "g", "obs": "Rica em vitamina C"},
       "frutas": {"kcal": 0.48, "p": 0.01, "c": 0.12, "g": 0.002, "f": 0.02, "categoria": "fruta", "unidade_comum": "g", "obs": "Mix variado"},
       "fruta": {"kcal": 0.48, "p": 0.01, "c": 0.12, "g": 0.002, "f": 0.02, "categoria": "fruta", "unidade_comum": "g", "obs": "Genérica"},
       
       # VEGETAIS - VALORES PRECISOS
       "legumes_variados": {"kcal": 0.25, "p": 0.02, "c": 0.05, "g": 0.001, "f": 0.02, "categoria": "vegetal", "unidade_comum": "g", "obs": "Mix de legumes"},
       "salada_crua": {"kcal": 0.108, "p": 0.01, "c": 0.02, "g": 0.001, "f": 0.015, "categoria": "vegetal", "unidade_comum": "g", "obs": "Mix de folhas"},
       "alface": {"kcal": 0.15, "p": 0.014, "c": 0.029, "g": 0.002, "f": 0.013, "categoria": "vegetal", "unidade_comum": "g", "obs": "Crespa ou lisa"},
       "tomate": {"kcal": 0.18, "p": 0.009, "c": 0.039, "g": 0.002, "f": 0.012, "categoria": "vegetal", "unidade_comum": "g", "obs": "Maduro"},
       "tomate_cereja": {"kcal": 0.21, "p": 0.009, "c": 0.039, "g": 0.002, "f": 0.012, "categoria": "vegetal", "unidade_comum": "unidade", "obs": "1 unidade = 10g"},
       "cenoura": {"kcal": 0.41, "p": 0.009, "c": 0.096, "g": 0.002, "f": 0.028, "categoria": "vegetal", "unidade_comum": "g", "obs": "Crua ou cozida"},
       "brocolis": {"kcal": 0.34, "p": 0.028, "c": 0.066, "g": 0.004, "f": 0.026, "categoria": "vegetal", "unidade_comum": "g", "obs": "Cozido"},
       "couve_flor": {"kcal": 0.25, "p": 0.019, "c": 0.05, "g": 0.003, "f": 0.02, "categoria": "vegetal", "unidade_comum": "g", "obs": "Cozida"},
       "abobrinha": {"kcal": 0.17, "p": 0.012, "c": 0.031, "g": 0.003, "f": 0.01, "categoria": "vegetal", "unidade_comum": "g", "obs": "Cozida"},
       "berinjela": {"kcal": 0.25, "p": 0.01, "c": 0.059, "g": 0.002, "f": 0.03, "categoria": "vegetal", "unidade_comum": "g", "obs": "Cozida"},
       "pimentao": {"kcal": 0.31, "p": 0.01, "c": 0.06, "g": 0.003, "f": 0.017, "categoria": "vegetal", "unidade_comum": "g", "obs": "Vermelho ou verde"},
       "pepino": {"kcal": 0.16, "p": 0.007, "c": 0.036, "g": 0.001, "f": 0.005, "categoria": "vegetal", "unidade_comum": "g", "obs": "Com casca"},
       "chuchu": {"kcal": 0.19, "p": 0.008, "c": 0.045, "g": 0.001, "f": 0.005, "categoria": "vegetal", "unidade_comum": "g", "obs": "Cozido"},
       "repolho": {"kcal": 0.25, "p": 0.013, "c": 0.058, "g": 0.001, "f": 0.025, "categoria": "vegetal", "unidade_comum": "g", "obs": "Cru ou cozido"},
       "couve": {"kcal": 0.49, "p": 0.043, "c": 0.089, "g": 0.007, "f": 0.04, "categoria": "vegetal", "unidade_comum": "g", "obs": "Refogada"},
       "espinafre": {"kcal": 0.23, "p": 0.029, "c": 0.036, "g": 0.004, "f": 0.022, "categoria": "vegetal", "unidade_comum": "g", "obs": "Cozido"},
       "vagem": {"kcal": 0.31, "p": 0.018, "c": 0.07, "g": 0.002, "f": 0.027, "categoria": "vegetal", "unidade_comum": "g", "obs": "Cozida"},
       "quiabo": {"kcal": 0.33, "p": 0.019, "c": 0.074, "g": 0.002, "f": 0.032, "categoria": "vegetal", "unidade_comum": "g", "obs": "Cozido"},
       "palmito": {"kcal": 0.25, "p": 0.026, "c": 0.047, "g": 0.005, "f": 0.017, "categoria": "vegetal", "unidade_comum": "g", "obs": "Em conserva"},
       "champignon": {"kcal": 0.25, "p": 0.031, "c": 0.033, "g": 0.003, "f": 0.01, "categoria": "vegetal", "unidade_comum": "g", "obs": "Cogumelo paris"},
       
       # GORDURAS - VALORES PRECISOS
       "azeite_oliva_extra_virgem": {"kcal": 8.666, "p": 0, "c": 0, "g": 0.96, "f": 0, "categoria": "gordura", "unidade_comum": "ml", "obs": "1ml = 0.92g"},
       "oleo_coco": {"kcal": 9.0, "p": 0, "c": 0, "g": 1.0, "f": 0, "categoria": "gordura", "unidade_comum": "g", "obs": "Extra virgem"},
       "manteiga": {"kcal": 7.17, "p": 0.009, "c": 0.001, "g": 0.811, "f": 0, "categoria": "gordura", "unidade_comum": "g", "obs": "Com sal"},
       "margarina_light": {"kcal": 3.7, "p": 0, "c": 0, "g": 0.41, "f": 0, "categoria": "gordura", "unidade_comum": "g", "obs": "Light"},
       
       # DOCES E OUTROS - VALORES PRECISOS
       "mel": {"kcal": 3.04, "p": 0.003, "c": 0.824, "g": 0, "f": 0.002, "categoria": "carboidrato", "unidade_comum": "g", "obs": "1 col sopa = 20g"},
       "geleia_diet": {"kcal": 0.45, "p": 0.002, "c": 0.11, "g": 0, "f": 0.002, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Sem açúcar"},
       "chocolate_70": {"kcal": 5.46, "p": 0.075, "c": 0.46, "g": 0.38, "f": 0.07, "categoria": "gordura", "unidade_comum": "g", "obs": "70% cacau"},
       "cacau_po": {"kcal": 2.8, "p": 0.2, "c": 0.58, "g": 0.14, "f": 0.33, "categoria": "tempero", "unidade_comum": "g", "obs": "100% cacau"},
       "canela_po": {"kcal": 2.61, "p": 0.04, "c": 0.81, "g": 0.03, "f": 0.53, "categoria": "tempero", "unidade_comum": "g", "obs": "Em pó"},
       "gelatina_diet": {"kcal": 0.1, "p": 0.02, "c": 0.001, "g": 0, "f": 0, "categoria": "sobremesa", "unidade_comum": "g", "obs": "1 unidade = 110g"},
       
       # TEMPEROS E MOLHOS
       "sal": {"kcal": 0, "p": 0, "c": 0, "g": 0, "f": 0, "categoria": "tempero", "unidade_comum": "g", "obs": "Sódio"},
       "oregano": {"kcal": 3.06, "p": 0.11, "c": 0.64, "g": 0.1, "f": 0.11, "categoria": "tempero", "unidade_comum": "g", "obs": "1 punhado = 3g"},
       "molho_tomate": {"kcal": 0.32, "p": 0.014, "c": 0.07, "g": 0.002, "f": 0.018, "categoria": "molho", "unidade_comum": "g", "obs": "1 col sopa = 15g"},
       "ketchup": {"kcal": 1.0, "p": 0.01, "c": 0.25, "g": 0.001, "f": 0.003, "categoria": "molho", "unidade_comum": "g", "obs": "1 col sopa = 15g"},
       "mostarda": {"kcal": 0.78, "p": 0.04, "c": 0.06, "g": 0.04, "f": 0.02, "categoria": "molho", "unidade_comum": "g", "obs": "1 col chá = 5g"},
       "maionese_light": {"kcal": 3.0, "p": 0.01, "c": 0.1, "g": 0.28, "f": 0, "categoria": "molho", "unidade_comum": "g", "obs": "Light"},
       "vinagre": {"kcal": 0.19, "p": 0, "c": 0.009, "g": 0, "f": 0, "categoria": "tempero", "unidade_comum": "ml", "obs": "De maçã"},
       "shoyu_light": {"kcal": 0.53, "p": 0.08, "c": 0.08, "g": 0.01, "f": 0.01, "categoria": "molho", "unidade_comum": "ml", "obs": "Menos sódio"},
       
       # PRODUTOS ESPECIAIS
       "iogurte_proteico_yopro": {"kcal": 0.66, "p": 0.1, "c": 0.04, "g": 0.002, "f": 0, "categoria": "proteina", "unidade_comum": "ml", "obs": "1 unidade = 250ml"},
       "creme_leite_light": {"kcal": 1.161, "p": 0.025, "c": 0.04, "g": 0.1, "f": 0, "categoria": "laticinio", "unidade_comum": "g", "obs": "Light"},
       "doce_leite": {"kcal": 3.06, "p": 0.05, "c": 0.58, "g": 0.065, "f": 0, "categoria": "doce", "unidade_comum": "g", "obs": "1 col sopa = 20g"},
       
       # SUBSTITUTOS E ESPECIAIS
       "adocante_stevia": {"kcal": 0, "p": 0, "c": 0, "g": 0, "f": 0, "categoria": "adocante", "unidade_comum": "g", "obs": "Zero cal"},
       "adocante_sucralose": {"kcal": 0, "p": 0, "c": 0, "g": 0, "f": 0, "categoria": "adocante", "unidade_comum": "g", "obs": "Zero cal"},
       "sal_rosa": {"kcal": 0, "p": 0, "c": 0, "g": 0, "f": 0, "categoria": "tempero", "unidade_comum": "g", "obs": "Himalaia"},
       "pimenta_reino": {"kcal": 2.55, "p": 0.11, "c": 0.64, "g": 0.03, "f": 0.25, "categoria": "tempero", "unidade_comum": "g", "obs": "Moída"}
   }

def get_meal_templates():
   """Retorna templates de refeições modulares."""
   return {
       'cafe_manha': {
           'padrao': {
               'nome': 'Café da Manhã Padrão',
               'alimentos': [
                   {'nome': 'pao_forma_integral', 'qtd_base': 50},
                   {'nome': 'requeijao_light', 'qtd_base': 20},
                   {'nome': 'ovo_inteiro', 'qtd_base': 50},
                   {'nome': 'frutas', 'qtd_base': 100}
               ]
           }
       },
       'almoco': {
           'tradicional': {
               'nome': 'Almoço Tradicional',
               'alimentos': [
                   {'nome': 'peito_frango_grelhado_sem_pele', 'qtd_base': 120},
                   {'nome': 'arroz_branco_cozido', 'qtd_base': 60},
                   {'nome': 'feijao_carioca_cozido', 'qtd_base': 80},
                   {'nome': 'legumes_variados', 'qtd_base': 100},
                   {'nome': 'salada_crua', 'qtd_base': 50},
                   {'nome': 'azeite_oliva_extra_virgem', 'qtd_base': 5}
               ]
           }
       },
       'lanche': {
           'proteico': {
               'nome': 'Lanche Proteico',
               'alimentos': [
                   {'nome': 'whey_protein_isolado_hidrolisado', 'qtd_base': 30},
                   {'nome': 'frutas', 'qtd_base': 100}
               ]
           }
       },
       'jantar': {
           'leve': {
               'nome': 'Jantar Leve',
               'alimentos': [
                   {'nome': 'tilapia_assada', 'qtd_base': 150},
                   {'nome': 'legumes_variados', 'qtd_base': 150},
                   {'nome': 'salada_crua', 'qtd_base': 100},
                   {'nome': 'azeite_oliva_extra_virgem', 'qtd_base': 5}
               ]
           }
       },
       'ceia': {
           'leve': {
               'nome': 'Ceia Leve',
               'alimentos': [
                   {'nome': 'iogurte_natural_desnatado', 'qtd_base': 150},
                   {'nome': 'chia', 'qtd_base': 10}
               ]
           }
       }
   }

def get_substitution_rules():
   """Retorna regras de substituição por categoria."""
   return {
       'proteina_animal': {
           'alimentos': [
               'peito_frango_grelhado_sem_pele',
               'tilapia_assada',
               'patinho_moido_95_5',
               'file_mignon',
               'atum_enlatado_agua',
               'ovo_inteiro'
           ],
           'fator_conversao': 1.0
       },
       'carboidrato_complexo': {
           'alimentos': [
               'arroz_branco_cozido',
               'arroz_integral_cozido',
               'batata_doce_cozida',
               'batata_inglesa_cozida',
               'macarrao_integral_cozido',
               'aipim_macaxeira_cozido',
               'inhame_cozido'
           ],
           'fator_conversao': 1.0
       },
       'leguminosas': {
           'alimentos': [
               'feijao_carioca_cozido',
               'feijao_preto_cozido',
               'lentilha_cozida',
               'grao_de_bico_cozido',
               'ervilha_cozida'
           ],
           'fator_conversao': 1.0
       },
       'frutas': {
           'alimentos': [
               'banana',
               'maca',
               'mamao',
               'morango',
               'melao',
               'abacaxi',
               'laranja_pera',
               'manga',
               'uva'
           ],
           'fator_conversao': 1.0
       },
       'laticinios': {
           'alimentos': [
               'iogurte_natural_desnatado',
               'queijo_cottage',
               'queijo_minas_light',
               'requeijao_light'
           ],
           'fator_conversao': 1.0
       }
   }

def get_static_info():
   """Retorna informações estáticas do sistema."""
   return {
       'orientacoes': {
           'hidratacao': 'Beber no mínimo 35ml de água por kg de peso corporal',
           'mastigacao': 'Mastigar bem os alimentos, pelo menos 20 vezes',
           'horarios': 'Manter intervalos regulares entre as refeições (3-4 horas)',
           'preparo': 'Preferir preparações grelhadas, assadas ou cozidas'
       },
       'limites_seguros': {
           'proteina_min_g_kg': 0.8,
           'proteina_max_g_kg': 3.0,
           'carb_min_percent': 25,
           'carb_max_percent': 65,
           'gordura_min_percent': 15,
           'gordura_max_percent': 35,
           'fibra_min_g': 25,
           'fibra_max_g': 50
       },
       'conversoes': {
           'colher_sopa_ml': 15,
           'colher_cha_ml': 5,
           'xicara_ml': 240,
           'copo_ml': 200,
           'concha_ml': 80
       }
   }

def validate_food_data():
   """Valida integridade da base de dados."""
   foods = get_food_data()
   errors = []
   
   for name, data in foods.items():
       # Verifica campos obrigatórios
       required_fields = ['kcal', 'p', 'c', 'g', 'categoria']
       for field in required_fields:
           if field not in data:
               errors.append(f"{name}: faltando campo {field}")
       
       # Valida cálculo calórico
       calc_kcal = (data['p'] * 4) + (data['c'] * 4) + (data['g'] * 9)
       diff = abs(calc_kcal - data['kcal'])
       if diff > 0.5:  # Tolerância de 0.5 kcal
           errors.append(f"{name}: calorias não batem. Declarado: {data['kcal']}, Calculado: {calc_kcal:.2f}")
   
   return errors

# Se executado diretamente, valida a base
if __name__ == "__main__":
   errors = validate_food_data()
   if errors:
       print("Erros encontrados na base de dados:")
       for error in errors:
           print(f"  - {error}")
   else:
       print("Base de dados validada com sucesso!")
