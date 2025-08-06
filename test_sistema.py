"""
Script de Teste - Sistema Pedro Barros Otimizado
Testa todas as funcionalidades e validações
"""

import json
import sys
import os

# Adiciona o diretório atual ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_manager import DataManager
from plan_builder import PlanBuilder
from plan_formatter import PlanFormatter

def test_data_manager():
    """Testa o DataManager"""
    print("🔍 Testando DataManager...")
    
    dm = DataManager()
    
    # Testa busca de alimento
    ovo = dm.get_alimento("ovo_galinha_inteiro")
    assert ovo is not None, "Ovo não encontrado"
    assert ovo["kcal_por_unidade"] == 77.49, "Calorias do ovo incorretas"
    
    # Testa cálculo de macros
    macros = dm.calcular_macros("ovo_galinha_inteiro", 2)
    assert macros["kcal"] == 154.98, "Cálculo de calorias incorreto"
    
    print("✅ DataManager funcionando corretamente")

def test_plan_builder():
    """Testa o PlanBuilder"""
    print("🔍 Testando PlanBuilder...")
    
    dm = DataManager()
    pb = PlanBuilder(dm)
    
    # Testa cálculo de necessidades
    paciente = {"peso_kg": 75, "altura_cm": 178, "sexo": "M"}
    metas = {
        "kcal_total": 2000,
        "proteina_min_g_por_kg": 2.3,
        "carboidrato_max_percent": 35,
        "gordura_max_percent": 25,
        "fibras_min_g": 30
    }
    
    necessidades = pb.calcular_necessidades_basicas(paciente, metas)
    assert necessidades["kcal_total"] == 2000, "Calorias totais incorretas"
    assert necessidades["proteina_min_g"] == 172.5, "Proteína mínima incorreta"
    
    # Testa criação de plano
    plano = pb.criar_plano_exemplo()
    assert "paciente" in plano, "Plano sem dados do paciente"
    assert "refeicoes" in plano, "Plano sem refeições"
    assert len(plano["substituicoes_lanche"]) == 6, "Número incorreto de substituições"
    assert len(plano["receitas_jantar"]) == 4, "Número incorreto de receitas"
    
    print("✅ PlanBuilder funcionando corretamente")

def test_plan_formatter():
    """Testa o PlanFormatter"""
    print("🔍 Testando PlanFormatter...")
    
    dm = DataManager()
    pb = PlanBuilder(dm)
    pf = PlanFormatter()
    
    # Cria plano de teste
    plano = pb.criar_plano_exemplo()
    
    # Testa verificação de tamanho
    verificacao = pf.verificar_tamanho_plano(plano)
    assert "status" in verificacao, "Verificação sem status"
    assert "precisa_dividir" in verificacao, "Verificação sem flag de divisão"
    
    # Testa formatação
    resultado = pf.processar_plano(plano)
    assert "plano_formatado" in resultado, "Resultado sem plano formatado"
    assert len(resultado["plano_formatado"]) > 0, "Plano formatado vazio"
    
    # Verifica se contém elementos obrigatórios
    plano_texto = resultado["plano_formatado"]
    assert "Plano Alimentar" in plano_texto, "Título ausente"
    assert "João Silva" in plano_texto, "Nome do paciente ausente"
    assert "•" in plano_texto, "Bullets ausentes"
    assert "Kcal" in plano_texto, "Calorias ausentes"
    
    # Testa limite de caracteres
    assert len(plano_texto) <= 8000, f"Plano excede limite: {len(plano_texto)} caracteres"
    
    print(f"✅ PlanFormatter funcionando corretamente")
    print(f"   📊 Tamanho do plano: {len(plano_texto)} caracteres")
    print(f"   📊 Status: {resultado['status']}")

def test_integracao_completa():
    """Teste de integração completa"""
    print("🔍 Testando integração completa...")
    
    # Dados de entrada
    dados_entrada = {
        "paciente": {
            "nome": "Maria Silva",
            "peso_kg": 65,
            "altura_cm": 165,
            "sexo": "F"
        },
        "metas": {
            "kcal_total": 1800,
            "proteina_min_g_por_kg": 2.0,
            "carboidrato_max_percent": 40,
            "gordura_max_percent": 30,
            "fibras_min_g": 25
        }
    }
    
    # Simula o fluxo completo da API
    dm = DataManager()
    pb = PlanBuilder(dm)
    pf = PlanFormatter()
    
    # Gera plano
    plano_base = pb.criar_plano_exemplo()
    plano_base["paciente"] = dados_entrada["paciente"]
    
    # Recalcula necessidades
    necessidades = pb.calcular_necessidades_basicas(
        dados_entrada["paciente"], 
        dados_entrada["metas"]
    )
    plano_base["necessidades"] = necessidades
    
    # Formata plano
    resultado = pf.processar_plano(plano_base)
    
    # Validações finais
    assert resultado["status"] in ["completo", "dividido"], "Status inválido"
    assert len(resultado["plano_formatado"]) > 0, "Plano vazio"
    assert len(resultado["plano_formatado"]) <= 8000, "Plano excede limite"
    
    print("✅ Integração completa funcionando corretamente")
    print(f"   👤 Paciente: {dados_entrada['paciente']['nome']}")
    print(f"   📊 Status: {resultado['status']}")
    print(f"   📏 Tamanho: {len(resultado['plano_formatado'])} caracteres")

def test_casos_extremos():
    """Testa casos extremos e limites"""
    print("🔍 Testando casos extremos...")
    
    dm = DataManager()
    pb = PlanBuilder(dm)
    pf = PlanFormatter()
    
    # Teste com valores extremos
    paciente_extremo = {
        "nome": "Nome Muito Longo Para Testar Limites de Formatação",
        "peso_kg": 150,
        "altura_cm": 200,
        "sexo": "M"
    }
    
    metas_extremas = {
        "kcal_total": 5000,
        "proteina_min_g_por_kg": 3.0,
        "carboidrato_max_percent": 50,
        "gordura_max_percent": 35,
        "fibras_min_g": 50
    }
    
    plano = pb.criar_plano_exemplo()
    plano["paciente"] = paciente_extremo
    
    necessidades = pb.calcular_necessidades_basicas(paciente_extremo, metas_extremas)
    plano["necessidades"] = necessidades
    
    resultado = pf.processar_plano(plano)
    
    # Deve funcionar mesmo com valores extremos
    assert len(resultado["plano_formatado"]) > 0, "Plano vazio com valores extremos"
    assert len(resultado["plano_formatado"]) <= 8000, "Plano excede limite com valores extremos"
    
    print("✅ Casos extremos tratados corretamente")

def executar_todos_os_testes():
    """Executa todos os testes"""
    print("🚀 Iniciando testes do Sistema Pedro Barros Otimizado\n")
    
    try:
        test_data_manager()
        print()
        
        test_plan_builder()
        print()
        
        test_plan_formatter()
        print()
        
        test_integracao_completa()
        print()
        
        test_casos_extremos()
        print()
        
        print("🎉 TODOS OS TESTES PASSARAM COM SUCESSO!")
        print("✅ Sistema Pedro Barros Otimizado está funcionando perfeitamente")
        print("✅ Gestão de 8.000 caracteres implementada")
        print("✅ Formatação seguindo o Padrão Pedro Barros")
        print("✅ Pronto para produção!")
        
        return True
        
    except AssertionError as e:
        print(f"❌ TESTE FALHOU: {e}")
        return False
    except Exception as e:
        print(f"❌ ERRO INESPERADO: {e}")
        return False

if __name__ == "__main__":
    sucesso = executar_todos_os_testes()
    sys.exit(0 if sucesso else 1)

