from database import get_food_data, get_recipes
from datetime import datetime

def generate_plan_logic(request_data):
    """
    Motor de Lógica para Geração de Planos.
    ATENÇÃO: Esta é uma implementação SIMPLIFICADA para fins de demonstração.
    A lógica de otimização real seria muito mais complexa, envolvendo algoritmos
    para encontrar a melhor combinação de alimentos que satisfaça todas as restrições.
    """
    paciente_info = request_data.get('paciente', {})
    metas = request_data.get('metas', {})
    preferencias = request_data.get('preferencias', {})

    # 1. Calcular metas numéricas
    peso_kg = paciente_info.get('peso_kg')
    meta_kcal = metas.get('kcal_total')
    
    if not peso_kg or not meta_kcal:
        return {"erro": "Peso do paciente e meta de kcal são obrigatórios."}, 400

    # 2. Lógica de montagem (exemplo simplificado)
    # Em um sistema real, aqui entraria o algoritmo de otimização.
    # Por agora, vamos apenas montar um plano de exemplo com base nas preferências.
    
    db_foods = get_food_data()
    db_recipes = get_recipes()
    
    refeicoes = []
    total_kcal_calculado = 0

    # Refeição 1: Almoço Padrão
    almoco_kcal = db_foods["frango_grelhado"]["kcal"] * 150 + db_foods["batata_doce_cozida"]["kcal"] * 200
    refeicoes.append({
        "nome_refeicao": "Almoço",
        "horario": "12:00",
        "kcal_total_refeicao": round(almoco_kcal),
        "itens": [
            {"item": "Frango Grelhado", "qtd": 150, "unidade": "g"},
            {"item": "Batata Doce Cozida", "qtd": 200, "unidade": "g"}
        ],
        "substituicoes": ["- Arroz por: 150g de aipim ou 150g de macarrão"]
    })
    total_kcal_calculado += almoco_kcal

    # Refeição 2: Lanche com base na preferência
    template_lanche = preferencias.get("template_lanche", "panqueca_proteica_v1")
    lanche = db_recipes.get(template_lanche, db_recipes["panqueca_proteica_v1"])
    refeicoes.append({
        "nome_refeicao": "Lanche da Tarde",
        "horario": "16:00",
        "kcal_total_refeicao": round(lanche["kcal"]),
        "itens": lanche["itens"],
        "substituicoes": ["- Pode trocar por: 1 iogurte + 30g de whey + 1 fruta"]
    })
    total_kcal_calculado += lanche["kcal"]

    # Refeição 3: Jantar com base na preferência
    template_jantar = preferencias.get("template_jantar", "hamburguer_artesanal_v1")
    jantar = db_recipes.get(template_jantar, db_recipes["hamburguer_artesanal_v1"])
    refeicoes.append({
        "nome_refeicao": "Jantar",
        "horario": "20:00",
        "kcal_total_refeicao": round(jantar["kcal"]),
        "itens": jantar["itens"],
        "substituicoes": ["- Pode trocar por: Pizza Fake (1 Rap10 + 80g frango + 30g queijo)"]
    })
    total_kcal_calculado += jantar["kcal"]

    # 3. Montar a resposta final
    response_payload = {
        "plano": {
            "paciente": paciente_info.get("nome", "Paciente"),
            "data": datetime.now().strftime("%d/%m/%Y"),
            "resumo": {
                "meta_kcal": meta_kcal,
                "total_kcal_calculado": round(total_kcal_calculado),
                "total_proteina": "N/A (lógica simplificada)",
                "total_carboidratos": "N/A (lógica simplificada)",
                "total_gordura": "N/A (lógica simplificada)"
            },
            "refeicoes": refeicoes
        }
    }
    
    return response_payload, 200

