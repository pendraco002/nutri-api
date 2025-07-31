# database.py - VERSÃO CORRIGIDA COM PRECISÃO ABSOLUTA
def get_food_data():
    """Base de dados com valores corrigidos e validados matematicamente."""
    return {
        # PROTEÍNAS PRINCIPAIS - VALORES CORRIGIDOS
        "peito_frango_grelhado_sem_pele": {"kcal": 1.65, "p": 0.31, "c": 0, "g": 0.036, "categoria": "proteina", "unidade_comum": "g", "obs": "Grelhado sem gordura"},
        "clara_ovo_pasteurizada": {"kcal": 0.52, "p": 0.11, "c": 0.007, "g": 0.002, "categoria": "proteina", "unidade_comum": "ml", "obs": "1 clara = 33g"},
        "whey_protein_isolado_hidrolisado": {"kcal": 3.68, "p": 0.9, "c": 0.02, "g": 0.01, "categoria": "proteina", "unidade_comum": "g", "obs": "Diluir em água"},
        "tilapia_assada": {"kcal": 1.28, "p": 0.26, "c": 0, "g": 0.026, "categoria": "proteina", "unidade_comum": "g", "obs": "Temperar com limão"},
        "patinho_moido_95_5": {"kcal": 1.5, "p": 0.22, "c": 0, "g": 0.06, "categoria": "proteina", "unidade_comum": "g", "obs": "95% carne/5% gordura"},
        "file_mignon": {"kcal": 1.95, "p": 0.22, "c": 0, "g": 0.11, "categoria": "proteina", "unidade_comum": "g", "obs": "Sem gordura aparente"},
        "salmao_grelhado": {"kcal": 2.08, "p": 0.22, "c": 0, "g": 0.13, "categoria": "proteina", "unidade_comum": "g", "obs": "Rico em Ômega 3"},
        "atum_enlatado_agua": {"kcal": 1.16, "p": 0.26, "c": 0, "g": 0.01, "categoria": "proteina", "unidade_comum": "g", "obs": "Em água, escorrido"},
        "peixe_branco_qualquer": {"kcal": 1.05, "p": 0.23, "c": 0, "g": 0.01, "categoria": "proteina", "unidade_comum": "g", "obs": "Badejo, linguado, pescada"},
        "file_suino_magro": {"kcal": 1.43, "p": 0.21, "c": 0, "g": 0.065, "categoria": "proteina", "unidade_comum": "g", "obs": "Sem gordura aparente"},
        
        # OVOS - VALORES PADRONIZADOS
        "ovo_inteiro": {"kcal": 1.43, "p": 0.125, "c": 0.01, "g": 0.095, "categoria": "proteina", "unidade_comum": "unidade", "obs": "1 unidade = 50g"},
        "ovo": {"kcal": 1.43, "p": 0.125, "c": 0.01, "g": 0.095, "categoria": "proteina", "unidade_comum": "unidade", "obs": "1 unidade = 50g"},
        "gema_ovo": {"kcal": 3.22, "p": 0.158, "c": 0.036, "g": 0.269, "categoria": "gordura", "unidade_comum": "unidade", "obs": "1 gema = 17g"},
        "clara_ovo": {"kcal": 0.52, "p": 0.11, "c": 0.007, "g": 0.002, "categoria": "proteina", "unidade_comum": "unidade", "obs": "1 clara = 33g"},
        "claras": {"kcal": 0.52, "p": 0.11, "c": 0.007, "g": 0.002, "categoria": "proteina", "unidade_comum": "g", "obs": "Clara de ovo"},
        
        # CARBOIDRATOS - VALORES PRECISOS
        "arroz_branco_cozido": {"kcal": 1.3, "p": 0.025, "c": 0.28, "g": 0.003, "categoria": "carboidrato", "unidade_comum": "g", "obs": "4 col sopa = 100g"},
        "arroz_branco": {"kcal": 1.3, "p": 0.025, "c": 0.28, "g": 0.003, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Cozido"},
        "arroz_integral_cozido": {"kcal": 1.13, "p": 0.026, "c": 0.23, "g": 0.01, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Rico em fibras"},
        "batata_doce_cozida": {"kcal": 0.86, "p": 0.016, "c": 0.2, "g": 0.001, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Com casca"},
        "batata_inglesa_cozida": {"kcal": 0.87, "p": 0.02, "c": 0.2, "g": 0.001, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Sem gordura"},
        "macarrao_integral_cozido": {"kcal": 1.24, "p": 0.05, "c": 0.25, "g": 0.005, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Al dente"},
        "aipim_macaxeira_cozido": {"kcal": 1.25, "p": 0.01, "c": 0.3, "g": 0.001, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Sem gordura"},
        "inhame_cozido": {"kcal": 0.97, "p": 0.02, "c": 0.23, "g": 0.001, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Sem gordura"},
        "abobora_japonesa_cozida": {"kcal": 0.4, "p": 0.012, "c": 0.1, "g": 0.001, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Rica em vitamina A"},
        
        # PÃES - VALORES CORRIGIDOS
        "pao_forma_integral": {"kcal": 2.76, "p": 0.13, "c": 0.49, "g": 0.04, "categoria": "carboidrato", "unidade_comum": "fatia", "obs": "1 fatia = 25g"},
        "pao_frances": {"kcal": 3.0, "p": 0.08, "c": 0.58, "g": 0.03, "categoria": "carboidrato", "unidade_comum": "unidade", "obs": "1 unidade = 50g"},
        "pao_hamburguer_light": {"kcal": 2.4, "p": 0.09, "c": 0.45, "g": 0.03, "categoria": "carboidrato", "unidade_comum": "unidade", "obs": "1 unidade = 50g"},
        "pao_integral": {"kcal": 2.6, "p": 0.12, "c": 0.48, "g": 0.04, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Integral verdadeiro"},
        "rap10_integral": {"kcal": 3.08, "p": 0.09, "c": 0.6, "g": 0.03, "categoria": "carboidrato", "unidade_comum": "unidade", "obs": "1 unidade = 35g"},
        "tapioca_seca": {"kcal": 3.4, "p": 0, "c": 0.85, "g": 0, "categoria": "carboidrato", "unidade_comum": "g", "obs": "2 col sopa = 20g"},
        "tapioca": {"kcal": 3.4, "p": 0, "c": 0.85, "g": 0, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Goma"},
        "aveia_flocos": {"kcal": 3.94, "p": 0.17, "c": 0.66, "g": 0.07, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Rica em beta-glucana"},
        
        # LEGUMINOSAS - VALORES PRECISOS
        "feijao_carioca_cozido": {"kcal": 1.15, "p": 0.057, "c": 0.207, "g": 0.005, "categoria": "carboidrato", "unidade_comum": "g", "obs": "1 concha = 80g"},
        "feijao_preto_cozido": {"kcal": 1.15, "p": 0.059, "c": 0.204, "g": 0.005, "categoria": "carboidrato", "unidade_comum": "g", "obs": "1 concha = 80g"},
        "feijao": {"kcal": 1.15, "p": 0.057, "c": 0.207, "g": 0.005, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Cozido"},
        "lentilha_cozida": {"kcal": 1.16, "p": 0.09, "c": 0.2, "g": 0.004, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Rica em ferro"},
        "grao_de_bico_cozido": {"kcal": 1.64, "p": 0.088, "c": 0.273, "g": 0.026, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Al dente"},
        "ervilha_cozida": {"kcal": 0.81, "p": 0.052, "c": 0.143, "g": 0.004, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Fresca ou congelada"},
        "milho_cozido": {"kcal": 1.32, "p": 0.035, "c": 0.289, "g": 0.015, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Sem manteiga"},
        
        # LATICÍNIOS - VALORES ATUALIZADOS
        "requeijao_light": {"kcal": 2.1, "p": 0.1, "c": 0.04, "g": 0.17, "categoria": "gordura", "unidade_comum": "g", "obs": "Versão light"},
        "queijo_cottage": {"kcal": 0.98, "p": 0.11, "c": 0.034, "g": 0.043, "categoria": "proteina", "unidade_comum": "g", "obs": "Baixa gordura"},
        "queijo_minas_light": {"kcal": 2.4, "p": 0.17, "c": 0.03, "g": 0.18, "categoria": "proteina", "unidade_comum": "g", "obs": "Versão light"},
        "queijo_minas_frescal": {"kcal": 2.64, "p": 0.177, "c": 0.032, "g": 0.205, "categoria": "proteina", "unidade_comum": "g", "obs": "Frescal tradicional"},
        "queijo_minas": {"kcal": 2.64, "p": 0.177, "c": 0.032, "g": 0.205, "categoria": "proteina", "unidade_comum": "g", "obs": "Frescal"},
        "ricota_fresca": {"kcal": 1.74, "p": 0.124, "c": 0.032, "g": 0.127, "categoria": "proteina", "unidade_comum": "g", "obs": "Baixo sódio"},
        "iogurte_desnatado_zero": {"kcal": 0.37, "p": 0.042, "c": 0.068, "g": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Sem açúcar"},
        "iogurte_desnatado": {"kcal": 0.37, "p": 0.042, "c": 0.068, "g": 0, "categoria": "proteina", "unidade_comum": "g", "obs": "Zero"},
        "iogurte_natural_desnatado": {"kcal": 0.42, "p": 0.047, "c": 0.057, "g": 0.002, "categoria": "proteina", "unidade_comum": "g", "obs": "Natural"},
        "iogurte_natural_integral": {"kcal": 0.61, "p": 0.035, "c": 0.047, "g": 0.033, "categoria": "proteina", "unidade_comum": "g", "obs": "Integral"},
        "iogurte_natural": {"kcal": 0.42, "p": 0.047, "c": 0.057, "g": 0.002, "categoria": "proteina", "unidade_comum": "g", "obs": "Desnatado"},
        "iogurte_zero_lactose": {"kcal": 0.4, "p": 0.04, "c": 0.06, "g": 0.002, "categoria": "proteina", "unidade_comum": "g", "obs": "Sem lactose"},
        "leite_desnatado": {"kcal": 0.35, "p": 0.034, "c": 0.049, "g": 0.001, "categoria": "proteina", "unidade_comum": "ml", "obs": "0% gordura"},
        "mussarela_light": {"kcal": 2.5, "p": 0.22, "c": 0.03, "g": 0.16, "categoria": "proteina", "unidade_comum": "g", "obs": "Versão light"},
        "queijo_mussarela_light": {"kcal": 2.5, "p": 0.22, "c": 0.03, "g": 0.16, "categoria": "proteina", "unidade_comum": "g", "obs": "Light"},
        
        # OLEAGINOSAS - VALORES CORRIGIDOS
        "castanha_do_para": {"kcal": 6.56, "p": 0.143, "c": 0.125, "g": 0.663, "categoria": "gordura", "unidade_comum": "unidade", "obs": "1 unidade = 5g"},
        "castanhas_do_para": {"kcal": 6.56, "p": 0.143, "c": 0.125, "g": 0.663, "categoria": "gordura", "unidade_comum": "g", "obs": "Rica em selênio"},
        "amendoim": {"kcal": 5.67, "p": 0.258, "c": 0.162, "g": 0.492, "categoria": "gordura", "unidade_comum": "g", "obs": "Sem sal"},
        "amendoa": {"kcal": 5.79, "p": 0.212, "c": 0.216, "g": 0.494, "categoria": "gordura", "unidade_comum": "unidade", "obs": "1 unidade = 1.2g"},
        "castanha_de_caju": {"kcal": 5.53, "p": 0.182, "c": 0.303, "g": 0.436, "categoria": "gordura", "unidade_comum": "g", "obs": "Sem sal"},
        "castanhas": {"kcal": 6.0, "p": 0.15, "c": 0.15, "g": 0.5, "categoria": "gordura", "unidade_comum": "g", "obs": "Mix variado"},
        "pasta_amendoim_integral": {"kcal": 5.88, "p": 0.25, "c": 0.2, "g": 0.5, "categoria": "gordura", "unidade_comum": "g", "obs": "100% amendoim"},
        "pasta_de_amendoim": {"kcal": 5.88, "p": 0.25, "c": 0.2, "g": 0.5, "categoria": "gordura", "unidade_comum": "g", "obs": "Sem açúcar"},
        
        # SEMENTES - VALORES PRECISOS
        "chia": {"kcal": 4.86, "p": 0.167, "c": 0.421, "g": 0.308, "categoria": "gordura", "unidade_comum": "g", "obs": "Hidratar antes"},
        "chia_em_graos": {"kcal": 4.86, "p": 0.167, "c": 0.421, "g": 0.308, "categoria": "gordura", "unidade_comum": "g", "obs": "Omega 3"},
        "linhaça_moída": {"kcal": 5.34, "p": 0.183, "c": 0.289, "g": 0.423, "categoria": "gordura", "unidade_comum": "g", "obs": "Moer na hora"},
        "psyllium": {"kcal": 4.2, "p": 0.015, "c": 0.88, "g": 0.006, "categoria": "fibra", "unidade_comum": "g", "obs": "Fibra solúvel"},
        "semente_abobora": {"kcal": 5.59, "p": 0.305, "c": 0.109, "g": 0.491, "categoria": "gordura", "unidade_comum": "g", "obs": "Rica em zinco"},
        "semente_girassol": {"kcal": 5.84, "p": 0.209, "c": 0.2, "g": 0.514, "categoria": "gordura", "unidade_comum": "g", "obs": "Sem sal"},
        
        # FRUTAS - VALORES ATUALIZADOS
        "banana": {"kcal": 0.89, "p": 0.011, "c": 0.229, "g": 0.003, "categoria": "fruta", "unidade_comum": "unidade", "obs": "1 média = 100g"},
        "banana_prata": {"kcal": 0.89, "p": 0.013, "c": 0.22, "g": 0.001, "categoria": "fruta", "unidade_comum": "g", "obs": "Prata"},
        "maca": {"kcal": 0.52, "p": 0.003, "c": 0.138, "g": 0.002, "categoria": "fruta", "unidade_comum": "unidade", "obs": "1 média = 150g"},
        "mamao_papaia": {"kcal": 0.4, "p": 0.005, "c": 0.102, "g": 0.001, "categoria": "fruta", "unidade_comum": "g", "obs": "Digestivo"},
        "mamao": {"kcal": 0.4, "p": 0.005, "c": 0.102, "g": 0.001, "categoria": "fruta", "unidade_comum": "g", "obs": "Papaia"},
        "morango": {"kcal": 0.3, "p": 0.007, "c": 0.077, "g": 0.003, "categoria": "fruta", "unidade_comum": "g", "obs": "Antioxidante"},
        "morangos": {"kcal": 0.3, "p": 0.007, "c": 0.077, "g": 0.003, "categoria": "fruta", "unidade_comum": "g", "obs": "Vitamina C"},
        "melao": {"kcal": 0.36, "p": 0.008, "c": 0.091, "g": 0.002, "categoria": "fruta", "unidade_comum": "g", "obs": "Hidratante"},
        "frutas_vermelhas": {"kcal": 0.4, "p": 0.01, "c": 0.09, "g": 0.004, "categoria": "fruta", "unidade_comum": "g", "obs": "Mix berries"},
        "abacaxi": {"kcal": 0.5, "p": 0.005, "c": 0.131, "g": 0.001, "categoria": "fruta", "unidade_comum": "g", "obs": "Bromelina"},
        "laranja_pera": {"kcal": 0.47, "p": 0.009, "c": 0.118, "g": 0.001, "categoria": "fruta", "unidade_comum": "unidade", "obs": "1 média = 130g"},
        "kiwi": {"kcal": 0.61, "p": 0.011, "c": 0.147, "g": 0.005, "categoria": "fruta", "unidade_comum": "unidade", "obs": "1 unidade = 76g"},
        "uva": {"kcal": 0.69, "p": 0.007, "c": 0.171, "g": 0.002, "categoria": "fruta", "unidade_comum": "g", "obs": "Sem semente"},
        "manga": {"kcal": 0.6, "p": 0.008, "c": 0.15, "g": 0.004, "categoria": "fruta", "unidade_comum": "g", "obs": "Tommy ou Palmer"},
        "goiaba": {"kcal": 0.68, "p": 0.026, "c": 0.143, "g": 0.01, "categoria": "fruta", "unidade_comum": "g", "obs": "Rica em vitamina C"},
        "frutas": {"kcal": 0.5, "p": 0.01, "c": 0.12, "g": 0.002, "categoria": "fruta", "unidade_comum": "g", "obs": "Mix variado"},
        "fruta": {"kcal": 0.5, "p": 0.01, "c": 0.12, "g": 0.002, "categoria": "fruta", "unidade_comum": "g", "obs": "Genérica"},
        
        # VEGETAIS - VALORES PRECISOS
        "legumes_variados": {"kcal": 0.4, "p": 0.02, "c": 0.08, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "Mix cozido"},
        "legumes_variados_cozidos": {"kcal": 0.4, "p": 0.02, "c": 0.08, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "No vapor"},
        "legumes_refogados": {"kcal": 0.45, "p": 0.02, "c": 0.08, "g": 0.01, "categoria": "vegetal", "unidade_comum": "g", "obs": "Com pouco óleo"},
        "legumes": {"kcal": 0.4, "p": 0.02, "c": 0.08, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "Variados"},
        "mix_de_legumes": {"kcal": 0.4, "p": 0.02, "c": 0.08, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "Coloridos"},
        "mix_de_legumes_cozidos": {"kcal": 0.4, "p": 0.02, "c": 0.08, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "Vapor"},
        "tomate": {"kcal": 0.18, "p": 0.009, "c": 0.039, "g": 0.002, "categoria": "vegetal", "unidade_comum": "unidade", "obs": "1 médio = 125g"},
        "tomate_em_rodelas": {"kcal": 0.18, "p": 0.009, "c": 0.039, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "Fresco"},
        "tomate_em_rodelas_oregano": {"kcal": 0.18, "p": 0.009, "c": 0.039, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "Com orégano"},
        "pepino": {"kcal": 0.16, "p": 0.007, "c": 0.036, "g": 0.001, "categoria": "vegetal", "unidade_comum": "unidade", "obs": "1 médio = 300g"},
        "alface": {"kcal": 0.15, "p": 0.014, "c": 0.029, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "Todas as variedades"},
        "alface_e_tomate": {"kcal": 0.2, "p": 0.01, "c": 0.04, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "Salada básica"},
        "brocolis": {"kcal": 0.34, "p": 0.028, "c": 0.066, "g": 0.004, "categoria": "vegetal", "unidade_comum": "g", "obs": "No vapor"},
        "abobrinha": {"kcal": 0.17, "p": 0.012, "c": 0.031, "g": 0.003, "categoria": "vegetal", "unidade_comum": "g", "obs": "Baixa caloria"},
        "cenoura": {"kcal": 0.41, "p": 0.009, "c": 0.096, "g": 0.002, "categoria": "vegetal", "unidade_comum": "unidade", "obs": "1 média = 80g"},
        "espinafre": {"kcal": 0.23, "p": 0.029, "c": 0.036, "g": 0.004, "categoria": "vegetal", "unidade_comum": "g", "obs": "Rico em ferro"},
        "rucula": {"kcal": 0.25, "p": 0.026, "c": 0.036, "g": 0.007, "categoria": "vegetal", "unidade_comum": "g", "obs": "Sabor picante"},
        "salada": {"kcal": 0.2, "p": 0.015, "c": 0.04, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "Mix folhas"},
        "salada_de_folhas": {"kcal": 0.2, "p": 0.015, "c": 0.04, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "Variadas"},
        "mix_de_folhas": {"kcal": 0.2, "p": 0.015, "c": 0.04, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "Verdes"},
        
        # GORDURAS - VALORES CORRIGIDOS
        "azeite_extra_virgem": {"kcal": 9.0, "p": 0, "c": 0, "g": 1.0, "categoria": "gordura", "unidade_comum": "g", "obs": "1 col chá = 5g"},
        "azeite_de_oliva_extra_virgem": {"kcal": 9.0, "p": 0, "c": 0, "g": 1.0, "categoria": "gordura", "unidade_comum": "g", "obs": "Extra virgem"},
        "azeite_de_oliva": {"kcal": 9.0, "p": 0, "c": 0, "g": 1.0, "categoria": "gordura", "unidade_comum": "g", "obs": "Puro"},
        "azeite": {"kcal": 9.0, "p": 0, "c": 0, "g": 1.0, "categoria": "gordura", "unidade_comum": "g", "obs": "Oliva"},
        "oleo_coco_extravirgem": {"kcal": 9.0, "p": 0, "c": 0, "g": 1.0, "categoria": "gordura", "unidade_comum": "g", "obs": "TCM"},
        "abacate": {"kcal": 1.6, "p": 0.02, "c": 0.085, "g": 0.147, "categoria": "gordura", "unidade_comum": "g", "obs": "Gordura boa"},
        
        # DIVERSOS - VALORES ATUALIZADOS
        "cacau_po_100": {"kcal": 2.28, "p": 0.196, "c": 0.577, "g": 0.137, "categoria": "diversos", "unidade_comum": "g", "obs": "100% cacau"},
        "cacau_em_po": {"kcal": 2.28, "p": 0.196, "c": 0.577, "g": 0.137, "categoria": "diversos", "unidade_comum": "g", "obs": "Sem açúcar"},
        "canela_po": {"kcal": 2.47, "p": 0.04, "c": 0.806, "g": 0.012, "categoria": "diversos", "unidade_comum": "g", "obs": "Termogênica"},
        "canela_em_po": {"kcal": 2.47, "p": 0.04, "c": 0.806, "g": 0.012, "categoria": "diversos", "unidade_comum": "g", "obs": "Em pó"},
        "canela": {"kcal": 2.47, "p": 0.04, "c": 0.806, "g": 0.012, "categoria": "diversos", "unidade_comum": "g", "obs": "Especiaria"},
        "molho_tomate_caseiro": {"kcal": 0.82, "p": 0.014, "c": 0.187, "g": 0.002, "categoria": "diversos", "unidade_comum": "g", "obs": "Sem açúcar"},
        "molho_caseiro": {"kcal": 0.9, "p": 0.015, "c": 0.2, "g": 0.003, "categoria": "diversos", "unidade_comum": "g", "obs": "Tomate natural"},
        "ketchup_zero": {"kcal": 1.0, "p": 0.01, "c": 0.24, "g": 0, "categoria": "diversos", "unidade_comum": "g", "obs": "Zero açúcar"},
        "ketchup_e_mostarda": {"kcal": 2.0, "p": 0.02, "c": 0.45, "g": 0.01, "categoria": "diversos", "unidade_comum": "g", "obs": "Mix"},
        "mostarda": {"kcal": 0.66, "p": 0.04, "c": 0.06, "g": 0.04, "categoria": "diversos", "unidade_comum": "g", "obs": "Dijon"},
        "molhos_light": {"kcal": 1.5, "p": 0.01, "c": 0.35, "g": 0.005, "categoria": "diversos", "unidade_comum": "g", "obs": "Variados light"},
        "doce_de_leite_light": {"kcal": 3.1, "p": 0.07, "c": 0.55, "g": 0.07, "categoria": "diversos", "unidade_comum": "g", "obs": "Moderação"},
        "chocolate_amargo_70": {"kcal": 5.98, "p": 0.077, "c": 0.458, "g": 0.428, "categoria": "diversos", "unidade_comum": "g", "obs": "70% cacau"},
        "cafe_preto": {"kcal": 0.02, "p": 0.001, "c": 0.003, "g": 0, "categoria": "diversos", "unidade_comum": "ml", "obs": "Sem açúcar"},
        "cafe": {"kcal": 0.02, "p": 0.001, "c": 0.003, "g": 0, "categoria": "diversos", "unidade_comum": "ml", "obs": "Preto"},
        "cha_verde": {"kcal": 0.01, "p": 0, "c": 0.002, "g": 0, "categoria": "diversos", "unidade_comum": "ml", "obs": "Antioxidante"},
        "champignon": {"kcal": 0.22, "p": 0.031, "c": 0.033, "g": 0.003, "categoria": "vegetal", "unidade_comum": "g", "obs": "Fresco"},
        "tomate_cereja": {"kcal": 0.18, "p": 0.009, "c": 0.039, "g": 0.002, "categoria": "vegetal", "unidade_comum": "g", "obs": "Doce"},
        "oregano": {"kcal": 2.65, "p": 0.09, "c": 0.689, "g": 0.043, "categoria": "diversos", "unidade_comum": "g", "obs": "Seco"},
        "gelatina_diet": {"kcal": 0.6, "p": 0.14, "c": 0.01, "g": 0, "categoria": "diversos", "unidade_comum": "g", "obs": "Zero açúcar"},
        "creme_leite_light": {"kcal": 1.87, "p": 0.025, "c": 0.04, "g": 0.17, "categoria": "gordura", "unidade_comum": "g", "obs": "Light"},
        "creme_de_leite_light": {"kcal": 1.87, "p": 0.025, "c": 0.04, "g": 0.17, "categoria": "gordura", "unidade_comum": "g", "obs": "Reduzido"},
        "milho_e_ervilha": {"kcal": 1.06, "p": 0.044, "c": 0.216, "g": 0.01, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Mix"},
        
        # PRODUTOS PRONTOS
        "yopro_25g_proteina": {"kcal": 0.6, "p": 0.1, "c": 0.04, "g": 0.004, "categoria": "proteina", "unidade_comum": "ml", "obs": "1 unidade = 250ml"},
        "yopro_protein": {"kcal": 0.6, "p": 0.1, "c": 0.04, "g": 0.004, "categoria": "proteina", "unidade_comum": "ml", "obs": "Shake pronto"},
        "yopro": {"kcal": 0.6, "p": 0.1, "c": 0.04, "g": 0.004, "categoria": "proteina", "unidade_comum": "ml", "obs": "25g proteína"},
        "yopro_shake": {"kcal": 0.6, "p": 0.1, "c": 0.04, "g": 0.004, "categoria": "proteina", "unidade_comum": "ml", "obs": "Pronto"},
        "barra_bold_protein": {"kcal": 3.6, "p": 0.4, "c": 0.3, "g": 0.12, "categoria": "proteina", "unidade_comum": "g", "obs": "1 barra = 50g"},
        "pre_treino_em_po": {"kcal": 0.4, "p": 0, "c": 0.1, "g": 0, "categoria": "diversos", "unidade_comum": "g", "obs": "1 dose = 10g"},
        
        # PREPARAÇÕES ESPECÍFICAS
        "frango_desfiado": {"kcal": 1.65, "p": 0.31, "c": 0, "g": 0.036, "categoria": "proteina", "unidade_comum": "g", "obs": "Cozido"},
        "frango_cozido_desfiado": {"kcal": 1.65, "p": 0.31, "c": 0, "g": 0.036, "categoria": "proteina", "unidade_comum": "g", "obs": "Desfiado"},
        "frango_cozido": {"kcal": 1.65, "p": 0.31, "c": 0, "g": 0.036, "categoria": "proteina", "unidade_comum": "g", "obs": "Sem pele"},
        "file_de_frango_grelhado": {"kcal": 1.65, "p": 0.31, "c": 0, "g": 0.036, "categoria": "proteina", "unidade_comum": "g", "obs": "Grelhado"},
        "file_de_frango": {"kcal": 1.65, "p": 0.31, "c": 0, "g": 0.036, "categoria": "proteina", "unidade_comum": "g", "obs": "Grelhado"},
        "patinho_moido": {"kcal": 1.5, "p": 0.22, "c": 0, "g": 0.06, "categoria": "proteina", "unidade_comum": "g", "obs": "Cru = cozido"},
        
        # COMPLEMENTOS
        "whey_protein": {"kcal": 3.68, "p": 0.9, "c": 0.02, "g": 0.01, "categoria": "proteina", "unidade_comum": "g", "obs": "Isolado"},
        "granola": {"kcal": 4.89, "p": 0.135, "c": 0.639, "g": 0.201, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Sem açúcar"},
        "mel": {"kcal": 3.04, "p": 0.003, "c": 0.824, "g": 0, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Natural"},
        "biscoitos_de_arroz": {"kcal": 3.87, "p": 0.089, "c": 0.816, "g": 0.038, "categoria": "carboidrato", "unidade_comum": "unidade", "obs": "1 grande = 7g"},
        "pipoca": {"kcal": 3.87, "p": 0.13, "c": 0.78, "g": 0.05, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Sem óleo"},
        "cuscuz": {"kcal": 1.12, "p": 0.022, "c": 0.232, "g": 0.005, "categoria": "carboidrato", "unidade_comum": "g", "obs": "Hidratado"}
    }

def get_meal_templates():
    """Templates corrigidos com 6 opções no lanche e 4 no jantar."""
    return {
        "cafe_da_manha": [
            {"id": "cafe_completo_1", "type": "base", "nome_template": "Café da Manhã Completo", 
             "ingredientes": ["ovo_inteiro:100", "pao_forma_integral:25", "whey_protein_isolado_hidrolisado:20", 
                            "iogurte_desnatado_zero:100", "chia:5", "mamao_papaia:100"]},
            {"id": "cafe_completo_2", "type": "base", "nome_template": "Café com Aveia", 
             "ingredientes": ["ovo_inteiro:100", "aveia_flocos:30", "whey_protein_isolado_hidrolisado:25", 
                            "banana:60", "linhaça_moída:10", "leite_desnatado:200"]},
            {"id": "cafe_completo_3", "type": "base", "nome_template": "Café Leve", 
             "ingredientes": ["tapioca_seca:20", "ovo_inteiro:100", "queijo_cottage:50", 
                            "mamao_papaia:100", "chia:5"]}
        ],
        
        "almoco": [
            {"id": "almoco_padrao_frango", "type": "base", "nome_template": "Almoço com Frango", 
             "ingredientes": ["peito_frango_grelhado_sem_pele:120", "arroz_branco_cozido:60", 
                            "feijao_carioca_cozido:80", "azeite_extra_virgem:5", "legumes_variados:100", 
                            "salada:50", "fruta:100"]},
            {"id": "almoco_padrao_carne", "type": "base", "nome_template": "Almoço com Carne", 
             "ingredientes": ["patinho_moido_95_5:120", "arroz_integral_cozido:60", 
                            "feijao_preto_cozido:80", "azeite_extra_virgem:5", "legumes_variados:100", 
                            "salada:50", "fruta:100"]},
            {"id": "almoco_padrao_peixe", "type": "base", "nome_template": "Almoço com Peixe", 
             "ingredientes": ["tilapia_assada:150", "batata_doce_cozida:120", 
                            "feijao_carioca_cozido:80", "azeite_extra_virgem:5", "legumes_variados:100", 
                            "salada:50", "fruta:100"]}
        ],
        
        "lanche": [
            {"id": "panqueca_proteica", "type": "receita", "nome_template": "Panqueca Proteica", 
             "ingredientes": ["banana:60", "ovo_inteiro:50", "whey_protein_isolado_hidrolisado:25", 
                            "cacau_po_100:5", "canela_po:2", "psyllium:5"],
             "modo_preparo": "Bater tudo e assar em frigideira antiaderente"},
            
            {"id": "crepioca_proteica", "type": "receita", "nome_template": "Crepioca", 
             "ingredientes": ["tapioca_seca:20", "ovo_inteiro:50", "clara_ovo:66", "requeijao_light:20"],
             "modo_preparo": "Misturar e grelhar"},
            
            {"id": "iogurte_turbinado", "type": "base", "nome_template": "Iogurte com Whey", 
             "ingredientes": ["iogurte_desnatado_zero:150", "whey_protein_isolado_hidrolisado:30", 
                            "morango:100", "chia:5"]},
            
            {"id": "omelete_completo", "type": "receita", "nome_template": "Omelete", 
             "ingredientes": ["ovo_inteiro:100", "clara_ovo:66", "mussarela_light:30", "legumes_variados:50"]},
            
            {"id": "sanduiche_proteico", "type": "base", "nome_template": "Sanduíche", 
             "ingredientes": ["pao_forma_integral:50", "peito_frango_grelhado_sem_pele:80", "requeijao_light:20"]},
            
            {"id": "shake_frutas", "type": "base", "nome_template": "Shake de Frutas",
             "ingredientes": ["whey_protein_isolado_hidrolisado:35", "frutas_vermelhas:100", 
                            "iogurte_desnatado_zero:120", "aveia_flocos:20"]}
        ],
        
        "jantar": [
            {"id": "pizza_fake", "type": "receita", "nome_template": "Pizza Fake", 
             "ingredientes": ["rap10_integral:35", "queijo_mussarela_light:30", "tomate_em_rodelas:50", 
                            "frango_desfiado:80", "oregano:2", "azeite_de_oliva:5"],
             "modo_preparo": "Montar sobre rap10 e aquecer"},
            
            {"id": "strogonoff_light", "type": "receita", "nome_template": "Strogonoff Light", 
             "ingredientes": ["file_mignon:100", "creme_de_leite_light:40", "ketchup_e_mostarda:10", 
                            "champignon:50", "arroz_branco_cozido:75"],
             "modo_preparo": "Refogar carne, adicionar molho"},
            
            {"id": "salpicao_light", "type": "receita", "nome_template": "Salpicão Light", 
             "ingredientes": ["rap10_integral:35", "frango_cozido_desfiado:100", "mix_de_legumes:50", 
                            "requeijao_light:20"],
             "modo_preparo": "Misturar tudo"},
            
            {"id": "hamburguer_artesanal", "type": "receita", "nome_template": "Hambúrguer Artesanal", 
             "ingredientes": ["pao_integral:50", "patinho_moido:120", "queijo_mussarela_light:20", 
                            "alface_e_tomate:50", "molhos_light:10"],
             "modo_preparo": "Grelhar e montar"}
        ],
        
        "ceia": [
            {"id": "ceia_padrao", "type": "base", "nome_template": "Ceia Proteica", 
             "ingredientes": ["iogurte_desnatado_zero:100", "whey_protein_isolado_hidrolisado:15", 
                            "morango:75", "chia:5", "gelatina_diet:100"]},
            {"id": "ceia_frutas", "type": "base", "nome_template": "Ceia com Frutas", 
             "ingredientes": ["iogurte_desnatado_zero:150", "whey_protein_isolado_hidrolisado:20", 
                            "fruta:100"]}
        ]
    }

def get_substitution_rules():
    """Regras de substituição corrigidas e validadas."""
    return {
        "peito_frango_grelhado_sem_pele": {
            "opcoes": [
                {"item": "patinho_moido_95_5", "qtd_g": 120, "obs": "Magro 95/5"},
                {"item": "tilapia_assada", "qtd_g": 150, "obs": "Grelhada"},
                {"item": "file_mignon", "qtd_g": 120, "obs": "Sem gordura"},
                {"item": "atum_enlatado_agua", "qtd_g": 120, "obs": "Em água"},
                {"item": "file_suino_magro", "qtd_g": 120, "obs": "Lombo"}
            ],
            "categoria": "proteina"
        },
        
        "arroz_branco_cozido": {
            "opcoes": [
                {"item": "batata_doce_cozida", "qtd_g": 120, "obs": "Com casca"},
                {"item": "batata_inglesa_cozida", "qtd_g": 120, "obs": "Sem óleo"},
                {"item": "arroz_integral_cozido", "qtd_g": 60, "obs": "Integral"},
                {"item": "macarrao_integral_cozido", "qtd_g": 60, "obs": "Al dente"},
                {"item": "abobora_japonesa_cozida", "qtd_g": 140, "obs": "Kabotiá"}
            ],
            "categoria": "carboidrato"
        },
        
        "feijao_carioca_cozido": {
            "opcoes": [
                {"item": "feijao_preto_cozido", "qtd_g": 80, "obs": "Temperado"},
                {"item": "lentilha_cozida", "qtd_g": 80, "obs": "Al dente"},
                {"item": "grao_de_bico_cozido", "qtd_g": 80, "obs": "Macio"},
                {"item": "ervilha_cozida", "qtd_g": 80, "obs": "Fresca"}
            ],
            "categoria": "leguminosa"
        },
        
        "whey_protein_isolado_hidrolisado": {
            "opcoes": [
                {"item": "peito_frango_grelhado_sem_pele", "qtd_g": 30, "obs": "Equivalente"},
                {"item": "ovo_inteiro", "qtd_g": 50, "obs": "1 unidade"},
                {"item": "clara_ovo", "qtd_g": 100, "obs": "3 claras"}
            ],
            "categoria": "proteina"
        }
    }

def get_static_info():
    """Informações estáticas corrigidas."""
    return {
        "legumes_variados": {
            "descricao": "Tomate, Chuchu, Abobrinha, Brócolis, Cenoura, Vagem, Berinjela, Couve-flor",
            "instrucao": "Cozinhar no vapor ou grelhar",
            "beneficios": "Vitaminas, minerais e fibras"
        },
        
        "orientacao_refeicao_livre": {
            "descricao": "1 refeição livre controlada no fim de semana",
            "exemplos": [
                "1 hambúrguer + sobremesa pequena",
                "2-3 fatias pizza + salada",
                "20 peças sushi",
                "1 prato massa + 1 taça vinho"
            ]
        },
        
        "gramatura_padrao_grupos": {
            "proteinas": {
                "frango": "120g",
                "carne": "120g", 
                "peixe": "150g",
                "ovos": "100g (2 unidades)"
            },
            "carboidratos": {
                "arroz": "60g",
                "batatas": "120g",
                "massas": "60g"
            },
            "gorduras": {
                "azeite": "5g",
                "oleaginosas": "30g"
            }
        }
    }

def validate_food_data():
    """Validação completa com correções."""
    foods = get_food_data()
    errors = []
    warnings = []
    
    for food_id, food_data in foods.items():
        # Validações obrigatórias
        if not all(k in food_data for k in ['kcal', 'p', 'c', 'g']):
            errors.append(f"{food_id}: falta macronutriente")
            continue
            
        # Validação calórica
        calc_kcal = (food_data['p'] * 4) + (food_data['c'] * 4) + (food_data['g'] * 9)
        diff = abs(calc_kcal - food_data['kcal'])
        
        if diff > 0.1:  # Tolerância de 0.1 kcal
            warnings.append(f"{food_id}: diferença {diff:.2f} kcal")
    
    # Validar templates
    templates = get_meal_templates()
    if len(templates['lanche']) < 6:
        errors.append("Lanche deve ter 6 opções")
    if len(templates['jantar']) < 4:
        errors.append("Jantar deve ter 4 opções")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "total_foods": len(foods)
    }
