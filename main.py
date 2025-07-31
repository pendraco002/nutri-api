# main.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime
from logic import generate_plan_logic
from database import validate_food_data

app = Flask(__name__)

# Configurar CORS
CORS(app, origins=['*'])

# Configuração básica
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

# Validar dados ao iniciar
validation_result = validate_food_data()
if not validation_result['valid']:
    print(f"⚠️ Erros na base de dados: {validation_result['errors']}")
else:
    print(f"✅ Base validada: {validation_result['total_foods']} alimentos")

@app.route('/')
def home():
    return jsonify({
        "message": "NutriAPI v4.0 - Motor de Cálculo Nutricional",
        "status": "online",
        "endpoints": {
            "/": "Esta mensagem",
            "/health": "Status da API",
            "/gerarPlano": "POST - Gerar plano alimentar"
        }
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "4.0.0"
    })

@app.route('/gerarPlano', methods=['POST'])
def gerar_plano():
    try:
        # Validar API Key
        api_key = request.headers.get('X-API-Key')
        if not api_key or api_key != os.getenv('API_KEY', 'default-key'):
            return jsonify({'error': 'API Key inválida'}), 401
        
        # Obter dados da requisição
        data = request.get_json()
        
        # Validações básicas
        if not data:
            return jsonify({'error': 'Dados não fornecidos'}), 400
            
        if 'paciente' not in data:
            return jsonify({'error': 'Dados do paciente são obrigatórios'}), 400
            
        if 'peso_kg' not in data['paciente']:
            return jsonify({'error': 'Peso do paciente é obrigatório'}), 400
        
        # Gerar plano
        result, status_code = generate_plan_logic(data)
        
        # Adicionar request_id se sucesso
        if status_code == 200:
            result['request_id'] = f"req_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        return jsonify(result), status_code
        
    except Exception as e:
        print(f"Erro ao gerar plano: {str(e)}")
        return jsonify({
            'error': 'Erro interno ao processar requisição',
            'details': str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint não encontrado'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Erro interno do servidor'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
