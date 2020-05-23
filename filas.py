from datetime import datetime, time, timedelta
from constants import CODIGO_FILA_NORMAL, \
    CODIGO_FILA_PRIORITARIA, TAMANHO_FILA
from relatorios import Relatorios
import erros

class Fila:
    _codigo: int = 0
    _senha_gerada: dict = {}
    _fila_atual: list = []
    _fila_atendida: list = []

    @property
    def fila_atendida(self):
        return self._fila_atendida

    def gerar_senha(self) -> None:
        if self.tem_vaga_na_fila():
            self._codigo += 1
            self._senha_gerada['senha'] = f'{self._codigo}'
            self._senha_gerada['hora_geracao'] = datetime.now()
        else:
            raise erros.CapacidadeMaxima(
                'A agência atingiu o limite de atendimentos no momento.')

    def puxar_senha(self) -> str:
        self.gerar_senha()
        self._fila_atual.append(self._senha_gerada.copy())
        hora_formatada: str = self._senha_gerada["hora_geracao"].strftime(
            '%d/%m/%Y %T'
        )
        return f'Senha gerada: {self._senha_gerada["senha"]}' \
               f' | Hora geração: {hora_formatada}'

    def chamar_senha(self, caixa: int) -> str:
        proxima_senha = self._fila_atual[0]
        self.registrar_atendido(caixa)
        return f'SENHA {proxima_senha["senha"]}\n' \
               f'CAIXA {caixa}'

    def registrar_atendido(self, caixa: int) -> None:
        senha_chamada = self._fila_atual[0]
        senha_chamada['hora_atendimento'] = datetime.now()
        senha_chamada['caixa'] = caixa
        delta = senha_chamada['hora_atendimento'] \
                - senha_chamada['hora_geracao']
        senha_chamada['tempo_fila'] = delta

        self._fila_atendida.append(senha_chamada)
        self._fila_atual.pop(0)

    def tem_vaga_na_fila(self) -> bool:
        if TAMANHO_FILA > len(self._fila_atual):
            return True
        else:
            return False

    def limpar_fila(self) -> None:
        Relatorios.gerar_arquivo(self._fila_atendida)
        self._fila_atendida.clear()

class FilaNormal(Fila):
    def gerar_senha(self) -> None:
        if self.tem_vaga_na_fila():
            Fila._codigo += 1
            self._senha_gerada['senha'] = f'{CODIGO_FILA_NORMAL}' \
                                          f'{self._codigo}'
            self._senha_gerada['hora_geracao'] = datetime.now()

        else:
            raise erros.CapacidadeMaxima(
                'A agência atingiu o limite de atendimentos no momento.')

class FilaPrioritaria(Fila):
    def gerar_senha(self) -> None:
        if self.tem_vaga_na_fila():
            Fila._codigo += 1
            self._senha_gerada['senha'] = f'{CODIGO_FILA_PRIORITARIA}' \
                                          f'{self._codigo}'
            self._senha_gerada['hora_geracao'] = datetime.now()
        else:
            raise erros.CapacidadeMaxima(
                'A agência atingiu o limite de atendimentos no momento.')

'''
relatório simples e detalhado do dia salvos em txt
'''