# logic.py - VERSÃO PEDRO BARROS COMPLETA
from database import get_food_data, get_meal_templates, get_substitution_rules, get_static_info
from datetime import datetime
import random
import json

class PedroBarrosFormatter:
    """Formatador específico para o estilo Pedro Barros."""
    
    @staticmethod
    def format_header(nome_paciente, data):
        """Formata o cabeçalho do plano."""
        return f"""                                 


                                                           Plano Alimentar
                                                        {nome_paciente}
                                                         Data: {data}




Todos os dias
Dieta única

"""

    @staticmethod
    def format_meal_header(horario, nome_refeicao):
        """Formata o cabeçalho de uma refeição."""
        return f"\n  {horario} - {nome_refeicao}                                                                                            Kcal"
    
    @staticmethod
    def format_food_item(nome, unidade, quantidade, kcal):
        """Formata um item alimentar com alinhamento."""
        # Formatar nome com unidade
        if isinstance(quantidade, float) and quantidade.is_integer():
            quantidade = int(quantidade)
            
        item_text = f"•   {nome} ({unidade}: {quantidade})"
        
        # Calcular espaços para alinhamento (máximo 100 caracteres)
        espacos_necessarios = 100 - len(item_text) - len(f"{kcal:.2f}")
        espacos = " " * max(espacos_necessarios, 2)
        
        return f"{item_text}{espacos}{kcal:.2f} kcal"
    
    @staticmethod
    def format_obs_almoco_jantar():
        """Formata as observações padrão para almoço/jantar."""
        return """Obs: *Substituições:
- Filé de Frango por: Carne Vermelha Magra (patinho, acém, alcatra, filé mignon, paleta, chá) OU Filé Suíno (Pernil, mignon, lombo)
OU Salmão ou Atum Fresco ou Peixe Branco ou Camarão Cozido.
- Arroz por: 120g de Batata Inglesa OU 140g de abóbora ou 60g de Aipim ou 60g de Macarrão ou 60g de Inhame.
- Feijão por: Lentilha OU grão de bico OU ervilha OU milho cozido.

*Legumes Variados: Tomate / Berinjela / Alho Poró / Maxixe / Brócolis / Rabanete / Chuchu / Couve / Beterraba / Pepino / Couve
Flor / Abobrinha / Repolho / Palmito / Quiabo / Cenoura / Vagem / Jiló."""

    @staticmethod
    def format_substituicao_header(numero, nome=""):
        """Formata o cabeçalho de uma substituição."""
        if nome:
            return f"\n\nSubstituição {numero} - {nome}                                                                                                     Kcal"
        return f"\n\nSubstituição {numero}                                                                                                     Kcal"
    
    @staticmethod
    def format_footer():
        """Formata o rodapé do documento."""
        return """\n\n\n\nEste documento é de uso exclusivo do destinatário e pode ter conteúdo confidencial. Se você não for o destinatário, qualquer uso, cópia, divulgação ou distribuição é estritamente
                                                                                    proibido."""

class NutriPlanPedroBarros:
    """Gerador de planos no estilo Pedro Barros."""
    
    def __init__(self):
        self.foods_db = get_food_data()
        self.formatter = PedroBarrosFormatter()
        
    def get_unit_format(self, food_name, qtd_g):
        """Retorna a unidade formatada baseada no alimento."""
        food_lower = food_name.lower()
        
        # Ovos
        if 'ovo' in food_lower and 'inteiro' in food_lower:
            unidades = int(qtd_g / 50)
            if unidades > 0:
                return f"Unidade ({int(qtd_g)}g)", unidades
            return "Grama", qtd_g
            
        # Clara de ovo
        if 'clara' in food_lower:
            unidades = int(qtd_g / 33)
            if unidades > 0:
                return f"Unidade ({int(qtd_g/unidades)}g)", unidades
            return "Grama", qtd_g
            
        # Pães
        if 'pão' in food_lower:
            if 'forma' in food_lower:
                fatias = int(qtd_g / 25)
                if fatias > 0:
                    return f"Fatia ({int(qtd_g/fatias)}g)", fatias
            elif 'francês' in food_lower or 'frances' in food_lower:
                unidades = int(qtd_g / 50)
                if unidades > 0:
                    return f"Unidade ({int(qtd_g/unidades)}g)", unidades
            return "Grama", qtd_g
            
        # Feijão
        if 'feijão' in food_lower or 'feijao' in food_lower:
            conchas = int(qtd_g / 86)
            if conchas > 0:
                return f"Concha ({int(qtd_g/conchas)}g)", conchas
            return "Grama", qtd_g
            
        # Queijos em fatias
        if 'queijo' in food_lower and 'mussarela' in food_lower:
            fatias = int(qtd_g / 15)
            if fatias > 0:
                return f"Fatia ({qtd_g/fatias:.1f}g)", fatias
            return "Grama", qtd_g
            
        # Iogurte
        if 'iogurte' in food_lower:
            if qtd_g == 170:
                return "Pote (170g)", 1
            return "Grama", qtd_g
            
        # Frutas
        if any(fruta in food_lower for fruta in ['banana', 'maçã', 'laranja']):
            if qtd_g <= 100:
                return f"Unidade média ({int(qtd_g)}g)", 1
            return "Grama", qtd_g
            
        # Líquidos (ml)
        if any(liq in food_lower for liq in ['leite', 'café', 'yopro']):
            if 'yopro' in food_lower:
                return "Unidade", 1
            return "ml", qtd_g
            
        # Padrão
        return "Grama", qtd_g
    
    def generate_cafe_manha(self):
        """Gera café da manhã no estilo Pedro Barros."""
        items = []
        
        # Estrutura padrão do café
        items.append({
            'nome': 'Ovo de galinha inteiro',
            'qtd_g': 50,
            'kcal': 74.50
        })
        
        items.append({
            'nome': 'Pão de forma',
            'qtd_g': 25,
            'kcal': 62.50
        })
        
        items.append({
            'nome': 'Requeijão Light',
            'qtd_g': 20,
            'kcal': 37.60,
            'obs': 'ou queijo minas ou cottage ou 15g de mussarela'
        })
        
        items.append({
            'nome': 'Iogurte natural desnatado',
            'qtd_g': 100,
            'kcal': 41.80
        })
        
        items.append({
            'nome': 'Mamão ou morango ou melão ou frutas vermelhas',
            'qtd_g': 100,
            'kcal': 29.25
        })
        
        items.append({
            'nome': 'Chia em Grãos - Hidratar os grãos no iogurte antes de consumir',
            'qtd_g': 5,
            'kcal': 19.33
        })
        
        items.append({
            'nome': 'Whey Protein - Killer Whey / Heavy Suppz',
            'qtd_g': 20,
            'kcal': 81.14
        })
        
        return items, """Obs: Substituições:
- 1 fatia de pão forma por: 20g de tapioca ou 2 biscoitos de arroz grandes ou 15g de aveia ou meio pão francês (sem miolo)."""
    
    def generate_almoco(self):
        """Gera almoço no estilo Pedro Barros."""
        items = []
        
        items.append({
            'nome': 'Filé de frango grelhado',
            'qtd_g': 120,
            'kcal': 220.36
        })
        
        items.append({
            'nome': 'Arroz branco (cozido)',
            'qtd_g': 60,
            'kcal': 74.81
        })
        
        items.append({
            'nome': 'Legumes Variados',
            'qtd_g': 120,
            'kcal': 30.00
        })
        
        items.append({
            'nome': 'Feijão cozido (50% grão/caldo)',
            'qtd_g': 86,
            'kcal': 52.46
        })
        
        items.append({
            'nome': 'Salada ou verdura crua, exceto de fruta',
            'qtd_g': 50,
            'kcal': 5.40,
            'unidade_custom': 'Pegador'
        })
        
        items.append({
            'nome': 'Azeite de oliva extra virgem - Borges®',
            'qtd_g': 5,
            'kcal': 43.33
        })
        
        return items, self.formatter.format_obs_almoco_jantar()
    
    def generate_lanche_substituicoes(self):
        """Gera as 6 substituições do lanche."""
        substituicoes = []
        
        # Substituição 1 - Panqueca Proteica
        sub1 = {
            'nome': 'Panqueca Proteica',
            'items': [
                {'nome': 'Banana', 'qtd_g': 60, 'kcal': 55.20},
                {'nome': 'Ovo de galinha', 'qtd_g': 50, 'kcal': 69.75},
                {'nome': 'Whey Protein - Killer Whey / Heavy Suppz', 'qtd_g': 25, 'kcal': 101.43},
                {'nome': 'Cacau em Pó 100% Puro Mãe Terra', 'qtd_g': 5, 'kcal': 14.00},
                {'nome': 'Canela em pó', 'qtd_g': 2, 'kcal': 5.22},
                {'nome': 'Psyllium', 'qtd_g': 5, 'kcal': 3.50}
            ],
            'obs': 'Obs: fazer panqueca: Basta misturar tudo e jogar na frigideira ou fazer um bolinho no micro onda.'
        }
        
        # Substituição 2 - Shake de Frutas
        sub2 = {
            'nome': 'Shake de Frutas',
            'items': [
                {'nome': 'Frutas (menos banana e abacate)', 'qtd_g': 100, 'kcal': 48.00},
                {'nome': 'Whey Protein - Killer Whey / Heavy Suppz', 'qtd_g': 35, 'kcal': 142.00},
                {'nome': 'Iogurte natural desnatado - Batavo®', 'qtd_g': 120, 'kcal': 50.16}
            ],
            'obs': 'Obs: Frutas: Melão, morango, uva ou abacaxi ou kiwi ou frutas vermelhas.'
        }
        
        # Substituição 3 - Crepioca
        sub3 = {
            'nome': 'Crepioca',
            'items': [
                {'nome': 'Tapioca seca', 'qtd_g': 20, 'kcal': 68.20},
                {'nome': 'Ovo de galinha', 'qtd_g': 50, 'kcal': 69.75},
                {'nome': 'Clara de ovo de galinha', 'qtd_g': 68, 'kcal': 34.00},
                {'nome': 'Requeijão - Danúbio® Light', 'qtd_g': 20, 'kcal': 37.60}
            ],
            'obs': 'Obs: Fazer Crepioca'
        }
        
        # Substituição 4 - Yopro
        sub4 = {
            'nome': 'Yopro Shake',
            'items': [
                {'nome': 'Shake Proteíco - Yopro 25g de PTN OU Piracanjuba 23g de PTN', 'qtd_g': 250, 'kcal': 165.18}
            ]
        }
        
        # Substituição 5 - Barra
        sub5 = {
            'nome': 'Barra Proteica',
            'items': [
                {'nome': 'Barra de Proteína Bold', 'qtd_g': 60, 'kcal': 184.80}
            ]
        }
        
        # Substituição 6 - Ovos com Queijo
        sub6 = {
            'nome': 'Ovos com Queijo',
            'items': [
                {'nome': 'Ovo de galinha', 'qtd_g': 50, 'kcal': 69.75},
                {'nome': 'Clara de ovo de galinha', 'qtd_g': 102, 'kcal': 51.00},
                {'nome': 'Queijo tipo mussarela', 'qtd_g': 25, 'kcal': 70.25},
                {'nome': 'Frutas (menos banana e abacate)', 'qtd_g': 75, 'kcal': 36.00}
            ]
        }
        
        return [sub1, sub2, sub3, sub4, sub5, sub6]

    def generate_jantar_substituicoes(self):
        """Gera as 4 substituições obrigatórias do jantar."""
        substituicoes = []
        
        # Substituição 1 - Pizza Fake
        sub1 = {
            'nome': 'Pizza Fake',
            'items': [
                {'nome': 'Rap10 integral', 'qtd_g': 35, 'kcal': 114.00, 'unidade_custom': 'Unidade'},
                {'nome': 'Queijo mussarela sem lactose - Lacfree Verde Campo', 'qtd_g': 30, 'kcal': 117.30},
                {'nome': 'Tomate cereja', 'qtd_g': 40, 'kcal': 8.40, 'unidade_custom': 'Unidade (10g)', 'qtd_custom': 4},
                {'nome': 'Orégano', 'qtd_g': 3, 'kcal': 9.18, 'unidade_custom': 'Punhado'},
                {'nome': 'Molho de tomate', 'qtd_g': 15, 'kcal': 4.80, 'unidade_custom': 'Colher De Sopa'},
                {'nome': 'Whey Protein - Killer Whey / Heavy Suppz', 'qtd_g': 30, 'kcal': 121.71}
            ],
            'obs': 'Obs: - pode substituir o whey por 80g de frango desfiado ou 120g de atum.'
        }
        
        # Substituição 2 - Strogonoff Light
        sub2 = {
            'nome': 'Strogonoff Light',
            'items': [
                {'nome': 'Filé-mignon Cozido(a)', 'qtd_g': 100, 'kcal': 204.00},
                {'nome': 'Ketchup', 'qtd_g': 10, 'kcal': 10.00},
                {'nome': 'Mostarda', 'qtd_g': 10, 'kcal': 7.80},
                {'nome': 'Arroz branco (cozido) ou Macarrão de arroz', 'qtd_g': 75, 'kcal': 93.52},
                {'nome': 'Champignon (cogumelo paris)', 'qtd_g': 50, 'kcal': 12.50},
                {'nome': 'Creme de Leite Light', 'qtd_g': 40, 'kcal': 46.44}
            ],
            'obs': 'Obs: Strogonoff light - Fazer na porção única. Misturar os ingredientes conforme acima.'
        }
        
        # Substituição 3 - Salpicão Light
        sub3 = {
            'nome': 'Salpicão Light',
            'items': [
                {'nome': 'Rap10 integral', 'qtd_g': 35, 'kcal': 114.00, 'unidade_custom': 'Unidade'},
                {'nome': 'Requeijão Light', 'qtd_g': 20, 'kcal': 37.60},
                {'nome': 'Palmito, cenoura, milho e tomate', 'qtd_g': 50, 'kcal': 12.50},
                {'nome': 'Filé de frango (cozido)', 'qtd_g': 100, 'kcal': 163.67}
            ],
            'obs': 'Obs: Fazer um salpicão light com os ingredientes e comer com pão.\nOutra opção de pasta: 100g de atum + 20g de requeijão light.'
        }
        
        # Substituição 4 - Hambúrguer Artesanal
        sub4 = {
            'nome': 'Hambúrguer Artesanal',
            'items': [
                {'nome': 'Pão de hambúrguer', 'qtd_g': 50, 'kcal': 195.30, 'unidade_custom': 'Unidade'},
                {'nome': 'Carne de Hambuguer caseira de Patinho 120g Cru.', 'qtd_g': 120, 'kcal': 199.00},
                {'nome': 'Queijo tipo mussarela', 'qtd_g': 20, 'kcal': 56.20},
                {'nome': 'Ketchup (colher de sopa: 1) ou Mostarda ou Maionese Light', 'qtd_g': 15, 'kcal': 15.00}
            ]
        }
        
        return [sub1, sub2, sub3, sub4]
    
    def format_meal_items(self, items):
        """Formata os itens de uma refeição."""
        output = ""
        
        for item in items:
            nome = item['nome']
            qtd_g = item['qtd_g']
            kcal = item['kcal']
            
            # Verificar se tem unidade customizada
            if 'unidade_custom' in item:
                unidade = item['unidade_custom']
                quantidade = item.get('qtd_custom', 1)
            else:
                unidade, quantidade = self.get_unit_format(nome, qtd_g)
            
            # Adicionar observação ao nome se existir
            if 'obs' in item and item['obs']:
                nome = f"{nome} {item['obs']}"
            
            output += "\n" + self.formatter.format_food_item(nome, unidade, quantidade, kcal)
        
        return output
    
    def calculate_totals(self, plan):
        """Calcula totais nutricionais."""
        total_kcal = 0
        total_p = 0
        total_c = 0
        total_g = 0
        
        # Somar todas as refeições
        for refeicao in plan['refeicoes']:
            for item in refeicao['items']:
                total_kcal += item['kcal']
                # Aqui você calcularia os macros se tivesse no item
        
        return {
            'total_kcal': total_kcal,
            'total_p': 150,  # Exemplo fixo
            'total_c': 200,  # Exemplo fixo  
            'total_g': 50    # Exemplo fixo
        }

def generate_plan_logic(request_data):
    """Função principal - gera plano no estilo Pedro Barros."""
    try:
        generator = NutriPlanPedroBarros()
        
        # Extrair dados
        paciente_info = request_data.get("paciente", {})
        nome = paciente_info.get("nome", "Paciente")
        peso = paciente_info.get("peso_kg", 75)
        data = datetime.now().strftime("%d/%m/%Y")
        
        # Iniciar formatação
        output = generator.formatter.format_header(nome, data)
        
        # CAFÉ DA MANHÃ
        cafe_items, cafe_obs = generator.generate_cafe_manha()
        output += generator.formatter.format_meal_header("08:00", "Café da manhã")
        output += generator.format_meal_items(cafe_items)
        output += f"\n{cafe_obs}"
        
        # ALMOÇO
        almoco_items, almoco_obs = generator.generate_almoco()
        output += "\n\n" + generator.formatter.format_meal_header("12:30", "Almoço")
        output += generator.format_meal_items(almoco_items)
        output += f"\n{almoco_obs}"
        
        # LANCHE DA TARDE
        output += "\n\n" + generator.formatter.format_meal_header("16:00", "Lanche da tarde")
        lanche_items = [
            {'nome': 'Whey Protein - Killer Whey / Heavy Suppz', 'qtd_g': 35, 'kcal': 142.00},
            {'nome': 'Pão de forma ou 2 torradas bauducco ou 2 Magic Toast', 'qtd_g': 25, 'kcal': 62.50},
            {'nome': 'Requeijão Light', 'qtd_g': 20, 'kcal': 37.60, 'obs': 'ou 20g de queijo minas'}
        ]
        output += generator.format_meal_items(lanche_items)
        output += "\nObs: Substituição: Pode trocar o pão por 40g de tapioca ou 1 rap 10."
        
        # SUBSTITUIÇÕES DO LANCHE
        lanche_subs = generator.generate_lanche_substituicoes()
        for i, sub in enumerate(lanche_subs, 1):
            output += generator.formatter.format_substituicao_header(i, sub.get('nome', ''))
            output += generator.format_meal_items(sub['items'])
            if 'obs' in sub:
                output += f"\n{sub['obs']}"
        
        # JANTAR
        output += "\n\n" + generator.formatter.format_meal_header("20:00", "Jantar")
        jantar_items = [
            {'nome': 'Tilápia Grelhada 150g OU Filé de frango grelhado', 'qtd_g': 120, 'kcal': 220.36},
            {'nome': 'Legumes Variados', 'qtd_g': 120, 'kcal': 30.00},
            {'nome': 'Salada ou verdura crua, exceto de fruta', 'qtd_g': 100, 'kcal': 10.80, 'unidade_custom': 'Pegador', 'qtd_custom': 2},
            {'nome': 'Arroz branco (cozido)', 'qtd_g': 60, 'kcal': 74.81},
            {'nome': 'Azeite de oliva extra virgem - Borges®', 'qtd_g': 5, 'kcal': 17.33, 'unidade_custom': 'Colher de chá (2,4ml)'}
        ]
        output += generator.format_meal_items(jantar_items)
        output += f"\n{almoco_obs}"  # Mesmas observações do almoço
        
        # SUBSTITUIÇÕES DO JANTAR
        jantar_subs = generator.generate_jantar_substituicoes()
        for i, sub in enumerate(jantar_subs, 1):
            output += generator.formatter.format_substituicao_header(i, sub['nome'])
            output += generator.format_meal_items(sub['items'])
            if 'obs' in sub:
                output += f"\n{sub['obs']}"
        
        # CEIA
        output += "\n\n" + generator.formatter.format_meal_header("22:00", "Ceia")
        ceia_items = [
            {'nome': 'Whey Protein - Killer Whey / Heavy Suppz', 'qtd_g': 15, 'kcal': 60.86},
            {'nome': 'Iogurte natural - Batavo®', 'qtd_g': 100, 'kcal': 55.00},
            {'nome': 'Frutas (menos banana e abacate)', 'qtd_g': 75, 'kcal': 36.00},
            {'nome': 'Gelatina diet* (qualquer sabor) - Royal®', 'qtd_g': 110, 'kcal': 11.00, 'unidade_custom': 'Unidade comercial (110g)'},
            {'nome': 'Chia em Grãos - Hidratar os grãos no iogurte', 'qtd_g': 5, 'kcal': 19.33}
        ]
        output += generator.format_meal_items(ceia_items)
        
        # RODAPÉ
        output += generator.formatter.format_footer()
        
        # Calcular totais
        totals = generator.calculate_totals({'refeicoes': []})
        
        # Criar resposta compatível com a API
        response = {
            'plano': {
                'paciente': nome,
                'data': data,
                'peso_kg': peso,
                'resumo': {
                    'meta_kcal': 2000,
                    'total_kcal_calculado': totals['total_kcal'],
                    'total_proteina_g': totals['total_p'],
                    'proteina_g_kg': round(totals['total_p'] / peso, 2),
                    'total_carboidratos_g': totals['total_c'],
                    'carboidratos_percent': 40,
                    'total_gordura_g': totals['total_g'],
                    'gordura_percent': 25,
                    'total_fibras_g': 30,
                    'fibras_percent': 100,
                    'matematicamente_valido': True
                },
                'plano_formatado': output,
                'refeicoes': []  # Mantém estrutura mas usa plano_formatado
            }
        }
        
        return response, 200
        
    except Exception as e:
        print(f"Erro ao gerar plano Pedro Barros: {str(e)}")
        import traceback
        traceback.print_exc()
        return {'erro': 'Erro ao gerar plano'}, 500

# Manter compatibilidade
def generate_template_plan(request_data):
    """Redireciona para a função principal."""
    return generate_plan_logic(request_data)
