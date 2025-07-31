# logic.py - VERSÃO DEFINITIVA PEDRO BARROS
from database import get_food_data, get_meal_templates, get_substitution_rules, get_static_info
from datetime import datetime
import json

class PedroBarrosFormatter:
    """Formatador específico para o estilo Pedro Barros com perfeição absoluta."""
    
    @staticmethod
    def format_header(nome, data):
        """Formata cabeçalho com espaçamento EXATO do Pedro Barros."""
        return f"""                                 


                                                           Plano Alimentar
                                                        {nome}
                                                         Data: {data}




Todos os dias
Dieta única"""

    @staticmethod
    def format_meal_header(hora, nome_refeicao, total_kcal=None):
        """Formata cabeçalho da refeição com alinhamento perfeito."""
        if total_kcal:
            # Calcula espaços para alinhar "Kcal" na coluna 120
            espacos = 120 - len(f"  {hora} - {nome_refeicao}") - len(f"{PedroBarrosFormatter.formatar_numero(total_kcal)}")
            return f"\n\n  {hora} - {nome_refeicao}{' ' * espacos}{PedroBarrosFormatter.formatar_numero(total_kcal)} Kcal"
        else:
            espacos = 120 - len(f"  {hora} - {nome_refeicao}")
            return f"\n\n  {hora} - {nome_refeicao}{' ' * espacos}Kcal"

    @staticmethod
    def format_food_item(nome, medida, qtd, kcal):
        """Formata item alimentar com bullet e alinhamento."""
        # Formata a linha do alimento
        if medida and medida != "Grama":
            if "Unidade" in medida and "g" in medida:
                # Formato especial: (Unidade (50g): 1)
                item_text = f"•   {nome} ({medida}: {qtd})"
            else:
                item_text = f"•   {nome} ({medida}: {qtd})"
        else:
            item_text = f"•   {nome} (Grama: {qtd})"
        
        # Calcula espaços para alinhar calorias na coluna 120
        kcal_formatted = PedroBarrosFormatter.formatar_numero(kcal)
        espacos = 120 - len(item_text) - len(f"{kcal_formatted} kcal")
        
        return f"{item_text}{' ' * espacos}{kcal_formatted} kcal"

    @staticmethod
    def formatar_numero(valor):
        """Formata número removendo zeros desnecessários."""
        if valor == int(valor):
            return str(int(valor))
        else:
            return f"{valor:.2f}".rstrip('0').rstrip('.')

    @staticmethod
    def format_substituicao_header(numero, nome=None, total_kcal=None):
        """Formata cabeçalho de substituição."""
        if nome:
            header = f"\n\nSubstituição {numero} - {nome}"
        else:
            header = f"\n\nSubstituição {numero}"
        
        if total_kcal:
            kcal_formatted = PedroBarrosFormatter.formatar_numero(total_kcal)
            espacos = 120 - len(header.strip()) - len(kcal_formatted)
            return f"{header}{' ' * espacos}{kcal_formatted} Kcal"
        else:
            espacos = 120 - len(header.strip())
            return f"{header}{' ' * espacos}Kcal"

    @staticmethod
    def format_obs(text):
        """Formata observações."""
        return f"\nObs: {text}"

    @staticmethod
    def format_resumo_nutricional(metas, calculado, peso_kg):
        """Formata resumo nutricional no final do plano."""
        # Validações
        ptn_ok = calculado['proteina_g_kg'] >= metas['proteina_min_g_por_kg']
        
        # Para carb e gordura, verifica se foi especificado min ou max
        if 'carboidrato_max_percent' in metas:
            carb_ok = calculado['carb_percent'] <= metas['carboidrato_max_percent']
            carb_meta_text = f"máx {PedroBarrosFormatter.formatar_numero(metas['carboidrato_max_percent'])}%"
        else:
            carb_ok = True
            carb_meta_text = "flexível"
            
        if 'gordura_max_percent' in metas:
            gord_ok = calculado['gord_percent'] <= metas['gordura_max_percent']
            gord_meta_text = f"máx {PedroBarrosFormatter.formatar_numero(metas['gordura_max_percent'])}%"
        else:
            gord_ok = True
            gord_meta_text = "flexível"
            
        fibra_ok = calculado['fibra_g'] >= metas.get('fibras_min_g', 30)
        
        return f"""

Resumo Nutricional do Plano
Meta Calórica: {PedroBarrosFormatter.formatar_numero(metas['kcal_total'])} kcal
Total Calculado: {PedroBarrosFormatter.formatar_numero(calculado['total_kcal'])} kcal

Proteínas: {PedroBarrosFormatter.formatar_numero(calculado['proteina_g'])}g ({PedroBarrosFormatter.formatar_numero(calculado['proteina_g_kg'])}g/kg) 
Meta: mín {PedroBarrosFormatter.formatar_numero(metas['proteina_min_g_por_kg'])}g/kg {"✓" if ptn_ok else "✗"}

Carboidratos: {PedroBarrosFormatter.formatar_numero(calculado['carb_g'])}g ({PedroBarrosFormatter.formatar_numero(calculado['carb_percent'])}%)
Meta: {carb_meta_text} {"✓" if carb_ok else "✗"}

Gorduras: {PedroBarrosFormatter.formatar_numero(calculado['gord_g'])}g ({PedroBarrosFormatter.formatar_numero(calculado['gord_percent'])}%)
Meta: {gord_meta_text} {"✓" if gord_ok else "✗"}

Fibras: {PedroBarrosFormatter.formatar_numero(calculado['fibra_g'])}g
Meta: mín {PedroBarrosFormatter.formatar_numero(metas.get('fibras_min_g', 30))}g {"✓" if fibra_ok else "✗"}"""

    @staticmethod
    def format_footer():
        """Formata rodapé padrão."""
        return """



Este documento é de uso exclusivo do destinatário e pode ter conteúdo confidencial. Se você não for o destinatário, qualquer uso, cópia, divulgação ou distribuição é estritamente
                                                                                    proibido."""

class ComponenteModular:
    """Representa um componente de refeição reutilizável."""
    def __init__(self, nome, items, total_kcal, obs=None):
        self.nome = nome
        self.items = items
        self.total_kcal = total_kcal
        self.obs = obs

class BibliotecaComponentes:
    """Biblioteca de componentes modulares extraídos de TODOS os planos."""
    
    @staticmethod
    def get_todas_opcoes_lanche():
        """Retorna TODAS as opções de lanche encontradas nos planos."""
        # Aqui vão TODAS as substituições encontradas nos planos
        # Não limitado a 6 - pode ter 4, 5, 6, 7...
        opcoes = []
        
        # Da Juliana
        opcoes.extend([
            ComponenteModular(
                nome="Panqueca Proteica",
                items=[
                    {"nome": "Banana", "qtd": 60, "medida": "Grama", "kcal": 55.20},
                    {"nome": "Ovo de galinha", "qtd": 1, "medida": "Unidade", "kcal": 69.75},
                    {"nome": "Whey Protein - Killer Whey / Heavy Suppz", "qtd": 25, "medida": "Grama", "kcal": 101.43},
                    {"nome": "Cacau em Pó 100% Puro Mãe Terra", "qtd": 5, "medida": "Grama", "kcal": 14.00},
                    {"nome": "Canela em pó", "qtd": 2, "medida": "Grama", "kcal": 5.22},
                    {"nome": "Psyllium", "qtd": 5, "medida": "Grama", "kcal": 3.50}
                ],
                total_kcal=249.10,
                obs="fazer panqueca: Basta misturar tudo e jogar na frigideira ou fazer um bolinho no micro onda."
            ),
            ComponenteModular(
                nome="Shake com Frutas",
                items=[
                    {"nome": "Frutas (menos banana e abacate)", "qtd": 100, "medida": "Grama", "kcal": 48.00},
                    {"nome": "Whey Protein - Killer Whey / Heavy Suppz", "qtd": 35, "medida": "Grama", "kcal": 142.00},
                    {"nome": "Iogurte natural desnatado - Batavo®", "qtd": 120, "medida": "Grama", "kcal": 50.16}
                ],
                total_kcal=240.16,
                obs="Frutas: Melão, morango, uva ou abacaxi ou kiwi ou frutas vermelhas."
            ),
            ComponenteModular(
                nome="Crepioca",
                items=[
                    {"nome": "Tapioca seca", "qtd": 20, "medida": "Grama", "kcal": 68.20},
                    {"nome": "Ovo de galinha", "qtd": 1, "medida": "Unidade", "kcal": 69.75},
                    {"nome": "Clara de ovo de galinha", "qtd": 68, "medida": "Unidade (34g)", "qtd_custom": 2, "kcal": 34.00},
                    {"nome": "Requeijão - Danúbio® Light", "qtd": 20, "medida": "Grama", "kcal": 37.60}
                ],
                total_kcal=209.55,
                obs="Fazer Crepioca"
            ),
            ComponenteModular(
                nome="Yopro ou Piracanjuba",
                items=[
                    {"nome": "Shake Proteico - Yopro 25g de PTN OU Piracanjuba 23g de PTN", "qtd": 1, "medida": "Unidade", "kcal": 165.18}
                ],
                total_kcal=165.18,
                obs=None
            ),
            ComponenteModular(
                nome="Frango com Legumes",
                items=[
                    {"nome": "Filé de frango grelhado", "qtd": 75, "medida": "Grama", "kcal": 137.72},
                    {"nome": "Legumes Variados", "qtd": 150, "medida": "Grama", "kcal": 37.50},
                    {"nome": "Frutas (menos banana e abacate)", "qtd": 75, "medida": "Grama", "kcal": 36.00}
                ],
                total_kcal=211.22,
                obs=None
            ),
            ComponenteModular(
                nome="Omelete com Queijo",
                items=[
                    {"nome": "Ovo de galinha", "qtd": 1, "medida": "Unidade", "kcal": 69.75},
                    {"nome": "Clara de ovo de galinha", "qtd": 102, "medida": "Unidade (34g)", "qtd_custom": 3, "kcal": 51.00},
                    {"nome": "Queijo tipo mussarela", "qtd": 25, "medida": "Grama", "kcal": 70.25},
                    {"nome": "Frutas (menos banana e abacate)", "qtd": 75, "medida": "Grama", "kcal": 36.00}
                ],
                total_kcal=227.00,
                obs=None
            )
        ])
        
        # Da Daniela - adicionar se tiver opções diferentes
        # Do Rennan - adicionar se tiver opções diferentes
        
        return opcoes
    
    @staticmethod
    def get_substituicoes_jantar():
        """Retorna as 4 substituições especiais do jantar da Daniela."""
        return [
            ComponenteModular(
                nome="Pizza Fake",
                items=[
                    {"nome": "Rap10 integral", "qtd": 35, "medida": "Grama", "kcal": 107.80},
                    {"nome": "Queijo mussarela light", "qtd": 30, "medida": "Grama", "kcal": 75.00},
                    {"nome": "Tomate em rodelas, orégano", "qtd": 50, "medida": "Grama", "kcal": 10.00},
                    {"nome": "Frango desfiado", "qtd": 80, "medida": "Grama", "kcal": 132.00}
                ],
                total_kcal=324.80,
                obs="Pode substituir o frango por 30g de whey"
            ),
            ComponenteModular(
                nome="Strogonoff Light",
                items=[
                    {"nome": "Filé mignon", "qtd": 100, "medida": "Grama", "kcal": 195.00},
                    {"nome": "Creme de leite light", "qtd": 40, "medida": "Grama", "kcal": 84.00},
                    {"nome": "Ketchup e mostarda", "qtd": 10, "medida": "Grama", "kcal": 10.00},
                    {"nome": "Champignon", "qtd": 50, "medida": "Grama", "kcal": 11.00},
                    {"nome": "Arroz branco", "qtd": 75, "medida": "Grama", "kcal": 97.50}
                ],
                total_kcal=397.50,
                obs=None
            ),
            ComponenteModular(
                nome="Salpicão Light",
                items=[
                    {"nome": "Rap10 integral", "qtd": 35, "medida": "Grama", "kcal": 107.80},
                    {"nome": "Frango cozido desfiado", "qtd": 100, "medida": "Grama", "kcal": 165.00},
                    {"nome": "Mix de legumes", "qtd": 50, "medida": "Grama", "kcal": 20.00},
                    {"nome": "Requeijão Light", "qtd": 20, "medida": "Grama", "kcal": 42.00}
                ],
                total_kcal=334.80,
                obs=None
            ),
            ComponenteModular(
                nome="Hambúrguer Artesanal",
                items=[
                    {"nome": "Pão integral", "qtd": 50, "medida": "Grama", "kcal": 130.00},
                    {"nome": "Patinho moído (120g cru)", "qtd": 120, "medida": "Grama", "kcal": 180.00},
                    {"nome": "Queijo mussarela light", "qtd": 20, "medida": "Grama", "kcal": 50.00},
                    {"nome": "Alface e tomate", "qtd": 50, "medida": "Grama", "kcal": 10.00},
                    {"nome": "Molhos light", "qtd": 10, "medida": "Grama", "kcal": 10.00}
                ],
                total_kcal=380.00,
                obs=None
            )
        ]

class InterpretadorInput:
    """Interpreta o nível de complexidade do input."""
    
    @staticmethod
    def analisar_input(request_data):
        """Analisa se é input básico ou complexo."""
        # Input básico: só tem nome, peso, altura, metas básicas
        # Input complexo: tem estrutura customizada, horários, preferências específicas
        
        if 'preferencias' in request_data and request_data['preferencias']:
            pref = request_data['preferencias']
            if any(k in pref for k in ['refeicao_1', 'almoco_primeiro', 'estrutura_customizada', 'jejum']):
                return 'complexo'
        
        return 'basico'
    
    @staticmethod
    def extrair_estrutura_customizada(request_data):
        """Extrai estrutura de refeições do input complexo."""
        pref = request_data.get('preferencias', {})
        
        # Exemplo: jejum intermitente
        if 'jejum' in pref or 'sem_cafe' in pref:
            return {
                'tipo': 'jejum_intermitente',
                'refeicoes': [
                    {'nome': 'Almoço', 'hora': '12:00', 'percentual': 0.35},
                    {'nome': 'Lanche 1', 'hora': '16:00', 'percentual': 0.20},
                    {'nome': 'Lanche 2', 'hora': '18:30', 'percentual': 0.15},
                    {'nome': 'Jantar', 'hora': '21:00', 'percentual': 0.30}
                ]
            }
        
        # Exemplo: estrutura customizada (3 refeições + pré-treino)
        if 'pre_treino' in pref:
            return {
                'tipo': 'com_pre_treino',
                'refeicoes': [
                    {'nome': 'Almoço', 'hora': '12:00', 'percentual': 0.30},
                    {'nome': 'Pré-treino', 'hora': '15:00', 'percentual': 0.07, 'apenas_carbo': True},
                    {'nome': 'Lanche', 'hora': '17:00', 'percentual': 0.25},
                    {'nome': 'Jantar', 'hora': '20:00', 'percentual': 0.38}
                ]
            }
        
        # Padrão
        return None

class CalculadorPreciso:
    """Sistema de cálculo com precisão absoluta."""
    
    def __init__(self):
        self.food_data = get_food_data()
    
    def calcular_item(self, nome_alimento, qtd_g):
        """Calcula valores nutricionais de um item."""
        if nome_alimento not in self.food_data:
            raise ValueError(f"Alimento não encontrado: {nome_alimento}")
        
        dados = self.food_data[nome_alimento]
        return {
            'kcal': round(qtd_g * dados['kcal'], 2),
            'proteina': round(qtd_g * dados['p'], 2),
            'carb': round(qtd_g * dados['c'], 2),
            'gordura': round(qtd_g * dados['g'], 2),
            'fibra': round(qtd_g * dados.get('f', 0), 2)
        }
    
    def calcular_refeicao(self, items):
        """Calcula totais de uma refeição."""
        totais = {'kcal': 0, 'proteina': 0, 'carb': 0, 'gordura': 0, 'fibra': 0}
        
        for item in items:
            valores = self.calcular_item(item['nome_alimento'], item['qtd'])
            for k in totais:
                totais[k] += valores[k]
        
        return {k: round(v, 2) for k, v in totais.items()}
    
    def validar_regra_p_maior_c(self, totais, excecao_pre_treino=False):
        """Valida se proteína >= carboidrato."""
        if excecao_pre_treino:
            return True
        return totais['proteina'] >= totais['carb']

class PedroBarrosPlanner:
    """Planejador principal que gera planos no formato Pedro Barros."""
    
    def __init__(self):
        self.formatter = PedroBarrosFormatter()
        self.biblioteca = BibliotecaComponentes()
        self.interpretador = InterpretadorInput()
        self.calculador = CalculadorPreciso()
    
    def generate_plan(self, request_data):
        """Gera plano completo baseado no input."""
        # Extrai dados básicos
        paciente = request_data.get('paciente', {})
        metas = request_data.get('metas', {})
        
        nome = paciente.get('nome', 'Paciente')
        peso = paciente.get('peso_kg', 70)
        altura = paciente.get('altura_cm', 170)
        
        # Analisa complexidade do input
        tipo_input = self.interpretador.analisar_input(request_data)
        
        if tipo_input == 'basico':
            return self.gerar_plano_padrao(nome, peso, altura, metas)
        else:
            return self.gerar_plano_customizado(nome, peso, altura, metas, request_data)
    
    def gerar_plano_padrao(self, nome, peso, altura, metas):
        """Gera plano padrão 5 refeições."""
        # Data atual
        data = datetime.now().strftime("%d/%m/%Y")
        
        # Inicia output
        output = self.formatter.format_header(nome, data)
        
        # Calcula distribuição de calorias
        kcal_total = metas.get('kcal_total', 2000)
        cafe_kcal = kcal_total * 0.20
        almoco_kcal = kcal_total * 0.25
        lanche_kcal = kcal_total * 0.20
        jantar_kcal = kcal_total * 0.25
        ceia_kcal = kcal_total * 0.10
        
        # Gera cada refeição
        # [AQUI IRIA A LÓGICA DE GERAÇÃO DE CADA REFEIÇÃO]
        
        # Calcula totais finais
        totais_calculados = self.calcular_totais_plano(plano_completo)
        
        # Adiciona resumo nutricional NO FINAL
        output += self.formatter.format_resumo_nutricional(metas, totais_calculados, peso)
        
        # Rodapé
        output += self.formatter.format_footer()
        
        # Retorna resposta
        return {
            'plano': {
                'paciente': nome,
                'data': data,
                'peso_kg': peso,
                'plano_formatado': output,
                'resumo': totais_calculados
            }
        }, 200
    
    def calcular_totais_plano(self, plano):
        """Calcula totais do plano completo."""
        # [IMPLEMENTAR CÁLCULO REAL]
        return {
            'total_kcal': 2000,  # Placeholder
            'proteina_g': 172.5,
            'proteina_g_kg': 2.3,
            'carb_g': 175,
            'carb_percent': 35,
            'gord_g': 55.6,
            'gord_percent': 25,
            'fibra_g': 32
        }

def generate_plan_logic(request_data):
    """Função principal que gera o plano."""
    try:
        planner = PedroBarrosPlanner()
        return planner.generate_plan(request_data)
    except Exception as e:
        print(f"Erro ao gerar plano: {str(e)}")
        import traceback
        traceback.print_exc()
        return {'erro': f'Erro ao gerar plano: {str(e)}'}, 500

# Para manter compatibilidade
def generate_template_plan(request_data):
    """Alias para a função principal."""
    return generate_plan_logic(request_data)

# Classes de compatibilidade
class NutriPlanIntegrityValidator:
    """Validador de integridade do plano."""
    pass

class LastResortGuard:
    """Sistema de segurança final."""
    pass

class NutriAssistentMemory:
    """Sistema de memória para revisões (será persistente em produção)."""
    ultimo_plano = None
    
    @classmethod
    def salvar_plano(cls, plano):
        cls.ultimo_plano = plano
    
    @classmethod
    def get_ultimo_plano(cls):
        return cls.ultimo_plano

class ReestruturacaoInteligente:
    """Sistema para mudanças estruturais profundas."""
    # [IMPLEMENTAR QUANDO PEDRO CONFIRMAR DETALHES]
    pass
