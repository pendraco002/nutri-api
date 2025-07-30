from database import get_food_data, get_recipes

def create_meal_plan(goals):
    total_kcal_goal = goals.get("total_kcal", 2000)
    protein_min = goals.get("protein_min_g", 0)
    carb_max = goals.get("carb_max_g", 1000)
    fat_max = goals.get("fat_max_g", 1000)

    db = get_food_data()
    recipes = get_recipes()

    frango_g = 150
    arroz_g = 100
    azeite_g = 10

    almoco_kcal = (
        db["file_de_frango_grelhado"]["kcal_por_g"] * frango_g +
        db["arroz_branco_cozido"]["kcal_por_g"] * arroz_g +
        db["azeite_extra_virgem"]["kcal_por_g"] * azeite_g
    )

    almoco_proteina = db["file_de_frango_grelhado"]["proteina_por_g"] * frango_g
    almoco_carb = db["arroz_branco_cozido"]["carb_por_g"] * arroz_g
    almoco_gordura = db["azeite_extra_virgem"]["gordura_por_g"] * azeite_g

    jantar = recipes["hamburguer_artesanal"]

    total_kcal = almoco_kcal + jantar["kcal"]
    total_prot = almoco_proteina + jantar["proteina_g"]
    total_carb = almoco_carb + jantar["carb_g"]
    total_fat = almoco_gordura + jantar["gordura_g"]

    return {
        "summary": {
            "total_kcal_calculado": round(total_kcal),
            "total_proteina_g": round(total_prot, 1),
            "total_carb_g": round(total_carb, 1),
            "total_gordura_g": round(total_fat, 1),
            "meta_total_kcal": total_kcal_goal,
            "meta_proteina_min": protein_min,
            "meta_carb_max": carb_max,
            "meta_fat_max": fat_max
        },
        "meals": [
            {
                "nome": "Almoço",
                "horario": "12:00",
                "meta_kcal": int(total_kcal_goal * 0.4),
                "total_kcal": int(almoco_kcal),
                "itens": [
                    {"item": "Filé de frango grelhado", "qtd": frango_g, "unidade": "g",
                     "kcal": int(db["file_de_frango_grelhado"]["kcal_por_g"] * frango_g)},
                    {"item": "Arroz branco cozido", "qtd": arroz_g, "unidade": "g",
                     "kcal": int(db["arroz_branco_cozido"]["kcal_por_g"] * arroz_g)},
                    {"item": "Azeite extra virgem", "qtd": azeite_g, "unidade": "g",
                     "kcal": int(db["azeite_extra_virgem"]["kcal_por_g"] * azeite_g)}
                ]
            },
            {
                "nome": "Jantar",
                "horario": "20:00",
                "meta_kcal": int(total_kcal_goal * 0.6),
                "total_kcal": jantar["kcal"],
                "itens": jantar["itens"]
            }
        ]
    }
