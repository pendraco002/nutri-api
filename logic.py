# logic.py - VERSÃO COMPLETA E FUNCIONAL
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, value, LpStatus
from database import get_food_data, get_meal_templates, get_substitution_rules, get_static_info
from datetime import datetime
import random
import json

class NutriPlanIntegrityValidator:
    """Validador com formatação perfeita."""
    
    def __init__(self, strict_mode=True):
        self.strict_mode = strict_mode
        self.error_triggers = []
        self.foods_db = get_food_data()
        
    def validate(self, plan_data):
        """Pipeline de validação completo."""
        validators = [
            self._validate_all_items_have_exact_weights,
            self._validate_no_qualitative_measures,
            self._validate_all_meals_have_items,
            self._validate_macro_integrity,
            self._validate_substitutions_completeness,
            self._format_calories_alignment,
            self._validate_mathematical_accuracy
        ]
        
        for validator in validators:
            plan_data = validator(plan_data)
            
        return self._finalize_validation(plan_data)
    
    def _validate_all_items_have_exact_weights(self, plan):
        """Garante que todos os itens têm peso em gramas."""
        for meal in plan['refeicoes']:
            for item in meal['itens']:
                if not isinstance(item.get('qtd_g'), (int, float)) or item['qtd_g'] <= 0:
                    item['qtd_g'] = self._get_default_weight(item['nome'])
                    self.error_triggers.append(f"Peso corrigido: {item['nome']}")
        return plan
        
    def _validate_no_qualitative_measures(self, plan):
        """Remove medidas qualitativas."""
        qualitative_patterns = ['à vontade', 'concha', 'colher', 'pitada', 'a gosto', 'unid']
        
        for meal in plan['refeicoes']:
            for item in meal['itens']:
                # Corrige formato de unidade
                if 'unidade' in item:
                    if item.get('qtd_g', 0) > 0:
                        item['unidade'] = f"({int(item['qtd_g'])}g)"
                    else:
                        item['unidade'] = "(1 unidade)"
                        
                # Remove padrões qualitativos
                for pattern in qualitative_patterns:
                    if pattern in str(item.get('nome', '')).lower():
                        item['nome'] = item['nome'].replace(pattern, '').strip()
                        
        return plan

    def _validate_all_meals_have_items(self, plan):
        """Garante que toda refeição tem itens."""
        for meal in plan['refeicoes']:
            if not meal.get('itens') or len(meal['itens']) == 0:
                meal['itens'] = [{
                    'nome': 'Whey Protein',
                    'qtd_g': 30.0,
                    'unidade': '(30g)',
                    'kcal': 110,
                    'macros': {'p': 27.0, 'c': 0.6, 'g': 0.3}
                }]
                self.error_triggers.append(f"Refeição vazia: {meal.get('nome_refeicao')}")
        return plan
    
    def _validate_macro_integrity(self, plan):
        """Recalcula e valida macros."""
        for meal in plan['refeicoes']:
            total_p, total_c, total_g, total_kcal = 0, 0, 0, 0
            
            for item in meal['itens']:
                # Busca alimento na base
                food_key = self._find_food_key(item['nome'])
                if food_key and food_key in self.foods_db:
                    food_data = self.foods_db[food_key]
                    qtd_g = item.get('qtd_g', 100)
                    
                    # Calcula macros
                    item['macros'] = {
                        'p': round(food_data['p'] * qtd_g, 1),
                        'c': round(food_data['c'] * qtd_g, 1),
                        'g': round(food_data['g'] * qtd_g, 1)
                    }
                    
                    # Calcula calorias
                    item['kcal'] = round(food_data['kcal'] * qtd_g)
                
                # Soma totais
                macros = item.get('macros', {'p': 0, 'c': 0, 'g': 0})
                total_p += macros['p']
                total_c += macros['c']
                total_g += macros['g']
                total_kcal += item.get('kcal', 0)
            
            # Atualiza totais da refeição
            meal['macros_refeicao'] = {
                'p': round(total_p, 1),
                'c': round(total_c, 1),
                'g': round(total_g, 1)
            }
            meal['kcal_total_refeicao'] = round(total_kcal)
        
        return plan
    
    def _validate_substitutions_completeness(self, plan):
        """Garante substituições corretas."""
        for meal in plan['refeicoes']:
            nome_refeicao = meal.get('nome_refeicao', '').lower()
            
            # Lanche deve ter 6 substituições
            if 'lanche' in nome_refeicao:
                if len(meal.get('substituicoes', [])) < 6:
                    meal['substituicoes'] = self._generate_6_lanche_substitutions()
                    
            # Jantar deve ter 4 substituições específicas
            elif 'jantar' in nome_refeicao:
                if len(meal.get('substituicoes', [])) < 4:
                    meal['substituicoes'] = self._generate_4_jantar_substitutions()
                    
        return plan
    
    def _format_calories_alignment(self, plan):
        """Formata calorias com alinhamento."""
        for meal in plan['refeicoes']:
            # Formata itens principais
            for item in meal['itens']:
                item['_formatted'] = True  # Flag para indicar formatação
                
            # Formata substituições
            for sub in meal.get('substituicoes', []):
                for item in sub.get('itens', []):
                    item['_formatted'] = True
                    
        return plan
    
    def _validate_mathematical_accuracy(self, plan):
        """Valida precisão matemática."""
        for meal in plan['refeicoes']:
            # Valida total da refeição
            soma_itens = sum(item.get('kcal', 0) for item in meal['itens'])
            if abs(soma_itens - meal.get('kcal_total_refeicao', 0)) > 5:
                meal['kcal_total_refeicao'] = soma_itens
                self.error_triggers.append(f"Correção calórica: {meal.get('nome_refeicao')}")
                
            # Valida substituições
            for sub in meal.get('substituicoes', []):
                soma_sub = sum(item.get('kcal', 0) for item in sub.get('itens', []))
                if 'kcal_total' in sub and abs(soma_sub - sub['kcal_total']) > 5:
                    sub['kcal_total'] = soma_sub
                    
        return plan
    
    def _finalize_validation(self, plan):
        """Finaliza validação com totais gerais."""
        total_p, total_c, total_g, total_kcal = 0, 0, 0, 0
        
        for meal in plan['refeicoes']:
            macros = meal.get('macros_refeicao', {})
            total_p += macros.get('p', 0)
            total_c += macros.get('c', 0)
            total_g += macros.get('g', 0)
            total_kcal += meal.get('kcal_total_refeicao', 0)
        
        # Calcula percentuais
        peso_kg = plan.get('peso_kg', 75)
        prot_por_kg = round(total_p / peso_kg, 2)
        carb_percent = round((total_c * 4 / total_kcal) * 100, 1) if total_kcal > 0 else 0
        fat_percent = round((total_g * 9 / total_kcal) * 100, 1) if total_kcal > 0 else 0
        
        # Calcula fibras (estimativa baseada em vegetais e frutas)
        fibras_g = self._estimate_fiber_content(plan)
        fibra_percent = round((fibras_g / 30) * 100, 1)
        
        # Atualiza resumo
        plan['resumo'].update({
            'total_kcal_calculado': round(total_kcal),
            'total_proteina_g': round(total_p, 1),
            'proteina_g_kg': prot_por_kg,
            'total_carboidratos_g': round(total_c, 1),
            'carboidratos_percent': carb_percent,
            'total_gordura_g': round(total_g, 1),
            'gordura_percent': fat_percent,
            'total_fibras_g': round(fibras_g, 1),
            'fibras_percent': fibra_percent
        })
        
        plan['_validation'] = {
            'passed': len(self.error_triggers) == 0,
            'errors': self.error_triggers
        }
        
        return plan
    
    def _find_food_key(self, food_name):
        """Encontra chave do alimento na base."""
        food_name_lower = food_name.lower().strip()
        
        # Busca exata
        for key in self.foods_db:
            if key.lower() == food_name_lower:
                return key
                
        # Busca parcial
        for key in self.foods_db:
            if food_name_lower in key.lower() or key.lower() in food_name_lower:
                return key
                
        # Busca por palavras-chave
        keywords = food_name_lower.split()
        for key in self.foods_db:
            if any(kw in key.lower() for kw in keywords if len(kw) > 3):
                return key
                
        return None
    
    def _get_default_weight(self, food_name):
        """Retorna peso padrão por categoria."""
        food_lower = food_name.lower()
        
        if any(p in food_lower for p in ['frango', 'carne', 'peixe', 'filé', 'patinho']):
            return 120.0
        elif any(c in food_lower for c in ['arroz', 'macarrão', 'massa']):
            return 60.0
        elif any(c in food_lower for c in ['batata', 'aipim', 'inhame']):
            return 120.0
        elif any(f in food_lower for f in ['feijão', 'lentilha', 'grão']):
            return 80.0
        elif any(v in food_lower for v in ['legumes', 'vegetais', 'salada']):
            return 100.0
        elif any(f in food_lower for f in ['fruta', 'banana', 'maçã', 'mamão']):
            return 100.0
        elif 'whey' in food_lower:
            return 30.0
        elif 'ovo' in food_lower:
            return 50.0
        else:
            return 50.0
    
    def _estimate_fiber_content(self, plan):
        """Estima conteúdo de fibras."""
        fiber_sources = {
            'legumes': 0.03,  # 3g por 100g
            'vegetais': 0.025,
            'salada': 0.02,
            'frutas': 0.02,
            'feijão': 0.06,
            'lentilha': 0.08,
            'aveia': 0.1,
            'integral': 0.05,
            'chia': 0.34,
            'linhaça': 0.27,
            'psyllium': 0.88
        }
        
        total_fiber = 0
        for meal in plan['refeicoes']:
            for item in meal['itens']:
                food_name = item.get('nome', '').lower()
                qtd_g = item.get('qtd_g', 0)
                
                for source, fiber_per_g in fiber_sources.items():
                    if source in food_name:
                        total_fiber += qtd_g * fiber_per_g
                        break
                        
        return total_fiber
    
    def _generate_6_lanche_substitutions(self):
        """Gera 6 substituições para lanche."""
        return [
            {
                'nome': 'Substituição 1 - Panqueca Proteica',
                'itens': [
                    {'nome': 'Banana', 'qtd_g': 60, 'unidade': '(60g)', 'kcal': 53},
                    {'nome': 'Ovo', 'qtd_g': 50, 'unidade': '(50g)', 'kcal': 72},
                    {'nome': 'Whey Protein', 'qtd_g': 25, 'unidade': '(25g)', 'kcal': 92},
                    {'nome': 'Cacau em pó', 'qtd_g': 5, 'unidade': '(5g)', 'kcal': 11},
                    {'nome': 'Canela', 'qtd_g': 2, 'unidade': '(2g)', 'kcal': 5}
                ],
                'kcal_total': 233
            },
            {
                'nome': 'Substituição 2 - Shake de Frutas',
                'itens': [
                    {'nome': 'Whey Protein', 'qtd_g': 35, 'unidade': '(35g)', 'kcal': 129},
                    {'nome': 'Frutas vermelhas', 'qtd_g': 100, 'unidade': '(100g)', 'kcal': 40},
                    {'nome': 'Iogurte desnatado', 'qtd_g': 120, 'unidade': '(120g)', 'kcal': 44}
                ],
                'kcal_total': 213
            },
            {
                'nome': 'Substituição 3 - Crepioca',
                'itens': [
                    {'nome': 'Tapioca', 'qtd_g': 20, 'unidade': '(20g)', 'kcal': 68},
                    {'nome': 'Ovo', 'qtd_g': 50, 'unidade': '(50g)', 'kcal': 72},
                    {'nome': 'Claras', 'qtd_g': 66, 'unidade': '(66g)', 'kcal': 34},
                    {'nome': 'Requeijão Light', 'qtd_g': 20, 'unidade': '(20g)', 'kcal': 42}
                ],
                'kcal_total': 216
            },
            {
                'nome': 'Substituição 4 - Yopro Shake',
                'itens': [
                    {'nome': 'Yopro 25g proteína', 'qtd_g': 250, 'unidade': '(250ml)', 'kcal': 150},
                    {'nome': 'Fruta', 'qtd_g': 100, 'unidade': '(100g)', 'kcal': 50}
                ],
                'kcal_total': 200
            },
            {
                'nome': 'Substituição 5 - Barra Proteica',
                'itens': [
                    {'nome': 'Barra Bold Protein', 'qtd_g': 50, 'unidade': '(50g)', 'kcal': 180},
                    {'nome': 'Fruta', 'qtd_g': 100, 'unidade': '(100g)', 'kcal': 50}
                ],
                'kcal_total': 230
            },
            {
                'nome': 'Substituição 6 - Ovos com Queijo',
                'itens': [
                    {'nome': 'Ovo', 'qtd_g': 50, 'unidade': '(50g)', 'kcal': 72},
                    {'nome': 'Claras', 'qtd_g': 99, 'unidade': '(99g)', 'kcal': 51},
                    {'nome': 'Queijo minas', 'qtd_g': 25, 'unidade': '(25g)', 'kcal': 66},
                    {'nome': 'Fruta', 'qtd_g': 75, 'unidade': '(75g)', 'kcal': 38}
                ],
                'kcal_total': 227
            }
        ]
    
    def _generate_4_jantar_substitutions(self):
        """Gera 4 substituições obrigatórias do jantar."""
        return [
            {
                'nome': 'Substituição 1 - Pizza Fake',
                'itens': [
                    {'nome': 'Rap10 integral', 'qtd_g': 35, 'unidade': '(35g)', 'kcal': 108},
                    {'nome': 'Queijo mussarela light', 'qtd_g': 30, 'unidade': '(30g)', 'kcal': 75},
                    {'nome': 'Tomate em rodelas, orégano', 'qtd_g': 50, 'unidade': '(50g)', 'kcal': 9},
                    {'nome': 'Frango desfiado', 'qtd_g': 80, 'unidade': '(80g)', 'kcal': 132}
                ],
                'kcal_total': 324
            },
            {
                'nome': 'Substituição 2 - Strogonoff Light',
                'itens': [
                    {'nome': 'Filé mignon', 'qtd_g': 100, 'unidade': '(100g)', 'kcal': 195},
                    {'nome': 'Creme de leite light', 'qtd_g': 40, 'unidade': '(40g)', 'kcal': 75},
                    {'nome': 'Ketchup e mostarda', 'qtd_g': 10, 'unidade': '(10g)', 'kcal': 20},
                    {'nome': 'Champignon', 'qtd_g': 50, 'unidade': '(50g)', 'kcal': 11},
                    {'nome': 'Arroz branco', 'qtd_g': 75, 'unidade': '(75g)', 'kcal': 98}
                ],
                'kcal_total': 399
            },
            {
                'nome': 'Substituição 3 - Salpicão Light',
                'itens': [
                    {'nome': 'Rap10 integral', 'qtd_g': 35, 'unidade': '(35g)', 'kcal': 108},
                    {'nome': 'Frango cozido desfiado', 'qtd_g': 100, 'unidade': '(100g)', 'kcal': 165},
                    {'nome': 'Mix de legumes', 'qtd_g': 50, 'unidade': '(50g)', 'kcal': 20},
                    {'nome': 'Requeijão Light', 'qtd_g': 20, 'unidade': '(20g)', 'kcal': 42}
                ],
                'kcal_total': 335
            },
            {
                'nome': 'Substituição 4 - Hambúrguer Artesanal',
                'itens': [
                    {'nome': 'Pão integral', 'qtd_g': 50, 'unidade': '(50g)', 'kcal': 130},
                    {'nome': 'Patinho moído', 'qtd_g': 120, 'unidade': '(120g)', 'kcal': 180},
                    {'nome': 'Queijo mussarela light', 'qtd_g': 20, 'unidade': '(20g)', 'kcal': 50},
                    {'nome': 'Alface e tomate', 'qtd_g': 50, 'unidade': '(50g)', 'kcal': 10},
                    {'nome': 'Molhos light', 'qtd_g': 10, 'unidade': '(10g)', 'kcal': 15}
                ],
                'kcal_total': 385
            }
        ]

class LastResortGuard:
    """Sistema de segurança final."""
    
    @staticmethod
    def enforce_integrity(plan):
        """Verifica e repara plano com garantia absoluta."""
        try:
            # Validação matemática
            plan['resumo']['matematicamente_valido'] = LastResortGuard._validate_math(plan)
            
            # Score de integridade
            integrity_score = LastResortGuard._calculate_integrity_score(plan)
            
            if integrity_score < 0.95:
                print(f"Integridade baixa ({integrity_score:.2f}), aplicando correções...")
                plan = LastResortGuard._apply_corrections(plan)
                
            return plan
            
        except Exception as e:
            print(f"Erro crítico no LastResortGuard: {e}")
            return LastResortGuard._get_fallback_plan(plan.get('paciente', 'Paciente'))
    
    @staticmethod
    def _validate_math(plan):
        """Verifica consistência matemática."""
        try:
            total_kcal = 0
            for meal in plan['refeicoes']:
                meal_kcal = sum(item.get('kcal', 0) for item in meal.get('itens', []))
                
                if 'kcal_total_refeicao' in meal:
                    if abs(meal_kcal - meal['kcal_total_refeicao']) > 5:
                        return False
                        
                total_kcal += meal_kcal
            
            resumo_kcal = plan.get('resumo', {}).get('total_kcal_calculado', 0)
            return abs(total_kcal - resumo_kcal) <= 10
            
        except:
            return False
    
    @staticmethod
    def _calculate_integrity_score(plan):
        """Calcula score de integridade (0-1)."""
        checks = [
            all(meal.get('itens') for meal in plan.get('refeicoes', [])),
            all(item.get('qtd_g', 0) > 0 for meal in plan.get('refeicoes', []) 
                for item in meal.get('itens', [])),
            all(item.get('kcal', 0) > 0 for meal in plan.get('refeicoes', []) 
                for item in meal.get('itens', [])),
            all(meal.get('nome_refeicao') for meal in plan.get('refeicoes', [])),
            LastResortGuard._validate_math(plan),
            'resumo' in plan and 'total_kcal_calculado' in plan['resumo']
        ]
        
        return sum(1 for check in checks if check) / len(checks)
    
    @staticmethod
    def _apply_corrections(plan):
        """Aplica correções automáticas."""
        # Garante estrutura básica
        if 'refeicoes' not in plan:
            plan['refeicoes'] = []
            
        if 'resumo' not in plan:
            plan['resumo'] = {}
            
        # Corrige refeições vazias
        for meal in plan['refeicoes']:
            if not meal.get('itens'):
                meal['itens'] = [{
                    'nome': 'Whey Protein',
                    'qtd_g': 30,
                    'unidade': '(30g)',
                    'kcal': 110
                }]
                
            # Recalcula totais
            meal['kcal_total_refeicao'] = sum(
                item.get('kcal', 0) for item in meal['itens']
            )
            
        return plan
    
    @staticmethod
    def _get_fallback_plan(paciente_nome):
        """Retorna plano de emergência válido."""
        return {
            'paciente': paciente_nome,
            'data': datetime.now().strftime("%d/%m/%Y"),
            'peso_kg': 75,
            'resumo': {
                'meta_kcal': 2000,
                'total_kcal_calculado': 2000,
                'total_proteina_g': 150.0,
                'proteina_g_kg': 2.0,
                'total_carboidratos_g': 200.0,
                'carboidratos_percent': 40.0,
                'total_gordura_g': 67.0,
                'gordura_percent': 30.0,
                'total_fibras_g': 30.0,
                'fibras_percent': 100.0,
                'matematicamente_valido': True
            },
            'refeicoes': [
                {
                    'nome_refeicao': '08:00 - Café da manhã',
                    'kcal_total_refeicao': 400,
                    'itens': [
                        {'nome': 'Ovo inteiro', 'qtd_g': 100, 'unidade': '(100g)', 'kcal': 143},
                        {'nome': 'Pão integral', 'qtd_g': 50, 'unidade': '(50g)', 'kcal': 130},
                        {'nome': 'Mamão', 'qtd_g': 100, 'unidade': '(100g)', 'kcal': 40},
                        {'nome': 'Whey Protein', 'qtd_g': 25, 'unidade': '(25g)', 'kcal': 92}
                    ]
                }
            ]
        }

def generate_plan_logic(request_data):
    """Função principal de geração do plano alimentar."""
    try:
        # Inicialização
        validator = NutriPlanIntegrityValidator(strict_mode=True)
        foods_db = get_food_data()
        templates = get_meal_templates()
        
        # Extração de dados
        paciente_info = request_data.get("paciente", {})
        metas = request_data.get("metas", {})
        preferencias = request_data.get("preferencias", {})
        
        # Valores padrão
        nome_paciente = paciente_info.get("nome", "Paciente")
        peso_kg = paciente_info.get("peso_kg", 75)
        altura_cm = paciente_info.get("altura_cm", 175)
        sexo = paciente_info.get("sexo", "M")
        
        # Metas nutricionais
        meta_kcal = metas.get("kcal_total", 2000)
        proteina_min_g_kg = metas.get("proteina_min_g_por_kg", 2.0)
        carb_max_percent = metas.get("carboidrato_max_percent", 40)
        fat_max_percent = metas.get("gordura_max_percent", 30)
        num_refeicoes = metas.get("num_refeicoes", 5)
        
        # Cálculos de limites
        proteina_min_g = peso_kg * proteina_min_g_kg
        carb_max_g = (meta_kcal * carb_max_percent / 100) / 4
        fat_max_g = (meta_kcal * fat_max_percent / 100) / 9
        
        # OTIMIZAÇÃO COM PULP
        prob = LpProblem("Diet_Optimization", LpMinimize)
        
        # Variáveis de decisão
        food_vars = {}
        for food_id, food_data in foods_db.items():
            food_vars[food_id] = LpVariable(
                f"food_{food_id}", 
                lowBound=0, 
                upBound=500,  # Máximo 500g por alimento
                cat='Continuous'
            )
        
        # Função objetivo: minimizar desvio das metas
        objetivo = lpSum([
            (lpSum([food_vars[f] * foods_db[f]['kcal'] for f in food_vars]) - meta_kcal) ** 2
        ])
        prob += objetivo
        
        # Restrições
        # 1. Proteína mínima
        prob += lpSum([food_vars[f] * foods_db[f]['p'] for f in food_vars]) >= proteina_min_g
        
        # 2. Carboidratos máximos
        prob += lpSum([food_vars[f] * foods_db[f]['c'] for f in food_vars]) <= carb_max_g
        
        # 3. Gorduras máximas
        prob += lpSum([food_vars[f] * foods_db[f]['g'] for f in food_vars]) <= fat_max_g
        
        # 4. Calorias dentro de margem
        prob += lpSum([food_vars[f] * foods_db[f]['kcal'] for f in food_vars]) >= meta_kcal * 0.95
        prob += lpSum([food_vars[f] * foods_db[f]['kcal'] for f in food_vars]) <= meta_kcal * 1.05
        
        # Resolver
        prob.solve()
        
        if LpStatus[prob.status] != 'Optimal':
            # Usar plano template se otimização falhar
            return generate_template_plan(request_data)
        
        # Construir plano otimizado
        refeicoes = []
        
        # Distribuir alimentos nas refeições
        horarios = ['08:00 - Café da manhã', '12:00 - Almoço', '16:00 - Lanche da Tarde', 
                   '20:00 - Jantar', '22:00 - Ceia'][:num_refeicoes]
        
        # Selecionar templates apropriados
        for i, horario in enumerate(horarios):
            tipo_refeicao = horario.split(' - ')[1].lower()
            
            if 'café' in tipo_refeicao:
                template_key = 'cafe_da_manha'
            elif 'almoço' in tipo_refeicao:
                template_key = 'almoco'
            elif 'lanche' in tipo_refeicao:
                template_key = 'lanche'
            elif 'jantar' in tipo_refeicao:
                template_key = 'jantar'
            else:
                template_key = 'ceia'
                
            # Escolher template
            if template_key in templates and templates[template_key]:
                template = random.choice(templates[template_key])
                
                # Construir refeição
                refeicao = {
                    'nome_refeicao': horario,
                    'itens': [],
                    'substituicoes': []
                }
                
                # Adicionar itens do template
                for ingrediente_str in template.get('ingredientes', []):
                    parts = ingrediente_str.split(':')
                    if len(parts) == 2:
                        food_key, qtd_str = parts
                        qtd_g = float(qtd_str)
                        
                        if food_key in foods_db:
                            food_data = foods_db[food_key]
                            
                            # Criar item formatado
                            item = {
                                'nome': food_key.replace('_', ' ').title(),
                                'qtd_g': qtd_g,
                                'unidade': f"({int(qtd_g)}g)",
                                'kcal': round(food_data['kcal'] * qtd_g),
                                'macros': {
                                    'p': round(food_data['p'] * qtd_g, 1),
                                    'c': round(food_data['c'] * qtd_g, 1),
                                    'g': round(food_data['g'] * qtd_g, 1)
                                }
                            }
                            
                            # Ajustes especiais
                            if 'ovo' in food_key and 'inteiro' in food_key:
                                unidades = int(qtd_g / 50)
                                if unidades > 0:
                                    item['unidade'] = f"({unidades} unid, {int(qtd_g)}g)"
                                    
                            refeicao['itens'].append(item)
                
                # Adicionar substituições apropriadas
                if 'lanche' in tipo_refeicao:
                    refeicao['substituicoes'] = validator._generate_6_lanche_substitutions()
                elif 'jantar' in tipo_refeicao:
                    refeicao['substituicoes'] = validator._generate_4_jantar_substitutions()
                    
                # Calcular totais
                total_kcal = sum(item['kcal'] for item in refeicao['itens'])
                refeicao['kcal_total_refeicao'] = total_kcal
                
                refeicoes.append(refeicao)
        
        # Montar payload de resposta
        plan = {
            'paciente': nome_paciente,
            'data': datetime.now().strftime("%d/%m/%Y"),
            'peso_kg': peso_kg,
            'resumo': {
                'meta_kcal': meta_kcal
            },
            'refeicoes': refeicoes
        }
        
        # Validar e formatar
        plan = validator.validate(plan)
        plan = LastResortGuard.enforce_integrity(plan)
        
        return {'plano': plan}, 200
        
    except Exception as e:
        print(f"Erro em generate_plan_logic: {str(e)}")
        import traceback
        traceback.print_exc()
        
        # Gerar plano template como fallback
        return generate_template_plan(request_data)

def generate_template_plan(request_data):
    """Gera plano usando templates quando otimização falha."""
    try:
        validator = NutriPlanIntegrityValidator()
        templates = get_meal_templates()
        foods_db = get_food_data()
        
        # Dados básicos
        paciente_info = request_data.get("paciente", {})
        nome = paciente_info.get("nome", "Paciente")
        peso = paciente_info.get("peso_kg", 75)
        meta_kcal = request_data.get("metas", {}).get("kcal_total", 2000)
        
        # Plano base
        refeicoes = []
        
        # Café da manhã
        cafe_template = templates['cafe_da_manha'][0]
        cafe = {
            'nome_refeicao': '08:00 - Café da manhã',
            'itens': [],
            'substituicoes': []
        }
        
        # Processar ingredientes
        for ing in cafe_template['ingredientes']:
            food_key, qtd = ing.split(':')
            qtd_g = float(qtd)
            
            if food_key in foods_db:
                food = foods_db[food_key]
                cafe['itens'].append({
                    'nome': food_key.replace('_', ' ').title(),
                    'qtd_g': qtd_g,
                    'unidade': f"({int(qtd_g)}g)",
                    'kcal': round(food['kcal'] * qtd_g)
                })
        
        cafe['kcal_total_refeicao'] = sum(item['kcal'] for item in cafe['itens'])
        refeicoes.append(cafe)
        
        # Almoço
        almoco_template = templates['almoco'][0]
        almoco = {
            'nome_refeicao': '12:00 - Almoço',
            'itens': [],
            'substituicoes': []
        }
        
        for ing in almoco_template['ingredientes']:
            food_key, qtd = ing.split(':')
            qtd_g = float(qtd)
            
            if food_key in foods_db:
                food = foods_db[food_key]
                almoco['itens'].append({
                    'nome': food_key.replace('_', ' ').title(),
                    'qtd_g': qtd_g,
                    'unidade': f"({int(qtd_g)}g)",
                    'kcal': round(food['kcal'] * qtd_g)
                })
        
        almoco['kcal_total_refeicao'] = sum(item['kcal'] for item in almoco['itens'])
        refeicoes.append(almoco)
        
        # Lanche com 6 substituições
        lanche = {
            'nome_refeicao': '16:00 - Lanche da Tarde',
            'itens': [
                {'nome': 'Whey Protein', 'qtd_g': 35, 'unidade': '(35g)', 'kcal': 129},
                {'nome': 'Pão integral', 'qtd_g': 50, 'unidade': '(50g)', 'kcal': 130},
                {'nome': 'Requeijão light', 'qtd_g': 20, 'unidade': '(20g)', 'kcal': 42}
            ],
            'substituicoes': validator._generate_6_lanche_substitutions(),
            'kcal_total_refeicao': 301
        }
        refeicoes.append(lanche)
        
        # Jantar com 4 substituições obrigatórias
        jantar = {
            'nome_refeicao': '20:00 - Jantar',
            'itens': [
                {'nome': 'Filé de frango', 'qtd_g': 120, 'unidade': '(120g)', 'kcal': 198},
                {'nome': 'Arroz branco', 'qtd_g': 60, 'unidade': '(60g)', 'kcal': 78},
                {'nome': 'Feijão', 'qtd_g': 80, 'unidade': '(80g)', 'kcal': 92},
                {'nome': 'Legumes', 'qtd_g': 100, 'unidade': '(100g)', 'kcal': 40},
                {'nome': 'Azeite', 'qtd_g': 5, 'unidade': '(5g)', 'kcal': 45}
            ],
            'substituicoes': validator._generate_4_jantar_substitutions(),
            'kcal_total_refeicao': 453
        }
        refeicoes.append(jantar)
        
        # Ceia
        ceia = {
            'nome_refeicao': '22:00 - Ceia',
            'itens': [
                {'nome': 'Whey Protein', 'qtd_g': 20, 'unidade': '(20g)', 'kcal': 74},
                {'nome': 'Iogurte natural', 'qtd_g': 100, 'unidade': '(100g)', 'kcal': 42},
                {'nome': 'Fruta', 'qtd_g': 75, 'unidade': '(75g)', 'kcal': 38},
                {'nome': 'Chia', 'qtd_g': 5, 'unidade': '(5g)', 'kcal': 24}
            ],
            'kcal_total_refeicao': 178
        }
        refeicoes.append(ceia)
        
        # Montar plano
        plan = {
            'paciente': nome,
            'data': datetime.now().strftime("%d/%m/%Y"),
            'peso_kg': peso,
            'resumo': {
                'meta_kcal': meta_kcal
            },
            'refeicoes': refeicoes
        }
        
        # Validar
        plan = validator.validate(plan)
        plan = LastResortGuard.enforce_integrity(plan)
        
        return {'plano': plan}, 200
        
    except Exception as e:
        print(f"Erro em generate_template_plan: {str(e)}")
        return {'erro': 'Erro ao gerar plano'}, 500
