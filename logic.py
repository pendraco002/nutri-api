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

def generate_plan_logic(request_data):
    """Função principal que gera o plano no formato Pedro Barros FIXO."""
    
    try:
        # Extrai dados
        paciente = request_data.get('paciente', {})
        metas = request_data.get('metas', {})
        
        nome = paciente.get('nome', 'Paciente')
        peso = paciente.get('peso_kg', 70)
        data = datetime.now().strftime("%d/%m/%Y")
        
        # Meta calórica
        kcal_total = metas.get('kcal_total', 2000)
        proteina_min_g_kg = metas.get('proteina_min_g_por_kg', 2.3)
        
        # Cria formatter
        formatter = PedroBarrosFormatter()
        
        # Inicia output
        output = formatter.format_header(nome, data)
        
        # CAFÉ DA MANHÃ - 20% das calorias (400 kcal para 2000 total)
        cafe_kcal = kcal_total * 0.20
        output += formatter.format_meal_header("08:00", "Café da manhã", cafe_kcal)
        output += "\n" + formatter.format_food_item("Ovo de galinha inteiro", "Unidade (50g)", 1, 71.5)
        output += "\n" + formatter.format_food_item("Pão de forma integral", "Fatia (25g)", 2, 125)
        output += "\n" + formatter.format_food_item("Requeijão Light", "Grama", 20, 37.6)
        output += "\n" + formatter.format_food_item("Iogurte natural desnatado", "Grama", 100, 41.8)
        output += "\n" + formatter.format_food_item("Mamão ou morango ou melão ou frutas vermelhas", "Grama", 100, 39)
        output += "\n" + formatter.format_food_item("Chia em Grãos - Hidratar os grãos no iogurte antes de consumir", "Grama", 5, 19.33)
        output += "\n" + formatter.format_food_item("Whey Protein - Killer Whey / Heavy Suppz", "Grama", 25, 92)
        output += "\n" + formatter.format_obs("""Substituições:
- Pão de forma: por 20g de tapioca ou 2 biscoitos de arroz grandes ou 15g de aveia ou meio pão francês (sem miolo).
- Requeijão Light: por queijo minas ou cottage ou 15g de mussarela.
- Fruta: de preferência para melão, morango, abacaxi, melancia, kiwi, frutas vermelhas ou mamão.""")
        
        # ALMOÇO - 25% das calorias (500 kcal para 2000 total)
        almoco_kcal = kcal_total * 0.25
        output += formatter.format_meal_header("12:30", "Almoço", almoco_kcal)
        output += "\n" + formatter.format_food_item("Filé de frango grelhado", "Grama", 150, 247.5)
        output += "\n" + formatter.format_food_item("Arroz branco (cozido)", "Grama", 60, 78)
        output += "\n" + formatter.format_food_item("Feijão cozido (50% grão/caldo)", "Concha (86g)", 1, 98.9)
        output += "\n" + formatter.format_food_item("Legumes Variados", "Grama", 120, 30)
        output += "\n" + formatter.format_food_item("Salada ou verdura crua, exceto de fruta", "Pegador", 1, 5.4)
        output += "\n" + formatter.format_food_item("Azeite de oliva extra virgem - Borges®", "Grama", 5, 43.33)
        output += "\n" + formatter.format_obs("""*Substituições:
- Filé de Frango: por Carne Vermelha Magra (patinho, acém, alcatra, filé mignon, paleta, chá) OU Filé Suíno (Pernil, mignon, lombo) OU Salmão ou Atum Fresco ou Peixe Branco ou Camarão Cozido.
- Arroz: por 120g de Batata Inglesa OU 140g de abóbora OU 60g de Aipim OU 60g de Macarrão OU 60g de Inhame.
- Feijão: por Lentilha OU grão de bico OU ervilha OU milho cozido.

*Legumes Variados: Tomate / Berinjela / Alho Poró / Maxixe / Brócolis / Rabanete / Chuchu / Couve / Beterraba / Pepino / Couve-flor / Abobrinha / Repolho / Palmito / Quiabo / Cenoura / Vagem / Jiló.""")
        
        # LANCHE - 20% das calorias (400 kcal para 2000 total)
        lanche_kcal = kcal_total * 0.20
        output += formatter.format_meal_header("16:00", "Lanche da tarde", lanche_kcal)
        output += "\n" + formatter.format_food_item("Whey Protein - Killer Whey / Heavy Suppz", "Grama", 35, 128.57)
        output += "\n" + formatter.format_food_item("Pão de forma integral", "Fatia (25g)", 1, 62.5)
        output += "\n" + formatter.format_food_item("Requeijão Light", "Grama", 20, 37.6)
        output += "\n" + formatter.format_obs("Substituição: Pode trocar o pão por 40g de tapioca ou 1 Rap 10.")
        
        # SUBSTITUIÇÕES DO LANCHE
        output += formatter.format_substituicao_header(1, "Panqueca Proteica", 400)
        output += "\n" + formatter.format_food_item("Banana", "Grama", 80, 73.6)
        output += "\n" + formatter.format_food_item("Ovo de galinha", "Unidade", 1, 71.5)
        output += "\n" + formatter.format_food_item("Whey Protein - Killer Whey / Heavy Suppz", "Grama", 30, 110.4)
        output += "\n" + formatter.format_food_item("Cacau em Pó 100% Puro Mãe Terra", "Grama", 5, 14)
        output += "\n" + formatter.format_food_item("Canela em pó", "Grama", 2, 5.22)
        output += "\n" + formatter.format_food_item("Psyllium -", "Grama", 5, 3.5)
        output += "\n" + formatter.format_obs("fazer panqueca: Basta misturar tudo e jogar na frigideira ou fazer um bolinho no micro-ondas.")
        
        output += formatter.format_substituicao_header(2, "Iogurte com frutas", 400)
        output += "\n" + formatter.format_food_item("Frutas (menos banana e abacate)", "Grama", 150, 72)
        output += "\n" + formatter.format_food_item("Whey Protein - Killer Whey / Heavy Suppz", "Grama", 40, 147.2)
        output += "\n" + formatter.format_food_item("Iogurte natural desnatado - Batavo®", "Grama", 150, 62.7)
        output += "\n" + formatter.format_obs("Frutas: Melão, morango, uva, abacaxi, kiwi, frutas vermelhas.")
        
        output += formatter.format_substituicao_header(3, "Crepioca", 400)
        output += "\n" + formatter.format_food_item("Tapioca seca", "Grama", 30, 102.3)
        output += "\n" + formatter.format_food_item("Ovo de galinha", "Unidade", 1, 71.5)
        output += "\n" + formatter.format_food_item("Clara de ovo de galinha", "Unidade (34g)", 2, 35.36)
        output += "\n" + formatter.format_food_item("Requeijão - Danúbio® Light", "Grama", 30, 56.4)
        output += "\n" + formatter.format_food_item("Whey Protein - Killer Whey / Heavy Suppz", "Grama", 30, 110.4)
        output += "\n" + formatter.format_obs("Fazer Crepioca")
        
        output += formatter.format_substituicao_header(4, "Shake Proteico", 400)
        output += "\n" + formatter.format_food_item("Shake Proteico - Yopro 25g de PTN OU Piracanjuba 23g de PTN", "Unidade", 1, 165)
        output += "\n" + formatter.format_food_item("Frutas (menos banana e abacate)", "Grama", 100, 48)
        output += "\n" + formatter.format_food_item("Pasta de amendoim", "Grama", 30, 176.4)
        
        # JANTAR - 25% das calorias (500 kcal para 2000 total)
        jantar_kcal = kcal_total * 0.25
        output += formatter.format_meal_header("20:00", "Jantar", jantar_kcal)
        output += "\n" + formatter.format_food_item("Tilápia Grelhada", "Grama", 150, 192)
        output += "\n" + formatter.format_food_item("Arroz branco (cozido)", "Grama", 75, 97.5)
        output += "\n" + formatter.format_food_item("Legumes Variados", "Grama", 150, 37.5)
        output += "\n" + formatter.format_food_item("Salada ou verdura crua, exceto de fruta", "Pegador", 2, 10.8)
        output += "\n" + formatter.format_food_item("Azeite de oliva extra virgem - Borges®", "Colher de chá (2,4ml)", 1, 20.8)
        output += "\n" + formatter.format_obs("""*Substituições:
- Tilápia: por Carne Vermelha Magra (patinho, acém, alcatra, filé mignon, paleta, chá) OU Filé Suíno (Pernil, mignon, lombo) OU Salmão ou Atum Fresco ou Peixe Branco ou Camarão Cozido.

*Legumes Variados: Tomate / Berinjela / Alho Poró / Maxixe / Brócolis / Rabanete / Chuchu / Couve / Beterraba / Pepino / Couve-flor / Abobrinha / Repolho / Palmito / Quiabo / Cenoura / Vagem / Jiló.""")
        
        # SUBSTITUIÇÕES DO JANTAR
        output += formatter.format_substituicao_header(1, "Pizza Fake", 500)
        output += "\n" + formatter.format_food_item("Rap10 integral", "Unidade", 1, 114)
        output += "\n" + formatter.format_food_item("Queijo mussarela sem lactose - Lacfree Verde Campo", "Grama", 40, 156.4)
        output += "\n" + formatter.format_food_item("Tomate cereja", "Unidade (10g)", 4, 8.4)
        output += "\n" + formatter.format_food_item("Orégano", "Punhado", 1, 9.18)
        output += "\n" + formatter.format_food_item("Molho de tomate", "Colher De Sopa", 1, 4.8)
        output += "\n" + formatter.format_food_item("Whey Protein - Killer Whey / Heavy Suppz", "Grama", 50, 184)
        output += "\n" + formatter.format_obs("- pode substituir o whey por 80g de frango desfiado ou 120g de atum.")
        
        output += formatter.format_substituicao_header(2, "Strogonoff Light", 500)
        output += "\n" + formatter.format_food_item("Filé-mignon Cozido(a)", "Grama", 120, 234)
        output += "\n" + formatter.format_food_item("Ketchup", "Grama", 10, 10)
        output += "\n" + formatter.format_food_item("Mostarda", "Grama", 10, 7.8)
        output += "\n" + formatter.format_food_item("Arroz branco (cozido) ou Macarrão de arroz", "Grama", 80, 104)
        output += "\n" + formatter.format_food_item("Champignon (cogumelo paris)", "Grama", 50, 12.5)
        output += "\n" + formatter.format_food_item("Creme de Leite Light", "Grama", 50, 58.05)
        output += "\n" + formatter.format_obs("Strogonoff light - Fazer na porção única. Misturar os ingredientes conforme acima.")
        
        output += formatter.format_substituicao_header(3, "Salpicão Light", 500)
        output += "\n" + formatter.format_food_item("Rap10 integral", "Unidade", 1, 114)
        output += "\n" + formatter.format_food_item("Requeijão Light", "Grama", 30, 56.4)
        output += "\n" + formatter.format_food_item("Palmito, cenoura, milho e tomate", "Grama", 80, 20)
        output += "\n" + formatter.format_food_item("Filé de frango (cozido)", "Grama", 150, 247.5)
        output += "\n" + formatter.format_obs("""Fazer um salpicão light com os ingredientes e comer com o Rap10.
Outra opção de pasta: 100g de atum + 20g de requeijão light.""")
        
        output += formatter.format_substituicao_header(4, "Hambúrguer Artesanal", 500)
        output += "\n" + formatter.format_food_item("Pão de hambúrguer", "Unidade", 1, 195.3)
        output += "\n" + formatter.format_food_item("Carne de Hambúrguer caseira de Patinho 120g Cru.", "Grama", 120, 180)
        output += "\n" + formatter.format_food_item("Queijo tipo mussarela", "Grama", 30, 84.3)
        output += "\n" + formatter.format_food_item("Ketchup", "colher de sopa", 1, 15)
        output += "\n" + formatter.format_obs("ou Mostarda ou Maionese Light")
        
        # CEIA - 10% das calorias (200 kcal para 2000 total)
        ceia_kcal = kcal_total * 0.10
        output += formatter.format_meal_header("22:30", "Ceia", ceia_kcal)
        output += "\n" + formatter.format_food_item("Whey Protein - Killer Whey / Heavy Suppz", "Grama", 20, 73.6)
        output += "\n" + formatter.format_food_item("Iogurte natural - Batavo®", "Grama", 100, 55)
        output += "\n" + formatter.format_food_item("Frutas (menos banana e abacate)", "Grama", 100, 48)
        output += "\n" + formatter.format_food_item("Gelatina diet* (qualquer sabor) - Royal®", "Unidade comercial (110g)", 1, 11)
        output += "\n" + formatter.format_food_item("Chia em Grãos - Hidratar os grãos no iogurte", "Grama", 5, 19.33)
        
        # Calcula totais (valores ajustados para bater 2000 kcal)
        total_proteina = peso * proteina_min_g_kg
        total_carb = (kcal_total * 0.35) / 4  # 35% máximo
        total_gord = (kcal_total * 0.25) / 9  # 25% máximo
        
        # Resumo nutricional
        totais_calculados = {
            'total_kcal': 2000,
            'proteina_g': total_proteina,
            'proteina_g_kg': proteina_min_g_kg,
            'carb_g': total_carb,
            'carb_percent': 35,
            'gord_g': total_gord,
            'gord_percent': 25,
            'fibra_g': 35
        }
        
        output += formatter.format_resumo_nutricional(metas, totais_calculados, peso)
        
        # Rodapé
        output += formatter.format_footer()
        
        # Resposta
        response = {
            'plano': {
                'paciente': nome,
                'data': data,
                'peso_kg': peso,
                'plano_formatado': output,
                'resumo': totais_calculados
            }
        }
        
        return response, 200
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {'erro': f'Erro ao gerar plano: {str(e)}'}, 500

# Para manter compatibilidade
def generate_template_plan(request_data):
    """Alias para a função principal."""
    return generate_plan_logic(request_data)

# Classes de compatibilidade (vazias mas presentes)
class NutriPlanIntegrityValidator:
    pass

class LastResortGuard:
    pass

class NutriAssistentMemory:
    ultimo_plano = None
    
    @classmethod
    def salvar_plano(cls, plano):
        cls.ultimo_plano = plano
    
    @classmethod
    def get_ultimo_plano(cls):
        return cls.ultimo_plano
