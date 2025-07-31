# logic.py - VERSÃO INTELIGENTE PEDRO BARROS
from database import get_food_data, get_meal_templates, get_substitution_rules, get_static_info
from datetime import datetime
import re
import json

class SmartInputParser:
    """Parser inteligente que entende diferentes formatos de input."""
    
    def __init__(self):
        self.patterns = {
            'peso': r'(\d+(?:\.\d+)?)\s*kg',
            'altura': r'(\d+(?:\.\d+)?)\s*(?:m|cm)',
            'proteina': r'(?:proteína|ptn).*?(\d+(?:\.\d+)?)\s*g/kg',
            'calorias': r'(\d+)\s*kcal',
            'carboidrato': r'(?:carbo|carboidrato).*?(\d+)\s*%',
            'gordura': r'gordura.*?(\d+)\s*%',
            'genero': r'(homem|mulher|masculino|feminino)',
            'refeicoes': r'(\d+)\s*refeiç(?:ão|ões)',
            'pre_treino': r'pré[\s-]?treino.*?(\d+)\s*kcal'
        }
    
    def parse(self, input_text):
        """Extrai informações de qualquer formato de input."""
        # Normaliza texto
        text = input_text.lower().strip()
        
        # Estrutura base
        parsed = {
            'paciente': {},
            'metas': {},
            'regras_especiais': [],
            'refeicoes_config': []
        }
        
        # Extrai dados básicos
        self._extract_basic_info(text, parsed)
        
        # Extrai metas nutricionais
        self._extract_nutritional_goals(text, parsed)
        
        # Extrai configuração de refeições
        self._extract_meal_configuration(text, parsed)
        
        # Extrai regras especiais
        self._extract_special_rules(text, parsed)
        
        return parsed
    
    def _extract_basic_info(self, text, parsed):
        """Extrai informações básicas do paciente."""
        # Nome
        if 'nome:' in text:
            nome_match = re.search(r'nome:\s*([^\n]+)', text)
            if nome_match:
                parsed['paciente']['nome'] = nome_match.group(1).strip()
        
        # Peso
        peso_match = re.search(self.patterns['peso'], text)
        if peso_match:
            parsed['paciente']['peso_kg'] = float(peso_match.group(1))
        
        # Altura
        altura_match = re.search(self.patterns['altura'], text)
        if altura_match:
            altura = float(altura_match.group(1))
            if altura < 3:  # Está em metros
                parsed['paciente']['altura_cm'] = altura * 100
            else:
                parsed['paciente']['altura_cm'] = altura
        
        # Gênero
        genero_match = re.search(self.patterns['genero'], text)
        if genero_match:
            genero = genero_match.group(1)
            parsed['paciente']['sexo'] = 'F' if genero in ['mulher', 'feminino'] else 'M'
    
    def _extract_nutritional_goals(self, text, parsed):
        """Extrai metas nutricionais."""
        # Calorias
        cal_match = re.search(self.patterns['calorias'], text)
        if cal_match:
            parsed['metas']['kcal_total'] = int(cal_match.group(1))
        
        # Proteína
        ptn_match = re.search(self.patterns['proteina'], text)
        if ptn_match:
            parsed['metas']['proteina_min_g_por_kg'] = float(ptn_match.group(1))
        
        # Carboidrato
        carb_match = re.search(self.patterns['carboidrato'], text)
        if carb_match:
            parsed['metas']['carboidrato_max_percent'] = int(carb_match.group(1))
        
        # Gordura
        fat_match = re.search(self.patterns['gordura'], text)
        if fat_match:
            parsed['metas']['gordura_max_percent'] = int(fat_match.group(1))
    
    def _extract_meal_configuration(self, text, parsed):
        """Extrai configuração específica de refeições."""
        # Detecta refeições mencionadas
        refeicoes = []
        
        # Padrões de refeições
        meal_patterns = {
            'cafe': r'café\s*(?:da\s*)?manhã',
            'almoco': r'almoço',
            'lanche': r'lanche',
            'pre_treino': r'pré[\s-]?treino',
            'jantar': r'jantar',
            'ceia': r'ceia|sobremesa'
        }
        
        # Verifica ordem das refeições se especificada
        if 'refeição 1' in text:
            # Formato numerado
            for i in range(1, 7):
                match = re.search(rf'refeição\s*{i}\s*[:\-]?\s*([^\n]+)', text)
                if match:
                    refeicao_nome = match.group(1).strip()
                    refeicoes.append({
                        'ordem': i,
                        'nome': refeicao_nome,
                        'config': self._extract_meal_specifics(text, refeicao_nome)
                    })
        else:
            # Detecta refeições mencionadas
            for tipo, pattern in meal_patterns.items():
                if re.search(pattern, text):
                    refeicoes.append({
                        'tipo': tipo,
                        'nome': tipo.replace('_', ' ').title()
                    })
        
        parsed['refeicoes_config'] = refeicoes
    
    def _extract_special_rules(self, text, parsed):
        """Extrai regras especiais do plano."""
        regras = []
        
        # Proteína > Carboidrato
        if 'ptn igual ou maior que carbo' in text or 'proteína igual ou maior que carbo' in text:
            regras.append('proteina_maior_carbo')
        
        # Última refeição maior
        if 'última refeição' in text and 'maior' in text:
            regras.append('ultima_refeicao_maior')
        
        # Hambúrguer no jantar
        if 'hambúrguer' in text and 'jantar' in text:
            regras.append('hamburguer_jantar')
        
        # Pré-treino só carbo
        if 'pré' in text and 'só carbo' in text:
            regras.append('pre_treino_so_carbo')
        
        parsed['regras_especiais'] = regras
    
    def _extract_meal_specifics(self, text, meal_name):
        """Extrai configurações específicas de uma refeição."""
        config = {}
        
        # Verifica calorias específicas
        cal_pattern = rf'{meal_name}.*?(\d+)\s*kcal'
        cal_match = re.search(cal_pattern, text, re.IGNORECASE)
        if cal_match:
            config['kcal'] = int(cal_match.group(1))
        
        # Verifica menções específicas
        if 'hambúrguer' in meal_name.lower():
            config['tipo'] = 'hamburguer_artesanal'
        elif 'pré' in meal_name.lower():
            config['tipo'] = 'pre_treino'
        
        return config

class PedroBarrosRulesEngine:
    """Motor de regras nutricionais do Pedro Barros."""
    
    def __init__(self):
        self.foods_db = get_food_data()
        self.templates = get_meal_templates()
    
    def create_meal_plan(self, parsed_input):
        """Cria plano de refeições baseado no input parseado."""
        # Extrai dados
        paciente = parsed_input['paciente']
        metas = parsed_input['metas']
        regras = parsed_input['regras_especiais']
        config_refeicoes = parsed_input['refeicoes_config']
        
        # Calcula necessidades
        peso = paciente.get('peso_kg', 75)
        kcal_total = metas.get('kcal_total', 2000)
        ptn_g_kg = metas.get('proteina_min_g_por_kg', 2.0)
        
        # Calcula macros
        proteina_total = peso * ptn_g_kg
        carb_max_percent = metas.get('carboidrato_max_percent', 40)
        fat_max_percent = metas.get('gordura_max_percent', 30)
        
        carb_max_g = (kcal_total * carb_max_percent / 100) / 4
        fat_max_g = (kcal_total * fat_max_percent / 100) / 9
        
        # Define estrutura de refeições
        if config_refeicoes:
            refeicoes = self._create_custom_meals(config_refeicoes, kcal_total, regras)
        else:
            refeicoes = self._create_default_meals(kcal_total)
        
        # Distribui macros
        refeicoes = self._distribute_macros(refeicoes, proteina_total, carb_max_g, fat_max_g, regras)
        
        # Aplica regras especiais
        if 'hamburguer_jantar' in regras:
            self._apply_hamburguer_jantar(refeicoes)
        
        if 'pre_treino_so_carbo' in regras:
            self._apply_pre_treino_carbo(refeicoes)
        
        return refeicoes
    
    def _create_custom_meals(self, config_refeicoes, kcal_total, regras):
        """Cria refeições customizadas baseadas na configuração."""
        refeicoes = []
        
        # Calcula distribuição de calorias
        num_refeicoes = len(config_refeicoes)
        
        for i, config in enumerate(config_refeicoes):
            refeicao = {
                'nome': config.get('nome', f'Refeição {i+1}'),
                'ordem': config.get('ordem', i+1),
                'tipo': config.get('tipo', 'padrao')
            }
            
            # Define calorias
            if 'kcal' in config.get('config', {}):
                refeicao['kcal_target'] = config['config']['kcal']
            else:
                # Distribuição inteligente
                if 'ultima_refeicao_maior' in regras and i == num_refeicoes - 1:
                    refeicao['kcal_target'] = int(kcal_total * 0.35)
                else:
                    remaining = kcal_total - sum(r.get('kcal_target', 0) for r in refeicoes)
                    remaining_meals = num_refeicoes - i
                    refeicao['kcal_target'] = int(remaining / remaining_meals)
            
            refeicoes.append(refeicao)
        
        return refeicoes
    
    def _create_default_meals(self, kcal_total):
        """Cria estrutura padrão de 5 refeições."""
        return [
            {'nome': 'Café da manhã', 'hora': '08:00', 'kcal_target': int(kcal_total * 0.20)},
            {'nome': 'Almoço', 'hora': '12:00', 'kcal_target': int(kcal_total * 0.25)},
            {'nome': 'Lanche da tarde', 'hora': '16:00', 'kcal_target': int(kcal_total * 0.20)},
            {'nome': 'Jantar', 'hora': '20:00', 'kcal_target': int(kcal_total * 0.25)},
            {'nome': 'Ceia', 'hora': '22:00', 'kcal_target': int(kcal_total * 0.10)}
        ]
    
    def _distribute_macros(self, refeicoes, proteina_total, carb_max_g, fat_max_g, regras):
        """Distribui macronutrientes entre as refeições."""
        for refeicao in refeicoes:
            kcal = refeicao['kcal_target']
            
            # Regra: proteína >= carboidrato
            if 'proteina_maior_carbo' in regras and refeicao.get('tipo') != 'pre_treino':
                # 40% proteína, 35% carbo, 25% gordura
                refeicao['macros_target'] = {
                    'proteina': (kcal * 0.40) / 4,
                    'carbo': (kcal * 0.35) / 4,
                    'gordura': (kcal * 0.25) / 9
                }
            elif refeicao.get('tipo') == 'pre_treino':
                # Pré-treino: 90% carbo, 10% proteína
                refeicao['macros_target'] = {
                    'proteina': (kcal * 0.10) / 4,
                    'carbo': (kcal * 0.90) / 4,
                    'gordura': 0
                }
            else:
                # Distribuição padrão
                refeicao['macros_target'] = {
                    'proteina': proteina_total / len(refeicoes),
                    'carbo': carb_max_g / len(refeicoes),
                    'gordura': fat_max_g / len(refeicoes)
                }
        
        return refeicoes

class DynamicPlanFormatter:
    """Formatador dinâmico que mantém o estilo Pedro Barros."""
    
    def __init__(self):
        self.formatter = PedroBarrosFormatter()
        self.generator = NutriPlanPedroBarros()
    
    def format_complete_plan(self, parsed_input, meal_plan):
        """Formata o plano completo no estilo Pedro Barros."""
        # Cabeçalho
        nome = parsed_input['paciente'].get('nome', 'Paciente')
        data = datetime.now().strftime("%d/%m/%Y")
        output = self.formatter.format_header(nome, data)
        
        # Formata cada refeição
        for refeicao in meal_plan:
            # Horário flexível ou nome direto
            if 'hora' in refeicao:
                header = f"{refeicao['hora']} - {refeicao['nome']}"
            else:
                header = refeicao['nome']
            
            output += f"\n  {header}                                                                                            Kcal"
            
            # Gera itens baseado no tipo
            items = self._generate_meal_items(refeicao, parsed_input)
            output += self.generator.format_meal_items(items)
            
            # Adiciona observações apropriadas
            output += self._get_meal_observations(refeicao)
            
            # Adiciona substituições se aplicável
            if refeicao['nome'].lower() in ['lanche', 'lanche da tarde']:
                output += self._format_lanche_substitutions()
            elif refeicao['nome'].lower() == 'jantar':
                output += self._format_jantar_substitutions()
        
        # Rodapé
        output += self.formatter.format_footer()
        
        return output
    
    def _generate_meal_items(self, refeicao, parsed_input):
        """Gera itens específicos para cada refeição."""
        # Aqui você implementaria a lógica para gerar
        # os alimentos específicos baseados nos targets
        # Por enquanto, retorna exemplo
        return []
    
    def _get_meal_observations(self, refeicao):
        """Retorna observações apropriadas para a refeição."""
        nome_lower = refeicao['nome'].lower()
        
        if 'almoço' in nome_lower or 'jantar' in nome_lower:
            return "\n" + PedroBarrosFormatter.format_obs_almoco_jantar()
        elif 'café' in nome_lower:
            return "\nObs: Substituições:\n- 1 fatia de pão forma por: 20g de tapioca ou 2 biscoitos de arroz grandes ou 15g de aveia ou meio pão francês (sem miolo)."
        else:
            return ""
    
    def _format_lanche_substitutions(self):
        """Formata as 6 substituições do lanche."""
        # Implementar formatação das substituições
        return ""
    
    def _format_jantar_substitutions(self):
        """Formata as 4 substituições do jantar."""
        # Implementar formatação das substituições
        return ""

# Nova função principal que usa o sistema inteligente
def generate_plan_logic(request_data):
    """Função principal com IA para interpretar e gerar planos."""
    try:
        # Se for texto direto, parseia
        if isinstance(request_data, str):
            parser = SmartInputParser()
            parsed_input = parser.parse(request_data)
        else:
            # Já está estruturado
            parsed_input = request_data
        
        # Cria plano de refeições
        rules_engine = PedroBarrosRulesEngine()
        meal_plan = rules_engine.create_meal_plan(parsed_input)
        
        # Formata no estilo Pedro Barros
        formatter = DynamicPlanFormatter()
        formatted_plan = formatter.format_complete_plan(parsed_input, meal_plan)
        
        # Resposta estruturada
        response = {
            'plano': {
                'paciente': parsed_input['paciente'].get('nome', 'Paciente'),
                'data': datetime.now().strftime("%d/%m/%Y"),
                'peso_kg': parsed_input['paciente'].get('peso_kg', 75),
                'plano_formatado': formatted_plan,
                'parsed_input': parsed_input,  # Para debug
                'meal_plan': meal_plan  # Para debug
            }
        }
        
        return response, 200
        
    except Exception as e:
        print(f"Erro ao gerar plano: {str(e)}")
        import traceback
        traceback.print_exc()
        return {'erro': str(e)}, 500

# Mantém compatibilidade com código existente
from logic_original import PedroBarrosFormatter, NutriPlanPedroBarros
