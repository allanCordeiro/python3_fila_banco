from filas import Fila, FilaNormal, FilaPrioritaria


class Atendimento:

    @staticmethod
    def iniciar_atendimento(tipo_fila : str) -> Fila:
        if tipo_fila == 'normal':
            return FilaNormal()
        elif tipo_fila == 'prioritaria':
            return FilaPrioritaria()