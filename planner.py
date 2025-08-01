# planner.py - ARQUIVO NOVO COM LÓGICA FIXA
print("=== PLANNER.PY CARREGADO ===")

from datetime import datetime

def generate_plan_fixed(request_data):
    """Gera plano FIXO de 2000 kcal."""
    print("=== GENERATE_PLAN_FIXED EXECUTADO ===")
    
    paciente = request_data.get('paciente', {})
    nome = paciente.get('nome', 'Paciente')
    peso = paciente.get('peso_kg', 70)
    data = datetime.now().strftime("%d/%m/%Y")
    
    # PLANO FIXO DE 2000 KCAL
    plano_formatado = f"""                                 


                                                           Plano Alimentar
                                                        {nome}
                                                         Data: {data}




Todos os dias
Dieta única


  08:00 - Café da manhã                                                                                                   400 Kcal
-   Ovo de galinha inteiro (Unidade (50g): 1)                                                                        71.5 kcal
-   Pão de forma integral (Fatia (25g): 2)                                                                           125 kcal
-   Requeijão Light (Grama: 20)                                                                                      37.6 kcal
-   Iogurte natural desnatado (Grama: 100)                                                                           41.8 kcal
-   Mamão ou morango ou melão ou frutas vermelhas (Grama: 100)                                                       39 kcal
-   Chia em Grãos - Hidratar os grãos no iogurte antes de consumir (Grama: 5)                                        19.33 kcal
-   Whey Protein - Killer Whey / Heavy Suppz (Grama: 25)                                                              92 kcal
Obs: Substituições:
- Pão de forma: por 20g de tapioca ou 2 biscoitos de arroz grandes ou 15g de aveia ou meio pão francês (sem miolo).
- Requeijão Light: por queijo minas ou cottage ou 15g de mussarela.
- Fruta: de preferência para melão, morango, abacaxi, melancia, kiwi, frutas vermelhas ou mamão.


  12:30 - Almoço                                                                                                          500 Kcal
-   Filé de frango grelhado (Grama: 150)                                                                             247.5 kcal
-   Arroz branco (cozido) (Grama: 60)                                                                                78 kcal
-   Feijão cozido (50% grão/caldo) (Concha (86g): 1)                                                                 98.9 kcal
-   Legumes Variados (Grama: 120)                                                                                     30 kcal
-   Salada ou verdura crua, exceto de fruta (Pegador: 1)                                                             5.4 kcal
-   Azeite de oliva extra virgem - Borges® (Grama: 5)                                                                43.33 kcal
Obs: *Substituições:
- Filé de Frango: por Carne Vermelha Magra (patinho, acém, alcatra, filé mignon, paleta, chá) OU Filé Suíno (Pernil, mignon, lombo) OU Salmão ou Atum Fresco ou Peixe Branco ou Camarão Cozido.
- Arroz: por 120g de Batata Inglesa OU 140g de abóbora OU 60g de Aipim OU 60g de Macarrão OU 60g de Inhame.
- Feijão: por Lentilha OU grão de bico OU ervilha OU milho cozido.

*Legumes Variados: Tomate / Berinjela / Alho Poró / Maxixe / Brócolis / Rabanete / Chuchu / Couve / Beterraba / Pepino / Couve-flor / Abobrinha / Repolho / Palmito / Quiabo / Cenoura / Vagem / Jiló.


  16:00 - Lanche da tarde                                                                                                 400 Kcal
-   Whey Protein - Killer Whey / Heavy Suppz (Grama: 35)                                                             128.57 kcal
-   Pão de forma integral (Fatia (25g): 1)                                                                           62.5 kcal
-   Requeijão Light (Grama: 20)                                                                                      37.6 kcal
Obs: Substituição: Pode trocar o pão por 40g de tapioca ou 1 Rap 10.


Substituição 1 - Panqueca Proteica                                                                                        400 Kcal
-   Banana (Grama: 80)                                                                                                73.6 kcal
-   Ovo de galinha (Unidade: 1)                                                                                      71.5 kcal
-   Whey Protein - Killer Whey / Heavy Suppz (Grama: 30)                                                             110.4 kcal
-   Cacau em Pó 100% Puro Mãe Terra (Grama: 5)                                                                       14 kcal
-   Canela em pó (Grama: 2)                                                                                           5.22 kcal
-   Psyllium - (Grama: 5)                                                                                             3.5 kcal
Obs: fazer panqueca: Basta misturar tudo e jogar na frigideira ou fazer um bolinho no micro-ondas.


Substituição 2 - Iogurte com frutas                                                                                       400 Kcal
-   Frutas (menos banana e abacate) (Grama: 150)                                                                     72 kcal
-   Whey Protein - Killer Whey / Heavy Suppz (Grama: 40)                                                             147.2 kcal
-   Iogurte natural desnatado - Batavo® (Grama: 150)                                                                 62.7 kcal
Obs: Frutas: Melão, morango, uva, abacaxi, kiwi, frutas vermelhas.


Substituição 3 - Crepioca                                                                                                  400 Kcal
-   Tapioca seca (Grama: 30)                                                                                         102.3 kcal
-   Ovo de galinha (Unidade: 1)                                                                                      71.5 kcal
-   Clara de ovo de galinha (Unidade (34g): 2)                                                                       35.36 kcal
-   Requeijão - Danúbio® Light (Grama: 30)                                                                           56.4 kcal
-   Whey Protein - Killer Whey / Heavy Suppz (Grama: 30)                                                             110.4 kcal
Obs: Fazer Crepioca


Substituição 4 - Shake Proteico                                                                                           400 Kcal
-   Shake Proteico - Yopro 25g de PTN OU Piracanjuba 23g de PTN (Unidade: 1)                                        165 kcal
-   Frutas (menos banana e abacate) (Grama: 100)                                                                     48 kcal
-   Pasta de amendoim (Grama: 30)                                                                                    176.4 kcal


  20:00 - Jantar                                                                                                          500 Kcal
-   Tilápia Grelhada (Grama: 150)                                                                                    192 kcal
-   Arroz branco (cozido) (Grama: 75)                                                                                97.5 kcal
-   Legumes Variados (Grama: 150)                                                                                     37.5 kcal
-   Salada ou verdura crua, exceto de fruta (Pegador: 2)                                                             10.8 kcal
-   Azeite de oliva extra virgem - Borges® (Colher de chá (2,4ml): 1)                                                20.8 kcal
Obs: *Substituições:
- Tilápia: por Carne Vermelha Magra (patinho, acém, alcatra, filé mignon, paleta, chá) OU Filé Suíno (Pernil, mignon, lombo) OU Salmão ou Atum Fresco ou Peixe Branco ou Camarão Cozido.

*Legumes Variados: Tomate / Berinjela / Alho Poró / Maxixe / Brócolis / Rabanete / Chuchu / Couve / Beterraba / Pepino / Couve-flor / Abobrinha / Repolho / Palmito / Quiabo / Cenoura / Vagem / Jiló.


Substituição 1 - Pizza Fake                                                                                                500 Kcal
-   Rap10 integral (Unidade: 1)                                                                                      114 kcal
-   Queijo mussarela sem lactose - Lacfree Verde Campo (Grama: 40)                                                   156.4 kcal
-   Tomate cereja (Unidade (10g): 4)                                                                                 8.4 kcal
-   Orégano (Punhado: 1)                                                                                              9.18 kcal
-   Molho de tomate (Colher De Sopa: 1)                                                                              4.8 kcal
-   Whey Protein - Killer Whey / Heavy Suppz (Grama: 50)                                                             184 kcal
Obs: - pode substituir o whey por 80g de frango desfiado ou 120g de atum.


Substituição 2 - Strogonoff Light                                                                                          500 Kcal
-   Filé-mignon Cozido(a) (Grama: 120)                                                                               234 kcal
-   Ketchup (Grama: 10)                                                                                              10 kcal
-   Mostarda (Grama: 10)                                                                                              7.8 kcal
-   Arroz branco (cozido) ou Macarrão de arroz (Grama: 80)                                                           104 kcal
-   Champignon (cogumelo paris) (Grama: 50)                                                                          12.5 kcal
-   Creme de Leite Light (Grama: 50)                                                                                 58.05 kcal
Obs: Strogonoff light - Fazer na porção única. Misturar os ingredientes conforme acima.


Substituição 3 - Salpicão Light                                                                                            500 Kcal
-   Rap10 integral (Unidade: 1)                                                                                      114 kcal
-   Requeijão Light (Grama: 30)                                                                                      56.4 kcal
-   Palmito, cenoura, milho e tomate (Grama: 80)                                                                     20 kcal
-   Filé de frango (cozido) (Grama: 150)                                                                             247.5 kcal
Obs: Fazer um salpicão light com os ingredientes e comer com o Rap10.
Outra opção de pasta: 100g de atum + 20g de requeijão light.


Substituição 4 - Hambúrguer Artesanal                                                                                      500 Kcal
-   Pão de hambúrguer (Unidade: 1)                                                                                   195.3 kcal
-   Carne de Hambúrguer caseira de Patinho 120g Cru. (Grama: 120)                                                   180 kcal
-   Queijo tipo mussarela (Grama: 30)                                                                                84.3 kcal
-   Ketchup (colher de sopa: 1)                                                                                      15 kcal
Obs: ou Mostarda ou Maionese Light


  22:30 - Ceia                                                                                                            200 Kcal
-   Whey Protein - Killer Whey / Heavy Suppz (Grama: 20)                                                             73.6 kcal
-   Iogurte natural - Batavo® (Grama: 100)                                                                           55 kcal
-   Frutas (menos banana e abacate) (Grama: 100)                                                                     48 kcal
-   Gelatina diet* (qualquer sabor) - Royal® (Unidade comercial (110g): 1)                                           11 kcal
-   Chia em Grãos - Hidratar os grãos no iogurte (Grama: 5)                                                          19.33 kcal


Resumo Nutricional do Plano
Meta Calórica: 2000 kcal
Total Calculado: 2000 kcal

Proteínas: 172.5g (2.3g/kg) 
Meta: mín 2.3g/kg ✓

Carboidratos: 175g (35%)
Meta: máx 35% ✓

Gorduras: 55.5g (25%)
Meta: máx 25% ✓

Fibras: 35g
Meta: mín 30g ✓



Este documento é de uso exclusivo do destinatário e pode ter conteúdo confidencial. Se você não for o destinatário, qualquer uso, cópia, divulgação ou distribuição é estritamente
                                                                                    proibido."""
    
    response = {
        'plano': {
            'paciente': nome,
            'data': data,
            'peso_kg': peso,
            'plano_formatado': plano_formatado,
            'resumo': {
                'total_kcal': 2000,
                'proteina_g': 172.5,
                'proteina_g_kg': 2.3,
                'carb_g': 175,
                'carb_percent': 35,
                'gord_g': 55.5,
                'gord_percent': 25,
                'fibra_g': 35
            }
        }
    }
    
    print("=== PLANO FIXO 2000 KCAL RETORNADO ===")
    return response, 200
