"""
Plan Builder - Módulo para construção de planos nutricionais
Padrão Pedro Barros - Versão Otimizada
"""

from typing import Dict, List, Optional, Tuple
from datetime import datetime
from data_manager import DataManager

class PlanBuilder:
    """Construtor de planos nutricionais com lógica otimizada"""
    
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager
    
    def calcular_necessidades_basicas(self, paciente: Dict, metas: Dict) -> Dict:
        """Calcula necessidades nutricionais básicas"""
        peso = paciente["peso_kg"]
        altura = paciente["altura_cm"]
        sexo = paciente["sexo"]
        
        # Cálculo do IMC
        altura_m = altura / 100
        imc = peso / (altura_m ** 2)
        
        # Necessidades proteicas
        proteina_min_g = peso * metas["proteina_min_g_por_kg"]
        
        # Distribuição de macros
        kcal_total = metas["kcal_total"]
        carboidrato_max_kcal = kcal_total * (metas["carboidrato_max_percent"] / 100)
        gordura_max_kcal = kcal_total * (metas["gordura_max_percent"] / 100)
        
        # Conversão para gramas
        carboidrato_max_g = carboidrato_max_kcal / 4  # 4 kcal/g
        gordura_max_g = gordura_max_kcal / 9  # 9 kcal/g
        
        return {
            "imc": round(imc, 2),
            "kcal_total": kcal_total,
            "proteina_min_g": round(proteina_min_g, 2),
            "carboidrato_max_g": round(carboidrato_max_g, 2),
            "gordura_max_g": round(gordura_max_g, 2),
            "fibras_min_g": metas["fibras_min_g"]
        }
    
    def criar_refeicao(self, nome: str, horario: str, alimentos: List[Dict]) -> Dict:
        """Cria uma refeição com cálculos automáticos"""
        total_kcal = 0
        total_proteina = 0
        total_carboidrato = 0
        total_gordura = 0
        total_fibra = 0
        
        itens_formatados = []
        
        for item in alimentos:
            codigo = item["codigo"]
            quantidade = item["quantidade"]
            
            macros = self.data_manager.calcular_macros(codigo, quantidade)
            if macros:
                total_kcal += macros["kcal"]
                total_proteina += macros["proteina_g"]
                total_carboidrato += macros["carboidrato_g"]
                total_gordura += macros["gordura_g"]
                total_fibra += macros["fibra_g"]
                
                itens_formatados.append({
                    "nome": macros["nome"],
                    "unidade": macros["unidade"],
                    "quantidade": quantidade,
                    "kcal": macros["kcal"]
                })
        
        return {
            "nome": nome,
            "horario": horario,
            "itens": itens_formatados,
            "totais": {
                "kcal": round(total_kcal, 2),
                "proteina_g": round(total_proteina, 2),
                "carboidrato_g": round(total_carboidrato, 2),
                "gordura_g": round(total_gordura, 2),
                "fibra_g": round(total_fibra, 2)
            }
        }
    
    def criar_substituicoes_lanche(self) -> List[Dict]:
        """Cria as 6 substituições obrigatórias do lanche"""
        return [
            {
                "numero": 1,
                "nome": "Panqueca Proteica",
                "ingredientes": ["Banana", "Ovo", "Whey", "Cacau", "Canela", "Psyllium"],
                "observacao": "Misture todos os ingredientes e faça na frigideira antiaderente"
            },
            {
                "numero": 2,
                "nome": "Shake com Frutas",
                "ingredientes": ["Frutas", "Whey", "Iogurte"],
                "observacao": "Bata no liquidificador com gelo"
            },
            {
                "numero": 3,
                "nome": "Crepioca",
                "ingredientes": ["Tapioca", "Ovo", "Clara", "Requeijão"],
                "observacao": "Misture a tapioca com ovo e clara, faça na frigideira"
            },
            {
                "numero": 4,
                "nome": "Yopro",
                "ingredientes": ["Yopro"],
                "observacao": "Pode ser consumido gelado"
            },
            {
                "numero": 5,
                "nome": "Barra de Proteína Bold",
                "ingredientes": ["Barra de Proteína Bold"],
                "observacao": "Escolha o sabor de sua preferência"
            },
            {
                "numero": 6,
                "nome": "Omelete com Queijo",
                "ingredientes": ["Ovo", "Clara", "Queijo", "Frutas"],
                "observacao": "Faça o omelete e sirva com frutas"
            }
        ]
    
    def criar_receitas_jantar(self) -> List[Dict]:
        """Cria as 4 receitas especiais do jantar"""
        return [
            {
                "nome": "Pizza Fake",
                "ingredientes": ["Rap10", "Queijo", "Tomate cereja", "Orégano", "Molho", "Whey"],
                "preparo": "Use o Rap10 como base, adicione os ingredientes e leve ao forno"
            },
            {
                "nome": "Strogonoff Light",
                "ingredientes": ["Filé-mignon", "Ketchup", "Mostarda", "Arroz", "Champignon", "Creme"],
                "preparo": "Refogue a carne, adicione o molho e sirva com arroz"
            },
            {
                "nome": "Salpicão Light",
                "ingredientes": ["Rap10", "Requeijão", "Palmito/cenoura/milho/tomate", "Frango"],
                "preparo": "Misture todos os ingredientes e tempere a gosto"
            },
            {
                "nome": "Hambúrguer Artesanal",
                "ingredientes": ["Pão", "Carne", "Queijo", "Ketchup/Mostarda/Maionese"],
                "preparo": "Monte o hambúrguer com os ingredientes de sua preferência"
            }
        ]
    
    def construir_plano_completo(self, paciente: Dict, metas: Dict, refeicoes: List[Dict]) -> Dict:
        """Constrói o plano nutricional completo"""
        necessidades = self.calcular_necessidades_basicas(paciente, metas)
        
        # Calcula totais do plano
        total_kcal = sum(r["totais"]["kcal"] for r in refeicoes)
        total_proteina = sum(r["totais"]["proteina_g"] for r in refeicoes)
        total_carboidrato = sum(r["totais"]["carboidrato_g"] for r in refeicoes)
        total_gordura = sum(r["totais"]["gordura_g"] for r in refeicoes)
        total_fibra = sum(r["totais"]["fibra_g"] for r in refeicoes)
        
        # Validações
        validacoes = {
            "kcal_ok": abs(total_kcal - necessidades["kcal_total"]) <= 50,
            "proteina_ok": total_proteina >= necessidades["proteina_min_g"],
            "carboidrato_ok": total_carboidrato <= necessidades["carboidrato_max_g"],
            "gordura_ok": total_gordura <= necessidades["gordura_max_g"],
            "fibra_ok": total_fibra >= necessidades["fibras_min_g"]
        }
        
        return {
            "paciente": paciente,
            "data": datetime.now().strftime("%d/%m/%Y"),
            "necessidades": necessidades,
            "refeicoes": refeicoes,
            "substituicoes_lanche": self.criar_substituicoes_lanche(),
            "receitas_jantar": self.criar_receitas_jantar(),
            "totais": {
                "kcal": round(total_kcal, 2),
                "proteina_g": round(total_proteina, 2),
                "carboidrato_g": round(total_carboidrato, 2),
                "gordura_g": round(total_gordura, 2),
                "fibra_g": round(total_fibra, 2)
            },
            "validacoes": validacoes,
            "resumo_nutricional": self._criar_resumo_nutricional(necessidades, {
                "kcal": total_kcal,
                "proteina_g": total_proteina,
                "carboidrato_g": total_carboidrato,
                "gordura_g": total_gordura,
                "fibra_g": total_fibra
            })
        }
    
    def _criar_resumo_nutricional(self, necessidades: Dict, totais: Dict) -> Dict:
        """Cria resumo nutricional com percentuais"""
        return {
            "kcal": {
                "valor": totais["kcal"],
                "meta": necessidades["kcal_total"],
                "percentual": round((totais["kcal"] / necessidades["kcal_total"]) * 100, 1)
            },
            "proteina": {
                "valor": totais["proteina_g"],
                "meta": necessidades["proteina_min_g"],
                "percentual": round((totais["proteina_g"] / necessidades["proteina_min_g"]) * 100, 1)
            },
            "carboidrato": {
                "valor": totais["carboidrato_g"],
                "meta": necessidades["carboidrato_max_g"],
                "percentual": round((totais["carboidrato_g"] / necessidades["carboidrato_max_g"]) * 100, 1)
            },
            "gordura": {
                "valor": totais["gordura_g"],
                "meta": necessidades["gordura_max_g"],
                "percentual": round((totais["gordura_g"] / necessidades["gordura_max_g"]) * 100, 1)
            },
            "fibra": {
                "valor": totais["fibra_g"],
                "meta": necessidades["fibras_min_g"],
                "percentual": round((totais["fibra_g"] / necessidades["fibras_min_g"]) * 100, 1)
            }
        }
    
    def criar_plano_exemplo(self) -> Dict:
        """Cria um plano de exemplo para testes"""
        paciente = {
            "nome": "João Silva",
            "peso_kg": 75,
            "altura_cm": 178,
            "sexo": "M"
        }
        
        metas = {
            "kcal_total": 2000,
            "proteina_min_g_por_kg": 2.3,
            "carboidrato_max_percent": 35,
            "gordura_max_percent": 25,
            "fibras_min_g": 30
        }
        
        # Refeições de exemplo com proteína adequada
        refeicoes = [
            self.criar_refeicao("Café da manhã", "08:00", [
                {"codigo": "ovo_galinha_inteiro", "quantidade": 3},
                {"codigo": "aveia_flocos", "quantidade": 3},
                {"codigo": "banana_nanica", "quantidade": 1}
            ]),
            self.criar_refeicao("Lanche da manhã", "10:30", [
                {"codigo": "whey_protein", "quantidade": 1.5},
                {"codigo": "banana_nanica", "quantidade": 0.5}
            ]),
            self.criar_refeicao("Almoço", "12:30", [
                {"codigo": "ovo_galinha_inteiro", "quantidade": 4},
                {"codigo": "aveia_flocos", "quantidade": 2}
            ]),
            self.criar_refeicao("Lanche da tarde", "15:30", [
                {"codigo": "whey_protein", "quantidade": 1.5}
            ]),
            self.criar_refeicao("Jantar", "19:00", [
                {"codigo": "ovo_galinha_inteiro", "quantidade": 3},
                {"codigo": "aveia_flocos", "quantidade": 1}
            ]),
            self.criar_refeicao("Ceia", "21:30", [
                {"codigo": "whey_protein", "quantidade": 1}
            ])
        ]
        
        return self.construir_plano_completo(paciente, metas, refeicoes)

