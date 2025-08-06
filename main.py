"""
Main API - Sistema de Planos Nutricionais Otimizado
Padrão Pedro Barros - Versão com Gestão de 8.000 Caracteres
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from typing import Dict, Optional
import logging

# Importa os módulos otimizados
from data_manager import DataManager
from plan_builder import PlanBuilder
from plan_formatter import PlanFormatter

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Permite requisições cross-origin

# Inicialização dos componentes
data_manager = DataManager()
plan_builder = PlanBuilder(data_manager)
plan_formatter = PlanFormatter()

# Cache para planos divididos
planos_cache = {}

def validar_entrada(dados: Dict) -> tuple[bool, str]:
    """Valida os dados de entrada da requisição"""
    try:
        # Valida estrutura do paciente
        paciente = dados.get("paciente", {})
        required_paciente = ["nome", "peso_kg", "altura_cm", "sexo"]
        for campo in required_paciente:
            if campo not in paciente:
                return False, f"Campo obrigatório ausente: paciente.{campo}"
        
        # Valida tipos
        if not isinstance(paciente["peso_kg"], (int, float)) or paciente["peso_kg"] <= 0:
            return False, "peso_kg deve ser um número positivo"
        
        if not isinstance(paciente["altura_cm"], (int, float)) or paciente["altura_cm"] <= 0:
            return False, "altura_cm deve ser um número positivo"
        
        if paciente["sexo"] not in ["M", "F"]:
            return False, "sexo deve ser 'M' ou 'F'"
        
        # Valida estrutura das metas
        metas = dados.get("metas", {})
        required_metas = ["kcal_total", "proteina_min_g_por_kg", "carboidrato_max_percent", "gordura_max_percent", "fibras_min_g"]
        for campo in required_metas:
            if campo not in metas:
                return False, f"Campo obrigatório ausente: metas.{campo}"
            
            if not isinstance(metas[campo], (int, float)) or metas[campo] <= 0:
                return False, f"metas.{campo} deve ser um número positivo"
        
        # Valida percentuais
        if metas["carboidrato_max_percent"] > 100:
            return False, "carboidrato_max_percent não pode exceder 100%"
        
        if metas["gordura_max_percent"] > 100:
            return False, "gordura_max_percent não pode exceder 100%"
        
        return True, "Dados válidos"
    
    except Exception as e:
        return False, f"Erro na validação: {str(e)}"

def gerar_plano_automatico(paciente: Dict, metas: Dict) -> Dict:
    """Gera um plano nutricional automático baseado nas metas"""
    try:
        # Por enquanto, usa o plano de exemplo
        # Em uma versão futura, isso seria substituído por lógica mais sofisticada
        plano_base = plan_builder.criar_plano_exemplo()
        
        # Atualiza com os dados do paciente
        plano_base["paciente"] = paciente
        
        # Recalcula necessidades com as metas fornecidas
        necessidades = plan_builder.calcular_necessidades_basicas(paciente, metas)
        plano_base["necessidades"] = necessidades
        
        # Recalcula resumo nutricional
        totais = plano_base["totais"]
        plano_base["resumo_nutricional"] = plan_builder._criar_resumo_nutricional(necessidades, totais)
        
        return plano_base
    
    except Exception as e:
        logger.error(f"Erro ao gerar plano automático: {str(e)}")
        raise

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint de verificação de saúde da API"""
    return jsonify({
        "status": "healthy",
        "message": "API Pedro Barros funcionando",
        "version": "2.0-otimizada"
    })

@app.route('/gerar-plano', methods=['POST'])
def gerar_plano():
    """Endpoint principal para geração de planos nutricionais"""
    try:
        # Valida Content-Type
        if not request.is_json:
            return jsonify({
                "erro": "Content-Type deve ser application/json"
            }), 400
        
        dados = request.get_json()
        
        # Valida entrada
        valido, mensagem = validar_entrada(dados)
        if not valido:
            return jsonify({
                "erro": f"Dados inválidos: {mensagem}"
            }), 400
        
        # Gera o plano nutricional
        paciente = dados["paciente"]
        metas = dados["metas"]
        
        logger.info(f"Gerando plano para {paciente['nome']}")
        
        plano = gerar_plano_automatico(paciente, metas)
        
        # Processa formatação com gestão de limite
        resultado = plan_formatter.processar_plano(plano)
        
        # Salva no cache se foi dividido
        if resultado["status"] == "dividido":
            cache_key = f"{paciente['nome']}_{hash(str(dados))}"
            planos_cache[cache_key] = {
                "continuacao": resultado["continuacao"],
                "plano_completo": plano
            }
            
            # Adiciona chave do cache na resposta
            resultado["cache_key"] = cache_key
        
        # Prepara resposta
        resposta = {
            "plano": {
                "plano_formatado": resultado["plano_formatado"],
                "continuacao_disponivel": resultado["continuacao_disponivel"]
            },
            "metadata": {
                "status": resultado["status"],
                "tamanho": resultado.get("tamanho_essencial", resultado.get("tamanho_total", 0)),
                "mensagem": resultado["mensagem"],
                "paciente": paciente["nome"],
                "data_geracao": plano["data"]
            }
        }
        
        # Adiciona cache_key se necessário
        if "cache_key" in resultado:
            resposta["metadata"]["cache_key"] = resultado["cache_key"]
        
        logger.info(f"Plano gerado com sucesso para {paciente['nome']} - Status: {resultado['status']}")
        
        return jsonify(resposta)
    
    except Exception as e:
        logger.error(f"Erro ao gerar plano: {str(e)}")
        return jsonify({
            "erro": "Erro interno do servidor",
            "detalhes": str(e)
        }), 500

@app.route('/continuar-plano', methods=['POST'])
def continuar_plano():
    """Endpoint para obter a continuação de um plano dividido"""
    try:
        dados = request.get_json()
        cache_key = dados.get("cache_key")
        
        if not cache_key:
            return jsonify({
                "erro": "cache_key é obrigatório"
            }), 400
        
        if cache_key not in planos_cache:
            return jsonify({
                "erro": "Plano não encontrado ou expirado"
            }), 404
        
        plano_cache = planos_cache[cache_key]
        
        resposta = {
            "plano": {
                "plano_formatado": plano_cache["continuacao"],
                "continuacao_disponivel": False
            },
            "metadata": {
                "status": "continuacao",
                "tipo": "substituicoes_e_receitas",
                "mensagem": "Continuação do plano entregue com sucesso"
            }
        }
        
        # Remove do cache após uso
        del planos_cache[cache_key]
        
        return jsonify(resposta)
    
    except Exception as e:
        logger.error(f"Erro ao continuar plano: {str(e)}")
        return jsonify({
            "erro": "Erro interno do servidor",
            "detalhes": str(e)
        }), 500

@app.route('/debug', methods=['POST'])
def debug_plano():
    """Endpoint de debug para análise detalhada"""
    try:
        dados = request.get_json()
        
        # Valida entrada
        valido, mensagem = validar_entrada(dados)
        if not valido:
            return jsonify({
                "erro": f"Dados inválidos: {mensagem}"
            }), 400
        
        # Gera plano
        paciente = dados["paciente"]
        metas = dados["metas"]
        plano = gerar_plano_automatico(paciente, metas)
        
        # Análise de tamanho
        verificacao = plan_formatter.verificar_tamanho_plano(plano)
        
        # Formata versões
        plano_essencial = plan_formatter.formatar_plano_essencial(plano)
        plano_completo = plan_formatter.formatar_plano_completo(plano)
        
        return jsonify({
            "debug": {
                "dados_entrada": dados,
                "plano_estruturado": plano,
                "verificacao_tamanho": verificacao,
                "tamanho_essencial": len(plano_essencial),
                "tamanho_completo": len(plano_completo),
                "limite_caracteres": plan_formatter.LIMITE_CARACTERES,
                "precisa_dividir": verificacao["precisa_dividir"]
            },
            "plano_essencial": plano_essencial,
            "plano_completo": plano_completo
        })
    
    except Exception as e:
        logger.error(f"Erro no debug: {str(e)}")
        return jsonify({
            "erro": "Erro interno do servidor",
            "detalhes": str(e)
        }), 500

@app.route('/limpar-cache', methods=['POST'])
def limpar_cache():
    """Endpoint para limpar o cache de planos"""
    global planos_cache
    quantidade = len(planos_cache)
    planos_cache.clear()
    
    return jsonify({
        "mensagem": f"Cache limpo com sucesso",
        "planos_removidos": quantidade
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "erro": "Endpoint não encontrado",
        "endpoints_disponiveis": [
            "/health",
            "/gerar-plano",
            "/continuar-plano",
            "/debug",
            "/limpar-cache"
        ]
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "erro": "Erro interno do servidor",
        "mensagem": "Contate o suporte técnico"
    }), 500

if __name__ == '__main__':
    # Configuração para desenvolvimento
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Iniciando API Pedro Barros na porta {port}")
    logger.info(f"Debug mode: {debug}")
    
    app.run(host='0.0.0.0', port=port, debug=debug)

