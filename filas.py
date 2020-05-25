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
        return f' * SENHA GERADA: {self._senha_gerada["senha"]}\n' \
               f' * HORA GERACAO: {hora_formatada}'

    def chamar_senha(self, caixa: int) -> str:
        try:
            proxima_senha = self._fila_atual[0]
            self.registrar_atendido(caixa)
            return f'SENHA {proxima_senha["senha"]}\n' \
                   f'CAIXA {caixa}'
        except IndexError:
            return 'Não há clientes na fila.'

    def registrar_atendido(self, caixa: int, indice:int = 0) -> None:
        senha_chamada = self._fila_atual[indice]
        senha_chamada['hora_atendimento'] = datetime.now()
        senha_chamada['caixa'] = caixa
        delta = senha_chamada['hora_atendimento'] \
                - senha_chamada['hora_geracao']
        senha_chamada['tempo_fila'] = delta

        self._fila_atendida.append(senha_chamada)
        self._fila_atual.pop(indice)

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

    def chamar_senha(self, caixa: int) -> str:
        try:
            indice = self._proximo_preferencial()
            proxima_senha = self._fila_atual[indice]
            self.registrar_atendido(caixa, indice)
            return f'SENHA {proxima_senha["senha"]}\n' \
                   f'CAIXA {caixa}'
        except IndexError:
            return 'Não há clientes na fila.'

    def _proximo_preferencial(self) -> int:
        indice: int = 0
        flag: bool = False
        for fila in self._fila_atual:
            if fila["senha"][0:2] == CODIGO_FILA_PRIORITARIA:
                flag = True
            if flag:
                break
            indice += 1
        return indice
