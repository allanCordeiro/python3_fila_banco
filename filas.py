from datetime import datetime, time
from constants import CODIGO_FILA_NORMAL, \
    CODIGO_FILA_PRIORITARIA, TAMANHO_FILA
import erros

class Fila:
    _codigo: int = 0
    _senha_gerada: dict = {}
    _fila_atual: list = []
    _fila_atendida: list = []

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
        self.registrar_atendido()
        return f'SENHA {proxima_senha["senha"]}\n' \
               f'CAIXA {caixa}'

    def registrar_atendido(self) -> None:
        senha_chamada = self._fila_atual[0]
        senha_chamada['hora_atendimento'] = datetime.now()

        self._fila_atendida.append(senha_chamada)
        self._fila_atual.pop(0)

    def tem_vaga_na_fila(self) -> bool:
        if TAMANHO_FILA >= self._codigo:
            return True
        else:
            return False

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
classe fila normal para clientes normais
classe fila prioritaria para clientes fila prioritaria
relatório simples e detalhado do dia salvos em txt
'''