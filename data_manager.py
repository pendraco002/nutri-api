"""
Data Manager - Módulo para gerenciamento de dados de alimentos
Padrão Pedro Barros - Versão Otimizada
"""

import json
from typing import Dict, List, Optional, Tuple

class DataManager:
    """Gerenciador de dados de alimentos com cache otimizado"""
    
    def __init__(self, database_path: str = "database.json"):
        self.database_path = database_path
        self._cache = {}
        self._load_database()
    
    def _load_database(self):
        """Carrega o banco de dados de alimentos"""
        try:
            with open(self.database_path, 'r', encoding='utf-8') as f:
                self._cache = json.load(f)
        except FileNotFoundError:
            # Database padrão com alimentos básicos
            self._cache = self._create_default_database()
            self._save_database()
    
    def _create_default_database(self) -> Dict:
        """Cria database padrão com alimentos essenciais"""
        return {
            "alimentos": {
                "ovo_galinha_inteiro": {
                    "nome": "Ovo de galinha inteiro",
                    "unidade": "Unidade (50g)",
                    "kcal_por_unidade": 77.49,
                    "proteina_g": 6.28,
                    "carboidrato_g": 0.36,
                    "gordura_g": 5.30,
                    "fibra_g": 0.0
                },
                "aveia_flocos": {
                    "nome": "Aveia em flocos",
                    "unidade": "Colher de sopa (15g)",
                    "kcal_por_unidade": 56.25,
                    "proteina_g": 2.25,
                    "carboidrato_g": 9.75,
                    "gordura_g": 1.05,
                    "fibra_g": 1.5
                },
                "banana_nanica": {
                    "nome": "Banana nanica",
                    "unidade": "Unidade média (86g)",
                    "kcal_por_unidade": 74.82,
                    "proteina_g": 1.29,
                    "carboidrato_g": 19.22,
                    "gordura_g": 0.09,
                    "fibra_g": 1.72
                },
                "whey_protein": {
                    "nome": "Whey Protein",
                    "unidade": "Scoop (30g)",
                    "kcal_por_unidade": 120.0,
                    "proteina_g": 24.0,
                    "carboidrato_g": 2.0,
                    "gordura_g": 1.0,
                    "fibra_g": 0.0
                }
            }
        }
    
    def _save_database(self):
        """Salva o database no arquivo"""
        with open(self.database_path, 'w', encoding='utf-8') as f:
            json.dump(self._cache, f, ensure_ascii=False, indent=2)
    
    def get_alimento(self, codigo: str) -> Optional[Dict]:
        """Retorna dados de um alimento específico"""
        return self._cache.get("alimentos", {}).get(codigo)
    
    def get_all_alimentos(self) -> Dict:
        """Retorna todos os alimentos disponíveis"""
        return self._cache.get("alimentos", {})
    
    def search_alimentos(self, termo: str) -> List[Tuple[str, Dict]]:
        """Busca alimentos por termo"""
        resultados = []
        termo_lower = termo.lower()
        
        for codigo, dados in self._cache.get("alimentos", {}).items():
            if termo_lower in dados["nome"].lower():
                resultados.append((codigo, dados))
        
        return resultados
    
    def calcular_macros(self, codigo: str, quantidade: float) -> Optional[Dict]:
        """Calcula macros para uma quantidade específica"""
        alimento = self.get_alimento(codigo)
        if not alimento:
            return None
        
        return {
            "nome": alimento["nome"],
            "unidade": alimento["unidade"],
            "quantidade": quantidade,
            "kcal": round(alimento["kcal_por_unidade"] * quantidade, 2),
            "proteina_g": round(alimento["proteina_g"] * quantidade, 2),
            "carboidrato_g": round(alimento["carboidrato_g"] * quantidade, 2),
            "gordura_g": round(alimento["gordura_g"] * quantidade, 2),
            "fibra_g": round(alimento["fibra_g"] * quantidade, 2)
        }
    
    def add_alimento(self, codigo: str, dados: Dict):
        """Adiciona novo alimento ao database"""
        if "alimentos" not in self._cache:
            self._cache["alimentos"] = {}
        
        self._cache["alimentos"][codigo] = dados
        self._save_database()
    
    def update_alimento(self, codigo: str, dados: Dict):
        """Atualiza dados de um alimento existente"""
        if codigo in self._cache.get("alimentos", {}):
            self._cache["alimentos"][codigo].update(dados)
            self._save_database()
            return True
        return False
    
    def delete_alimento(self, codigo: str):
        """Remove um alimento do database"""
        if codigo in self._cache.get("alimentos", {}):
            del self._cache["alimentos"][codigo]
            self._save_database()
            return True
        return False

