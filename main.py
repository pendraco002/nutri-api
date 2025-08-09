import logging
from flask import Flask, request, jsonify
from datetime import datetime
from database import load_alimentos
from logic import calcular_plano
from integracao_perfeita import gerar_plano_formatacao_perfeita

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/api/gerar-plano-perfeito', methods=['POST'])
def gerar_plano_perfeito():
    try:
        dados = request.get_json()
        logger.info(f"🎯 GERAÇÃO PERFEITA iniciada para: {dados.get('nome')}")

        obrigatorios = ['nome','peso','altura','idade','sexo','objetivo','fator_atividade']
        faltando = [c for c in obrigatorios if c not in dados]
        if faltando:
            return jsonify({'error': f'Campos ausentes: {faltando}'}), 400

        plano_base = calcular_plano(
            nome=dados['nome'],
            peso=dados['peso'],
            altura=dados['altura'],
            idade=dados['idade'],
            sexo=dados['sexo'],
            objetivo=dados['objetivo'],
            fator_atividade=dados['fator_atividade'],
            restricoes=dados.get('restricoes', {})
        )

        plano_formatado = gerar_plano_formatacao_perfeita(plano_base)

        return jsonify({
            'plano_formatado': plano_formatado,
            'request_id': datetime.now().isoformat()
        }), 200

    except Exception as e:
        logger.error(f"Erro ao gerar plano: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '4.0.0',
        'uptime': 0
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=False)
