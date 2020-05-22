from atendimento import Atendimento
import erros

'''
Por enquanto o main.py é uma zona de testes
para implementação das outras funcionalidades
'''
fila_normal = Atendimento.iniciar_atendimento('normal')
fila_prioritaria = Atendimento.iniciar_atendimento('prioritaria')

x = 0
while x < 10:
    print(fila_normal.puxar_senha())
    print(fila_prioritaria.puxar_senha())
    x += 1

print('******* FILA NORMAL ********')
print(fila_normal.chamar_senha(2))
segura_tempo = input('Input para ajudar a mensurar os tempos de espera')
print('***** FILA PRIORITARIA *****')
print(fila_prioritaria.chamar_senha(10))
segura_tempo = input('Input para ajudar a mensurar os tempos de espera')
print('******* FILA NORMAL ********')
print(fila_normal.chamar_senha(1))
segura_tempo = input('Input para ajudar a mensurar os tempos de espera')
print('***** FILA PRIORITARIA *****')
print(fila_prioritaria.chamar_senha(3))
segura_tempo = input('Input para ajudar a mensurar os tempos de espera')




atendidos = fila_normal.fila_atendida
for atendido in atendidos:
    print(atendido)