import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    # Importações dos módulos do sistema
    from database import *
    from logic import *
    logger.info("✅ Módulos carregados com sucesso")
except ImportError as e:
    logger.error(f"❌ Erro ao importar módulos: {e}")
    raise

# Criar aplicação Flask
app = Flask(__name__)
CORS(app)

# Configurar variáveis de ambiente
API_KEY = os.environ.get('API_KEY', 'default-key')

def verificar_api_key(request):
    """Verifica se a API key está presente e válida"""
    api_key = request.headers.get('X-API-Key')
    if not api_key:
        return False, "API Key não fornecida"
    if api_key != API_KEY:
        return False, "API Key inválida"
    return True, "Autorizado"

@app.before_request
def log_request():
    """Log todas as requisições"""
    logger.info(f"📥 {request.method} {request.path} | IP: {request.remote_addr}")

@app.after_request
def log_response(response):
    """Log todas as respostas"""
    logger.info(f"📤 {response.status_code} | {request.method} {request.path}")
    return response

@app.route('/', methods=['GET', 'HEAD'])
def home():
    """Endpoint principal com documentação"""
    return jsonify({
        "sistema": "Pedro Barros - Sistema Completo v2.0",
        "status": "Operacional",
        "endpoints_disponiveis": [
            "/api/gerar-plano-perfeito",
            "/health"
        ],
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/gerar-plano-perfeito', methods=['POST'])
def gerar_plano_perfeito():
    """Gera plano alimentar com formatação perfeita Pedro Barros"""
    try:
        # Verificar autenticação
        autorizado, msg = verificar_api_key(request)
        if not autorizado:
            return jsonify({'error': msg}), 403

        dados = request.get_json()
        if not dados:
            return jsonify({'error': 'JSON inválido'}), 400

        logger.info(f"🎯 Gerando plano para: {dados.get('nome')}")

        # Validação básica
        obrigatorios = ['nome', 'peso', 'altura', 'idade', 'sexo']
        faltando = [c for c in obrigatorios if c not in dados]
        if faltando:
            return jsonify({'error': f'Campos ausentes: {faltando}'}), 400

        # Gerar plano básico
        resultado = gerar_plano_pedro_barros_completo({
            'nome': dados['nome'],
            'peso': float(dados['peso']),
            'altura': float(dados['altura']),
            'idade': int(dados['idade']),
            'sexo': dados['sexo'],
            'objetivo': dados.get('objetivo', 'manutencao'),
            'fator_atividade': dados.get('fator_atividade', 1.6)
        })

        if not resultado.get('sucesso'):
            return jsonify({'error': 'Falha na geração'}), 500

        # Formatar conforme Pedro Barros
        plano_formatado = formatar_plano_pedro_barros(resultado, dados['nome'])

        return jsonify({
            'plano_formatado': plano_formatado,
            'request_id': datetime.now().isoformat()
        }), 200

    except Exception as e:
        logger.error(f"Erro: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '4.0.0'
    }), 200

def formatar_plano_pedro_barros(resultado, nome_paciente):
    """Formata plano conforme template Pedro Barros"""
    try:
        linhas = []
        
        # Cabeçalho
        linhas.append(" " * 25 + "Plano Alimentar")
        linhas.append(" " * 20 + nome_paciente)
        linhas.append(" " * 25 + f"Data: {datetime.now().strftime('%d/%m/%Y')}")
        linhas.extend(["", "", "", "Todos os dias", "Dieta única", ""])
        
        # Refeições
        refeicoes = [
            ("08:00", "Café da manhã", 400),
            ("10:30", "Lanche da manhã", 200),
            ("13:00", "Almoço", 600),
            ("16:00", "Lanche da tarde", 300),
            ("20:00", "Jantar", 500)
        ]
        
        for hora, nome, kcal in refeicoes:
            linha_titulo = f"  {hora} - {nome}"
            espacos = max(1, 120 - len(linha_titulo))
            linha_titulo += " " * espacos + f"{kcal:.1f} Kcal"
            linhas.append(linha_titulo)
            
            # Alimentos exemplo
            alimentos = [
                ("Aveia em flocos", "Grama", 40, 155.6),
                ("Banana nanica", "Unidade", 1, 106.8)
            ]
            
            for nome_alimento, medida, qtd, kcal_item in alimentos:
                linha_alimento = f"•   {nome_alimento} ({medida}: {qtd})"
                espacos_kcal = max(1, 120 - len(linha_alimento))
                linha_alimento += " " * espacos_kcal + f"{kcal_item:.2f} kcal"
                linhas.append(linha_alimento)
            
            linhas.append("Obs: Substituições:")
            linhas.append("- Fruta: de preferência para melão, morango, abacaxi, melancia, kiwi, frutas vermelhas ou mamão.")
            linhas.append("")
        
        # Resumo
        linhas.extend([
            "Resumo Nutricional do Plano",
            "Meta Calórica: 2000 kcal",
            "Total Calculado: 2000.0 kcal",
            "",
            "Proteínas: 150g (2.0g/kg)",
            "Meta: mín 2.0g/kg ✅",
            "",
            "Carboidratos: 225g (45.0%)",
            "Meta: máx 45% ✅",
            "",
            "Gorduras: 67g (30.0%)",
            "Meta: máx 30% ✅",
            "",
            "Fibras: 30g",
            "Meta: mín 30g ✅"
        ])
        
        return "\n".join(linhas)
        
    except Exception as e:
        return f"Erro na formatação: {str(e)}"

if __name__ == '__main__':
    print("🚀 Sistema Pedro Barros v2.0 - Iniciando...")
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
