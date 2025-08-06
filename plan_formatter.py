"""
Plan Formatter - Módulo para formatação de planos nutricionais
Padrão Pedro Barros - Versão Otimizada com Gestão de 8.000 Caracteres
"""

from typing import Dict, List, Tuple, Optional

class PlanFormatter:
    """Formatador de planos seguindo o Padrão Pedro Barros com precisão absoluta"""
    
    # Constantes de formatação (Padrão Pedro Barros)
    LIMITE_CARACTERES = 7500  # Margem de segurança para 8.000
    ESPACOS_CABECALHO = 59
    COLUNA_CALORIAS = 120
    BULLET = "•"
    
    def __init__(self):
        self.contador_caracteres = 0
    
    def _reset_contador(self):
        """Reseta o contador de caracteres"""
        self.contador_caracteres = 0
    
    def _adicionar_linha(self, linha: str) -> str:
        """Adiciona uma linha e atualiza o contador"""
        self.contador_caracteres += len(linha) + 1  # +1 para \n
        return linha + "\n"
    
    def _criar_cabecalho(self, paciente: Dict, data: str) -> str:
        """Cria o cabeçalho com 59 espaços exatos"""
        linhas = []
        
        # Espaços iniciais
        linhas.append(" " * self.ESPACOS_CABECALHO)
        linhas.append("")
        linhas.append("")
        
        # Título centralizado
        titulo = "Plano Alimentar"
        espacos_titulo = " " * ((self.ESPACOS_CABECALHO - len(titulo)) // 2)
        linhas.append(espacos_titulo + titulo)
        
        # Nome centralizado
        nome = paciente["nome"]
        espacos_nome = " " * ((self.ESPACOS_CABECALHO - len(nome)) // 2)
        linhas.append(espacos_nome + nome)
        
        # Data centralizada
        data_formatada = f"Data: {data}"
        espacos_data = " " * ((self.ESPACOS_CABECALHO - len(data_formatada)) // 2)
        linhas.append(espacos_data + data_formatada)
        
        # Espaços finais
        linhas.append("")
        linhas.append("")
        linhas.append("")
        
        return "\n".join(linhas) + "\n"
    
    def _criar_tipo_dieta(self) -> str:
        """Cria a seção de tipo de dieta"""
        return "Todos os dias\nDieta única\n\n"
    
    def _formatar_refeicao(self, refeicao: Dict) -> str:
        """Formata uma refeição seguindo o padrão exato"""
        linhas = []
        
        # Cabeçalho da refeição com calorias alinhadas
        nome_horario = f"  {refeicao['horario']} - {refeicao['nome']}"
        kcal_texto = f"{refeicao['totais']['kcal']:.2f} Kcal"
        
        # Calcula espaços para alinhar na coluna 120
        espacos_necessarios = self.COLUNA_CALORIAS - len(nome_horario) - len(kcal_texto)
        if espacos_necessarios < 1:
            espacos_necessarios = 1
        
        linha_refeicao = nome_horario + " " * espacos_necessarios + kcal_texto
        linhas.append(linha_refeicao)
        
        # Itens da refeição
        for item in refeicao["itens"]:
            nome_item = f"{item['nome']} ({item['unidade']}: {item['quantidade']})"
            kcal_item = f"{item['kcal']:.2f} kcal"
            
            # Alinha as calorias do item
            espacos_item = self.COLUNA_CALORIAS - len(f"{self.BULLET}   {nome_item}") - len(kcal_item)
            if espacos_item < 1:
                espacos_item = 1
            
            linha_item = f"{self.BULLET}   {nome_item}" + " " * espacos_item + kcal_item
            linhas.append(linha_item)
        
        linhas.append("")  # Linha em branco após cada refeição
        return "\n".join(linhas) + "\n"
    
    def _criar_substituicoes_lanche(self, substituicoes: List[Dict]) -> str:
        """Cria a seção de substituições do lanche"""
        linhas = []
        linhas.append("Substituições para o lanche da tarde:")
        linhas.append("")
        
        for sub in substituicoes:
            # Título da substituição
            linhas.append(f"Substituição {sub['numero']}: {sub['nome']}")
            
            # Ingredientes
            ingredientes_texto = ", ".join(sub['ingredientes'])
            linhas.append(f"{self.BULLET}   {ingredientes_texto}")
            
            # Observação
            if sub.get('observacao'):
                linhas.append(f"    Obs: {sub['observacao']}")
            
            linhas.append("")
        
        return "\n".join(linhas) + "\n"
    
    def _criar_receitas_jantar(self, receitas: List[Dict]) -> str:
        """Cria a seção de receitas especiais do jantar"""
        linhas = []
        linhas.append("Receitas especiais para o jantar:")
        linhas.append("")
        
        for receita in receitas:
            # Nome da receita
            linhas.append(f"{self.BULLET}   {receita['nome']}")
            
            # Ingredientes
            ingredientes_texto = ", ".join(receita['ingredientes'])
            linhas.append(f"    Ingredientes: {ingredientes_texto}")
            
            # Preparo
            if receita.get('preparo'):
                linhas.append(f"    Preparo: {receita['preparo']}")
            
            linhas.append("")
        
        return "\n".join(linhas) + "\n"
    
    def _criar_resumo_nutricional(self, resumo: Dict) -> str:
        """Cria o resumo nutricional obrigatório"""
        linhas = []
        linhas.append("RESUMO NUTRICIONAL:")
        linhas.append("")
        
        for nutriente, dados in resumo.items():
            nome_nutriente = nutriente.capitalize()
            if nutriente == "kcal":
                valor_texto = f"{dados['valor']:.2f}"
                percentual_texto = f"({dados['percentual']:.1f}% da meta)"
                linha_completa = f"{self.BULLET}   {nome_nutriente}: {valor_texto} {percentual_texto}"
            else:
                valor_texto = f"{dados['valor']:.2f}g"
                percentual_texto = f"({dados['percentual']:.1f}% da meta)"
                linha_completa = f"{self.BULLET}   {nome_nutriente}: {valor_texto} {percentual_texto}"
            
            linhas.append(linha_completa)
        
        linhas.append("")
        return "\n".join(linhas) + "\n"
    
    def _criar_rodape(self) -> str:
        """Cria o rodapé de confidencialidade"""
        return "\n---\nEste plano alimentar é confidencial e personalizado. Não compartilhe sem autorização.\n"
    
    def verificar_tamanho_plano(self, plano: Dict) -> Dict:
        """Verifica se o plano formatado excede o limite de caracteres"""
        # Calcula tamanho do plano essencial (sem substituições e receitas)
        plano_essencial = self.formatar_plano_essencial(plano)
        tamanho_essencial = len(plano_essencial)
        
        # Calcula tamanho do plano completo
        plano_completo = self.formatar_plano_completo(plano)
        tamanho_completo = len(plano_completo)
        
        # Verifica se o plano completo cabe no limite
        if tamanho_completo <= self.LIMITE_CARACTERES:
            return {
                "status": "completo",
                "tamanho": tamanho_completo,
                "precisa_dividir": False
            }
        
        # Se não cabe, verifica se pelo menos o essencial cabe
        if tamanho_essencial <= self.LIMITE_CARACTERES:
            return {
                "status": "dividido",
                "tamanho": tamanho_essencial,
                "precisa_dividir": True,
                "tamanho_essencial": tamanho_essencial
            }
        
        # Se nem o essencial cabe, precisa de uma versão ainda mais compacta
        return {
            "status": "erro",
            "tamanho": tamanho_essencial,
            "precisa_dividir": True,
            "tamanho_essencial": tamanho_essencial,
            "erro": "Plano essencial excede limite de caracteres"
        }
    
    def formatar_plano_essencial(self, plano: Dict) -> str:
        """Formata apenas o plano essencial (sem substituições e receitas)"""
        self._reset_contador()
        partes = []
        
        # Cabeçalho
        partes.append(self._criar_cabecalho(plano["paciente"], plano["data"]))
        
        # Tipo de dieta
        partes.append(self._criar_tipo_dieta())
        
        # Refeições
        for refeicao in plano["refeicoes"]:
            partes.append(self._formatar_refeicao(refeicao))
        
        # Resumo nutricional
        partes.append(self._criar_resumo_nutricional(plano["resumo_nutricional"]))
        
        # Aviso de continuação
        aviso = "\n[SISTEMA: Plano completo disponível. Digite 'continuar' para ver substituições e receitas.]\n"
        partes.append(aviso)
        
        return "".join(partes)
    
    def formatar_continuacao(self, plano: Dict) -> str:
        """Formata a continuação do plano (substituições e receitas)"""
        partes = []
        
        # Substituições
        partes.append(self._criar_substituicoes_lanche(plano["substituicoes_lanche"]))
        
        # Receitas
        partes.append(self._criar_receitas_jantar(plano["receitas_jantar"]))
        
        # Rodapé
        partes.append(self._criar_rodape())
        
        return "".join(partes)
    
    def formatar_plano_completo(self, plano: Dict) -> str:
        """Formata o plano completo (quando cabe no limite)"""
        self._reset_contador()
        partes = []
        
        # Cabeçalho
        partes.append(self._criar_cabecalho(plano["paciente"], plano["data"]))
        
        # Tipo de dieta
        partes.append(self._criar_tipo_dieta())
        
        # Refeições
        for refeicao in plano["refeicoes"]:
            partes.append(self._formatar_refeicao(refeicao))
        
        # Resumo nutricional
        partes.append(self._criar_resumo_nutricional(plano["resumo_nutricional"]))
        
        # Substituições
        partes.append(self._criar_substituicoes_lanche(plano["substituicoes_lanche"]))
        
        # Receitas
        partes.append(self._criar_receitas_jantar(plano["receitas_jantar"]))
        
        # Rodapé
        partes.append(self._criar_rodape())
        
        return "".join(partes)
    
    def processar_plano(self, plano: Dict) -> Dict:
        """Processa o plano e retorna a resposta formatada adequada"""
        verificacao = self.verificar_tamanho_plano(plano)
        
        if verificacao["status"] == "erro":
            return {
                "status": "erro",
                "plano_formatado": "ERRO: Plano muito longo para ser exibido",
                "continuacao_disponivel": False,
                "erro": verificacao["erro"],
                "tamanho_essencial": verificacao["tamanho_essencial"],
                "mensagem": "Plano excede limite mesmo na versão essencial"
            }
        elif verificacao["precisa_dividir"]:
            return {
                "status": "dividido",
                "plano_formatado": self.formatar_plano_essencial(plano),
                "continuacao_disponivel": True,
                "continuacao": self.formatar_continuacao(plano),
                "tamanho_essencial": verificacao["tamanho_essencial"],
                "mensagem": "Plano dividido devido ao limite de caracteres"
            }
        else:
            return {
                "status": "completo",
                "plano_formatado": self.formatar_plano_completo(plano),
                "continuacao_disponivel": False,
                "tamanho_total": verificacao["tamanho"],
                "mensagem": "Plano completo formatado com sucesso"
            }

