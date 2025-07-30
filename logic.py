# logic.py (Versão Final 12.0 - Apresentação Impecável)

# ... (importações e schemas Pydantic permanecem os mesmos da v11.0) ...
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
import random
from database import get_food_data, get_meal_templates, get_substitution_rules, get_static_info

# (Schemas Pydantic aqui)

def format_item_for_response(food_id, gramas, db_foods):
    """
    NOVA FUNÇÃO: Formata um item de forma rica e precisa,
    evitando simplificações indesejadas.
    """
    nome_item = food_id.replace("_", " ").title()
    # Lógica para converter gramas em unidades, se aplicável e desejado,
    # mas priorizando a gramatura para precisão.
    # Ex: 100g de ovo -> "Ovo Inteiro (2 un - 100g)"
    if food_id == "ovo_inteiro":
        unidades = round(gramas / 50)
        return f"{nome_item} ({unidades} un - {round(gramas)}g)"
    return f"{nome_item} ({round(gramas)}g)"

def generate_plan_logic(request_data):
    try:
        # ... (Passos 1 a 4: Validação, Saneamento, Otimização - permanecem os mesmos) ...
        
        # --- PASSO 5: CONSTRUÇÃO DA RESPOSTA COM MÁXIMA PRECISÃO ---
        # Esta seção é reescrita para ser obcecada com os detalhes.
        
        # (Simulação de um resultado do solver)
        
        refeicoes_finais_formatadas = []
        
        # Exemplo para o Jantar
        jantar_principal = {
            "nome_refeicao": "Jantar",
            "kcal": 500,
            "itens": [
                format_item_for_response("tilapia_assada", 150, db_foods),
                format_item_for_response("arroz_branco_cozido", 80, db_foods),
                # ... etc
            ],
            "observacoes": {
                "Proteína": "Pode ser substituído por...",
                # ... etc
            }
        }
        
        substituicoes_jantar_formatadas = [
            {
                "nome": "Hambúrguer Artesanal Controlado",
                "kcal": 500,
                "ingredientes": [
                    "Pão de hambúrguer integral (1 un - 50g)",
                    "Hambúrguer de patinho moído (120g)",
                    "Queijo mussarela light (20g)",
                    "Molho caseiro light (10g)",
                    "Mix de folhas e tomate (à vontade)"
                ]
            },
            # ... outras receitas formatadas com 100% de detalhe
        ]
        
        refeicoes_finais_formatadas.append({
            "refeicao_principal": jantar_principal,
            "substituicoes_de_refeicao": substituicoes_jantar_formatadas
        })

        response_payload = {
            "plano": {
                "paciente": "João Silva",
                "data": datetime.now().strftime("%d/%m/%Y"),
                "resumo": {
                    # ... resumo numérico ...
                },
                "refeicoes": refeicoes_finais_formatadas
            }
        }
        
        return response_payload, 200

    except Exception as e:
        print(f"Erro interno no servidor: {e}")
        return {"erro": "Ocorreu um erro interno inesperado no servidor."}, 500
