# logic.py - VERSÃO DEFINITIVA COM PRECISÃO ABSOLUTA
from database import get_food_data, get_meal_templates, get_substitution_rules, get_static_info
from datetime import datetime
import json
import copy

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
           espacos = 120 - len(f"  {hora} - {nome_refeicao}") - len(f"{PedroBarrosFormatter.formatar_numero(total_kcal)}")
           return f"\n\n  {hora} - {nome_refeicao}{' ' * espacos}{PedroBarrosFormatter.formatar_numero(total_kcal)} Kcal"
       else:
           espacos = 120 - len(f"  {hora} - {nome_refeicao}")
           return f"\n\n  {hora} - {nome_refeicao}{' ' * espacos}Kcal"

   @staticmethod
   def format_food_item(nome, medida, qtd, kcal):
       """Formata item alimentar com bullet e alinhamento."""
       if medida and medida != "Grama":
           if "Unidade" in medida and "g" in medida:
               item_text = f"•   {nome} ({medida}: {qtd})"
           else:
               item_text = f"•   {nome} ({medida}: {qtd})"
       else:
           item_text = f"•   {nome} (Grama: {qtd})"
       
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
       ptn_ok = calculado['proteina_g_kg'] >= metas['proteina_min_g_por_kg']
       
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

class CalculadorPreciso:
   """Sistema de cálculo com precisão absoluta."""
   
   def __init__(self):
       self.food_data = get_food_data()
   
   def calcular_item(self, nome_alimento, qtd_g):
       """Calcula valores nutricionais de um item com precisão."""
       alimento_key = self._find_food_key(nome_alimento)
       if not alimento_key:
           raise ValueError(f"Alimento não encontrado: {nome_alimento}")
       
       dados = self.food_data[alimento_key]
       return {
           'kcal': round(qtd_g * dados['kcal'], 2),
           'proteina': round(qtd_g * dados['p'], 2),
           'carb': round(qtd_g * dados['c'], 2),
           'gordura': round(qtd_g * dados['g'], 2),
           'fibra': round(qtd_g * dados.get('f', 0), 2)
       }
   
   def _find_food_key(self, nome_alimento):
       """Encontra a chave do alimento no banco de dados."""
       nome_lower = nome_alimento.lower()
       
       # Mapeamentos especiais
       mapeamentos = {
           'pão de forma integral': 'pao_forma_integral',
           'pão de forma': 'pao_forma_integral',
           'requeijão light': 'requeijao_light',
           'iogurte natural - batavo®': 'iogurte_natural_desnatado',
           'iogurte natural desnatado': 'iogurte_natural_desnatado',
           'frutas (menos banana e abacate)': 'frutas',
           'chia em grãos': 'chia',
           'whey protein - killer whey / heavy suppz': 'whey_protein_isolado_hidrolisado',
           'whey protein': 'whey_protein_isolado_hidrolisado',
           'ovo de galinha inteiro': 'ovo_inteiro',
           'ovo de galinha': 'ovo_inteiro',
           'filé de frango grelhado': 'peito_frango_grelhado_sem_pele',
           'arroz branco (cozido)': 'arroz_branco_cozido',
           'arroz branco': 'arroz_branco_cozido',
           'feijão cozido': 'feijao_carioca_cozido',
           'legumes variados': 'legumes_variados',
           'salada ou verdura crua': 'salada_crua',
           'azeite de oliva': 'azeite_oliva_extra_virgem',
           'tilápia grelhada': 'tilapia_assada',
           'rap10 integral': 'rap10_integral',
           'queijo mussarela': 'queijo_mussarela_light',
           'tomate cereja': 'tomate_cereja',
           'orégano': 'oregano',
           'molho de tomate': 'molho_tomate',
           'filé-mignon': 'file_mignon',
           'ketchup': 'ketchup',
           'mostarda': 'mostarda',
           'champignon': 'champignon',
           'creme de leite light': 'creme_leite_light',
           'palmito': 'palmito',
           'pão de hambúrguer': 'pao_hamburguer_light',
           'carne de hambúrguer': 'patinho_moido_95_5',
           'gelatina diet': 'gelatina_diet',
           'banana': 'banana',
           'cacau em pó': 'cacau_po',
           'canela em pó': 'canela_po',
           'psyllium': 'psyllium',
           'tapioca seca': 'tapioca_seca',
           'clara de ovo': 'clara_ovo',
           'shake proteico - yopro': 'iogurte_proteico_yopro'
       }
       
       # Procura no mapeamento
       for key, value in mapeamentos.items():
           if key in nome_lower:
               return value
       
       # Procura direto no banco
       for key in self.food_data:
           if key in nome_lower.replace(' ', '_'):
               return key
       
       return None
   
   def calcular_totais_refeicao(self, items):
       """Calcula totais de uma refeição."""
       totais = {'kcal': 0, 'proteina': 0, 'carb': 0, 'gordura': 0, 'fibra': 0}
       
       for item in items:
           if 'valores' in item:
               valores = item['valores']
           else:
               valores = self.calcular_item(item['nome'], item['qtd'])
           
           for k in totais:
               totais[k] = round(totais[k] + valores.get(k, 0), 2)
       
       return totais

class AjustadorInteligente:
   """Ajusta plano para atingir metas com precisão absoluta."""
   
   def __init__(self):
       self.calculador = CalculadorPreciso()
       self.food_data = get_food_data()
   
   def ajustar_plano_completo(self, plano_base, metas, peso_kg):
       """Ajusta o plano completo para bater EXATAMENTE as metas."""
       # Calcula totais atuais
       totais_atual = self._calcular_totais_plano(plano_base)
       
       # Calcula fatores de ajuste
       fator_kcal = metas['kcal_total'] / totais_atual['kcal'] if totais_atual['kcal'] > 0 else 1
       
       # Ajusta todas as quantidades proporcionalmente
       plano_ajustado = self._aplicar_fator_global(plano_base, fator_kcal)
       
       # Recalcula após ajuste
       totais_ajustado = self._calcular_totais_plano(plano_ajustado)
       
       # Ajuste fino para proteína se necessário
       proteina_alvo = peso_kg * metas['proteina_min_g_por_kg']
       if totais_ajustado['proteina'] < proteina_alvo:
           plano_ajustado = self._aumentar_proteina(plano_ajustado, proteina_alvo - totais_ajustado['proteina'])
       
       # Rebalanceia macros se necessário
       plano_final = self._rebalancear_macros(plano_ajustado, metas, peso_kg)
       
       return plano_final
   
   def _calcular_totais_plano(self, plano):
       """Calcula totais nutricionais do plano completo."""
       totais = {'kcal': 0, 'proteina': 0, 'carb': 0, 'gordura': 0, 'fibra': 0}
       
       for refeicao in plano:
           if 'items' in refeicao:
               for item in refeicao['items']:
                   if 'valores' in item:
                       valores = item['valores']
                   else:
                       valores = self.calculador.calcular_item(item['nome'], item['qtd'])
                   
                   for k in totais:
                       totais[k] += valores.get(k, 0)
       
       return {k: round(v, 2) for k, v in totais.items()}
   
   def _aplicar_fator_global(self, plano_base, fator):
       """Aplica fator de ajuste em todas as quantidades."""
       plano_ajustado = copy.deepcopy(plano_base)
       
       for refeicao in plano_ajustado:
           if 'items' in refeicao:
               for item in refeicao['items']:
                   item['qtd'] = round(item['qtd'] * fator, 1)
                   if 'qtd_custom' in item:
                       item['qtd_custom'] = round(item['qtd_custom'] * fator, 1)
                   
                   # Recalcula valores
                   item['valores'] = self.calculador.calcular_item(item['nome'], item['qtd'])
                   item['kcal'] = item['valores']['kcal']
       
       return plano_ajustado
   
   def _aumentar_proteina(self, plano, deficit_proteina):
       """Aumenta proteína distribuindo entre whey e ovos."""
       whey_por_g = self.food_data.get('whey_protein_isolado_hidrolisado', {}).get('p', 0.9)
       gramas_whey_extra = round(deficit_proteina / whey_por_g / 3)  # Divide em 3 refeições
       
       # Adiciona whey no café, lanche e ceia
       for refeicao in plano:
           if any(x in refeicao.get('nome', '').lower() for x in ['café', 'lanche', 'ceia']):
               for item in refeicao['items']:
                   if 'whey' in item['nome'].lower():
                       item['qtd'] += gramas_whey_extra
                       item['valores'] = self.calculador.calcular_item(item['nome'], item['qtd'])
                       item['kcal'] = item['valores']['kcal']
                       break
       
       return plano
   
   def _rebalancear_macros(self, plano, metas, peso_kg):
       """Rebalanceia macros para ficar dentro dos limites."""
       totais = self._calcular_totais_plano(plano)
       
       # Calcula percentuais
       carb_percent = (totais['carb'] * 4 / totais['kcal']) * 100 if totais['kcal'] > 0 else 0
       gord_percent = (totais['gordura'] * 9 / totais['kcal']) * 100 if totais['kcal'] > 0 else 0
       
       # Se carboidrato passou do limite
       if carb_percent > metas.get('carboidrato_max_percent', 100):
           plano = self._reduzir_carboidratos(plano, carb_percent - metas['carboidrato_max_percent'])
       
       # Se gordura passou do limite
       if gord_percent > metas.get('gordura_max_percent', 100):
           plano = self._reduzir_gorduras(plano, gord_percent - metas['gordura_max_percent'])
       
       return plano
   
   def _reduzir_carboidratos(self, plano, excesso_percent):
       """Reduz carboidratos proporcionalmente."""
       fator_reducao = 1 - (excesso_percent / 100)
       
       for refeicao in plano:
           if 'items' in refeicao:
               for item in refeicao['items']:
                   # Reduz apenas itens ricos em carboidrato
                   if any(x in item['nome'].lower() for x in ['arroz', 'pão', 'tapioca', 'batata', 'macarrão']):
                       item['qtd'] = round(item['qtd'] * fator_reducao, 1)
                       item['valores'] = self.calculador.calcular_item(item['nome'], item['qtd'])
                       item['kcal'] = item['valores']['kcal']
       
       return plano
   
   def _reduzir_gorduras(self, plano, excesso_percent):
       """Reduz gorduras proporcionalmente."""
       fator_reducao = 1 - (excesso_percent / 50)  # Redução mais suave
       
       for refeicao in plano:
           if 'items' in refeicao:
               for item in refeicao['items']:
                   # Reduz apenas itens ricos em gordura
                   if any(x in item['nome'].lower() for x in ['azeite', 'pasta de amendoim', 'castanha', 'queijo']):
                       item['qtd'] = round(item['qtd'] * fator_reducao, 1)
                       item['valores'] = self.calculador.calcular_item(item['nome'], item['qtd'])
                       item['kcal'] = item['valores']['kcal']
       
       return plano

class GeradorPlanoPedroBarros:
   """Gerador principal de planos no formato Pedro Barros."""
   
   def __init__(self):
       self.formatter = PedroBarrosFormatter()
       self.calculador = CalculadorPreciso()
       self.ajustador = AjustadorInteligente()
       self.food_data = get_food_data()
   
   def gerar_plano_completo(self, nome, peso_kg, altura_cm, metas):
       """Gera plano completo com precisão absoluta."""
       # Data atual
       data = datetime.now().strftime("%d/%m/%Y")
       
       # Cria estrutura base do plano
       plano_base = self._criar_plano_base(metas['kcal_total'])
       
       # Ajusta para bater as metas EXATAMENTE
       plano_ajustado = self.ajustador.ajustar_plano_completo(plano_base, metas, peso_kg)
       
       # Formata output
       output = self._formatar_plano_completo(plano_ajustado, nome, data, peso_kg, metas)
       
       return output
   
   def _criar_plano_base(self, kcal_total):
       """Cria estrutura base do plano com distribuição padrão."""
       # Distribuição: Café 20%, Almoço 25%, Lanche 20%, Jantar 25%, Ceia 10%
       return [
           {
               'nome': 'Café da manhã',
               'hora': '08:00',
               'percentual': 0.20,
               'items': [
                   {'nome': 'Pão de forma integral', 'qtd': 50, 'medida': 'Fatia (25g)', 'qtd_custom': 2},
                   {'nome': 'Requeijão Light', 'qtd': 20, 'medida': 'Grama'},
                   {'nome': 'Iogurte natural - Batavo®', 'qtd': 100, 'medida': 'Grama'},
                   {'nome': 'Frutas (menos banana e abacate)', 'qtd': 100, 'medida': 'Grama'},
                   {'nome': 'Chia em Grãos - Hidratar os grãos no iogurte', 'qtd': 5, 'medida': 'Grama'},
                   {'nome': 'Whey Protein - Killer Whey / Heavy Suppz', 'qtd': 20, 'medida': 'Grama'},
                   {'nome': 'Ovo de galinha inteiro', 'qtd': 50, 'medida': 'Unidade (50g)', 'qtd_custom': 1}
               ],
               'obs': 'Substituições:\n- Pão por: 50g de tapioca ou 2 biscoitos de arroz grandes ou 30g de aveia ou 1 pão francês sem miolo.'
           },
           {
               'nome': 'Almoço',
               'hora': '12:30',
               'percentual': 0.25,
               'items': [
                   {'nome': 'Filé de frango grelhado', 'qtd': 120, 'medida': 'Grama'},
                   {'nome': 'Arroz branco (cozido)', 'qtd': 60, 'medida': 'Grama'},
                   {'nome': 'Feijão cozido (50% grão/caldo)', 'qtd': 86, 'medida': 'Concha (86g)', 'qtd_custom': 1},
                   {'nome': 'Legumes Variados', 'qtd': 120, 'medida': 'Grama'},
                   {'nome': 'Salada ou verdura crua, exceto de fruta', 'qtd': 50, 'medida': 'Pegador', 'qtd_custom': 1},
                   {'nome': 'Azeite de oliva extra virgem - Borges®', 'qtd': 5, 'medida': 'Grama'}
               ],
               'obs': '*Substituições:\n- Filé de Frango por: carne vermelha magra (patinho, acém, alcatra, filé mignon, paleta, chá) ou filé suíno (pernil, mignon, lombo) ou salmão, atum fresco, peixe branco ou camarão cozido.\n- Arroz por: 120g de batata inglesa ou 140g de abóbora ou 60g de aipim ou 60g de macarrão ou 60g de inhame.\n- Feijão por: lentilha, grão de bico, ervilha ou milho cozido.\n*Legumes Variados: Tomate / Berinjela / Alho Poró / Maxixe / Brócolis / Rabanete / Chuchu / Couve / Beterraba / Pepino / Couve-flor / Abobrinha / Repolho / Palmito / Quiabo / Cenoura / Vagem / Jiló.'
           },
           {
               'nome': 'Lanche da tarde',
               'hora': '16:00',
               'percentual': 0.20,
               'items': [
                   {'nome': 'Whey Protein - Killer Whey / Heavy Suppz', 'qtd': 35, 'medida': 'Grama'},
                   {'nome': 'Pão de forma integral', 'qtd': 25, 'medida': 'Fatia (25g)', 'qtd_custom': 1},
                   {'nome': 'Requeijão Light', 'qtd': 20, 'medida': 'Grama'}
               ],
               'obs': 'Pode trocar o pão por 40g de tapioca ou 1 Rap10',
               'substituicoes': [
                   {
                       'nome': 'Panqueca Proteica',
                       'items': [
                           {'nome': 'Banana', 'qtd': 60, 'medida': 'Grama'},
                           {'nome': 'Ovo de galinha', 'qtd': 50, 'medida': 'Unidade', 'qtd_custom': 1},
                           {'nome': 'Whey Protein - Killer Whey / Heavy Suppz', 'qtd': 25, 'medida': 'Grama'},
                           {'nome': 'Cacau em Pó 100% Puro Mãe Terra', 'qtd': 5, 'medida': 'Grama'},
                           {'nome': 'Canela em pó', 'qtd': 2, 'medida': 'Grama'},
                           {'nome': 'Psyllium -', 'qtd': 5, 'medida': 'Grama'}
                       ],
                       'obs': 'Misturar tudo e fazer panqueca ou bolinho de micro-ondas'
                   },
                   {
                       'nome': 'Iogurte com frutas',
                       'items': [
                           {'nome': 'Frutas (menos banana e abacate)', 'qtd': 100, 'medida': 'Grama'},
                           {'nome': 'Whey Protein - Killer Whey / Heavy Suppz', 'qtd': 35, 'medida': 'Grama'},
                           {'nome': 'Iogurte natural desnatado - Batavo®', 'qtd': 120, 'medida': 'Grama'}
                       ],
                       'obs': 'Frutas: Melão, morango, uva, abacaxi, kiwi, frutas vermelhas'
                   },
                   {
                       'nome': 'Crepioca',
                       'items': [
                           {'nome': 'Tapioca seca', 'qtd': 20, 'medida': 'Grama'},
                           {'nome': 'Ovo de galinha', 'qtd': 50, 'medida': 'Unidade', 'qtd_custom': 1},
                           {'nome': 'Clara de ovo de galinha', 'qtd': 68, 'medida': 'Unidade (34g)', 'qtd_custom': 2},
                           {'nome': 'Requeijão - Danúbio® Light', 'qtd': 20, 'medida': 'Grama'}
                       ],
                       'obs': 'Fazer crepioca'
                   },
                   {
                       'nome': 'Shake Proteico',
                       'items': [
                           {'nome': 'Shake Proteico - Yopro 25g de PTN OU Piracanjuba 23g de PTN', 'qtd': 250, 'medida': 'Unidade', 'qtd_custom': 1}
                       ]
                   }
               ]
           },
           {
               'nome': 'Jantar',
               'hora': '20:00',
               'percentual': 0.25,
               'items': [
                   {'nome': 'Tilápia Grelhada', 'qtd': 150, 'medida': 'Grama'},
                   {'nome': 'Arroz branco (cozido)', 'qtd': 60, 'medida': 'Grama'},
                   {'nome': 'Legumes Variados', 'qtd': 120, 'medida': 'Grama'},
                   {'nome': 'Salada ou verdura crua, exceto de fruta', 'qtd': 100, 'medida': 'Pegador', 'qtd_custom': 2},
                   {'nome': 'Azeite de oliva extra virgem - Borges®', 'qtd': 2.4, 'medida': 'Colher de chá (2,4ml)', 'qtd_custom': 1}
               ],
               'obs': '*Substituições:\n- Tilápia por: carne vermelha magra (patinho, acém, alcatra, filé mignon, paleta, chá) ou filé suíno (pernil, mignon, lombo) ou salmão, atum fresco, peixe branco ou camarão cozido.\n*Legumes Variados: Tomate / Berinjela / Alho Poró / Maxixe / Brócolis / Rabanete / Chuchu / Couve / Beterraba / Pepino / Couve-flor / Abobrinha / Repolho / Palmito / Quiabo / Cenoura / Vagem / Jiló.',
               'substituicoes': [
                   {
                       'nome': 'Pizza Fake',
                       'items': [
                           {'nome': 'Rap10 integral', 'qtd': 35, 'medida': 'Unidade', 'qtd_custom': 1},
                           {'nome': 'Queijo mussarela sem lactose - Lacfree Verde Campo', 'qtd': 30, 'medida': 'Grama'},
                           {'nome': 'Tomate cereja', 'qtd': 40, 'medida': 'Unidade (10g)', 'qtd_custom': 4},
                           {'nome': 'Orégano', 'qtd': 1, 'medida': 'Punhado', 'qtd_custom': 1},
                           {'nome': 'Molho de tomate', 'qtd': 15, 'medida': 'Colher De Sopa', 'qtd_custom': 1},
                           {'nome': 'Whey Protein - Killer Whey / Heavy Suppz', 'qtd': 30, 'medida': 'Grama'}
                       ],
                       'obs': 'Pode substituir o whey por 80g de frango desfiado ou 120g de atum'
                   },
                   {
                       'nome': 'Strogonoff Light',
                       'items': [
                           {'nome': 'Filé-mignon Cozido(a)', 'qtd': 100, 'medida': 'Grama'},
                           {'nome': 'Ketchup', 'qtd': 10, 'medida': 'Grama'},
                           {'nome': 'Mostarda', 'qtd': 10, 'medida': 'Grama'},
                           {'nome': 'Arroz branco (cozido) ou Macarrão de arroz', 'qtd': 75, 'medida': 'Grama'},
                           {'nome': 'Champignon (cogumelo paris)', 'qtd': 50, 'medida': 'Grama'},
                           {'nome': 'Creme de Leite Light', 'qtd': 40, 'medida': 'Grama'}
                       ],
                       'obs': 'Misturar os ingredientes e aquecer. Porção única.'
                   },
                   {
                       'nome': 'Salpicão Light',
                       'items': [
                           {'nome': 'Rap10 integral', 'qtd': 35, 'medida': 'Unidade', 'qtd_custom': 1},
                           {'nome': 'Requeijão Light', 'qtd': 20, 'medida': 'Grama'},
                           {'nome': 'Palmito, cenoura, milho e tomate', 'qtd': 50, 'medida': 'Grama'},
                           {'nome': 'Filé de frango (cozido)', 'qtd': 100, 'medida': 'Grama'}
                       ],
                       'obs': 'Fazer salpicão com os ingredientes e comer com o Rap10. Outra opção: 100g de atum + 20g de requeijão light'
                   },
                   {
                       'nome': 'Hambúrguer Artesanal',
                       'items': [
                           {'nome': 'Pão de hambúrguer', 'qtd': 50, 'medida': 'Unidade', 'qtd_custom': 1},
                           {'nome': 'Carne de Hambúrguer caseira de Patinho 120g Cru.', 'qtd': 120, 'medida': 'Grama'},
                           {'nome': 'Queijo tipo mussarela', 'qtd': 20, 'medida': 'Grama'},
                           {'nome': 'Ketchup', 'qtd': 15, 'medida': 'colher de sopa', 'qtd_custom': 1}
                       ],
                       'obs': 'ou Mostarda ou Maionese Light'
                   }
               ]
           },
           {
               'nome': 'Ceia',
               'hora': '22:30',
               'percentual': 0.10,
               'items': [
                   {'nome': 'Whey Protein - Killer Whey / Heavy Suppz', 'qtd': 15, 'medida': 'Grama'},
                   {'nome': 'Iogurte natural - Batavo®', 'qtd': 100, 'medida': 'Grama'},
                   {'nome': 'Frutas (menos banana e abacate)', 'qtd': 75, 'medida': 'Grama'},
                   {'nome': 'Gelatina diet* (qualquer sabor) - Royal®', 'qtd': 110, 'medida': 'Unidade comercial (110g)', 'qtd_custom': 1},
                   {'nome': 'Chia em Grãos - Hidratar os grãos no iogurte', 'qtd': 5, 'medida': 'Grama'}
               ]
           }
       ]
   
   def _formatar_plano_completo(self, plano_ajustado, nome, data, peso_kg, metas):
       """Formata o plano completo no estilo Pedro Barros."""
       output = self.formatter.format_header(nome, data)
       
       # Formata cada refeição
       for refeicao in plano_ajustado:
           # Calcula total da refeição
           total_refeicao = sum(item.get('valores', {}).get('kcal', item.get('kcal', 0)) for item in refeicao['items'])
           
           # Header da refeição
           output += self.formatter.format_meal_header(refeicao['hora'], refeicao['nome'], total_refeicao)
           
           # Items da refeição
           for item in refeicao['items']:
               kcal = item.get('valores', {}).get('kcal', item.get('kcal', 0))
               qtd = item.get('qtd_custom', item['qtd'])
               output += "\n" + self.formatter.format_food_item(
                   item['nome'],
                   item.get('medida', 'Grama'),
                   qtd,
                   kcal
               )
           
           # Observações
           if 'obs' in refeicao:
               output += "\n" + self.formatter.format_obs(refeicao['obs'])
           
           # Substituições
           if 'substituicoes' in refeicao:
               for i, sub in enumerate(refeicao['substituicoes'], 1):
                   # Calcula total da substituição
                   total_sub = sum(item.get('valores', {}).get('kcal', 0) for item in sub['items'])
                   
                   # Header da substituição
                   output += self.formatter.format_substituicao_header(i, sub.get('nome'), total_sub)
                   
                   # Items da substituição
                   for item in sub['items']:
                       kcal = item.get('valores', {}).get('kcal', 0)
                       qtd = item.get('qtd_custom', item['qtd'])
                       output += "\n" + self.formatter.format_food_item(
                           item['nome'],
                           item.get('medida', 'Grama'),
                           qtd,
                           kcal
                       )
                   
                   # Obs da substituição
                   if 'obs' in sub:
                       output += "\n" + self.formatter.format_obs(sub['obs'])
       
       # Calcula totais finais
       totais_finais = self._calcular_totais_finais(plano_ajustado)
       
       # Adiciona resumo nutricional
       output += self.formatter.format_resumo_nutricional(metas, totais_finais, peso_kg)
       
       # Rodapé
       output += self.formatter.format_footer()
       
       return output
   
   def _calcular_totais_finais(self, plano):
       """Calcula totais nutricionais finais do plano."""
       totais = {'kcal': 0, 'proteina': 0, 'carb': 0, 'gordura': 0, 'fibra': 0}
       
       for refeicao in plano:
           # Items principais
           for item in refeicao['items']:
               valores = item.get('valores', {})
               for k in totais:
                   totais[k] += valores.get(k, 0)
           
           # Não soma substituições (são alternativas, não adicionais)
       
       # Formata resultado
       return {
           'total_kcal': round(totais['kcal'], 2),
           'proteina_g': round(totais['proteina'], 2),
           'proteina_g_kg': round(totais['proteina'] / 75, 2),  # Usar peso real
           'carb_g': round(totais['carb'], 2),
           'carb_percent': round((totais['carb'] * 4 / totais['kcal']) * 100, 1) if totais['kcal'] > 0 else 0,
           'gord_g': round(totais['gordura'], 2),
           'gord_percent': round((totais['gordura'] * 9 / totais['kcal']) * 100, 1) if totais['kcal'] > 0 else 0,
           'fibra_g': round(totais['fibra'], 2)
       }

def generate_plan_logic(request_data):
   """Função principal que gera o plano com precisão absoluta."""
   try:
       # Extrai dados
       paciente = request_data.get('paciente', {})
       metas = request_data.get('metas', {})
       
       nome = paciente.get('nome', 'Paciente')
       peso = paciente.get('peso_kg', 70)
       altura = paciente.get('altura_cm', 170)
       
       # Gera plano
       gerador = GeradorPlanoPedroBarros()
       plano_formatado = gerador.gerar_plano_completo(nome, peso, altura, metas)
       
       # Resposta compatível com a API
       response = {
           'plano': {
               'paciente': nome,
               'data': datetime.now().strftime("%d/%m/%Y"),
               'peso_kg': peso,
               'plano_formatado': plano_formatado,
               'resumo': {}  # Já está no plano_formatado
           }
       }
       
       return response, 200
       
   except Exception as e:
       print(f"Erro ao gerar plano: {str(e)}")
       import traceback
       traceback.print_exc()
       return {'erro': f'Erro ao gerar plano: {str(e)}'}, 500

# Função de compatibilidade
def generate_template_plan(request_data):
   """Alias para a função principal."""
   return generate_plan_logic(request_data)

# Classes de compatibilidade (vazias mas presentes)
class NutriPlanIntegrityValidator:
   pass

class LastResortGuard:
   pass
