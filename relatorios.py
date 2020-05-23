import humanize
humanize.i18n.activate("pt_BR")

from datetime import datetime
from typing import List
from constants import CODIGO_FILA_PRIORITARIA, CODIGO_FILA_NORMAL

class Relatorios:

    _dados_relatorio_simples: dict = {}

    def relatorio_simples(self, data_relatorio: str) -> dict:

        relatorio = self._ler_arquivo(data_relatorio)
        quantidade_atendimentos = self._retorna_quantidade_de_atendimentos(
            relatorio)
        contagem_caixa = self._retorna_atendimento_caixa(relatorio)
        qte_normal = self._quantidade_fila_normal(relatorio)
        qte_prioritario = self._quantidade_prioritarios(relatorio)

        self._dados_relatorio_simples['qte_atendimento'] = \
            quantidade_atendimentos
        self._dados_relatorio_simples['por_caixa'] = contagem_caixa
        self._dados_relatorio_simples['qte_normal'] = qte_normal
        self._dados_relatorio_simples['qte_prioritario'] = qte_prioritario

        return self._dados_relatorio_simples

    def _retorna_quantidade_de_atendimentos(self, lista: list) -> int:
        return len(lista)

    def _retorna_atendimento_caixa(self, lista: list) -> dict:
        lista_caixas: dict = {}
        for caixa in lista:
            no_caixa = lista_caixas.get(caixa['caixa'], 0)
            lista_caixas[caixa['caixa']] = no_caixa + 1

        return lista_caixas

    def _quantidade_fila_normal(self, lista: list) -> int:
        contador: int = 0
        for senha in lista:
            if senha['senha'][0:2] == CODIGO_FILA_NORMAL:
                contador += 1

        return contador

    def _quantidade_prioritarios(self, lista: list) -> int:
        contador: int = 0
        for senha in lista:
            if senha['senha'][0:2] == CODIGO_FILA_PRIORITARIA:
                contador += 1

        return contador


    def relatorio_detalhado(self):
            ...

    @staticmethod
    def gerar_arquivo(senhas: List) -> None:
        nome_arquivo = f'relatorios/fila_cliente_' \
                       f'{datetime.now().strftime("%d-%m-%Y")}.txt'
        hora_atual = datetime.now().strftime("%d/%m/%Y %T")
        with open(nome_arquivo, 'a') as arquivo:
            for senha in senhas:
                delta = humanize.naturaldelta(senha["tempo_fila"],
                                              minimum_unit="seconds")
                arquivo.write(
                    f'{senha["senha"]}\t'
                    f'{senha["caixa"]}\t'
                    f'{senha["hora_geracao"].strftime("%d/%m/%Y %T")}\t'
                    f'{senha["hora_atendimento"].strftime("%d/%m/%Y %T")}\t'
                    f'{delta}\n'
                )

    def _ler_arquivo(self, nome_arquivo : str) -> List:
        nome_arquivo = f'relatorios/fila_cliente_{nome_arquivo}.txt'
        lista: List = []
        registro: dict = {}

        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                linha_quebrada = linha.split('\t')
                registro["senha"] = linha_quebrada[0]
                registro["caixa"] = linha_quebrada[1]
                registro["hora_geracao"] = linha_quebrada[2]
                registro["hora_atendimento"] = linha_quebrada[3]
                registro["tempo_atendimento"] = linha_quebrada[4]
                lista.append(registro.copy())

        return lista