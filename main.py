from atendimento import Atendimento
from relatorios import Relatorios


'''
Por enquanto o main.py é uma zona de testes
para implementação das outras funcionalidades
'''

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
#segura_tempo = input('Input para ajudar a mensurar os tempos de espera')
print('******* FILA NORMAL ********')
print(fila_normal.chamar_senha(1))
#segura_tempo = input('Input para ajudar a mensurar os tempos de espera')
print('***** FILA PRIORITARIA *****')
print(fila_prioritaria.chamar_senha(3))
#segura_tempo = input('Input para ajudar a mensurar os tempos de espera')


fila_normal.limpar_fila()
'''

relatorios = Relatorios()

for relatorio, valor in relatorios.relatorio_simples('22-05-2020').items():
    print(relatorio, valor)

print('*********** RELATORIO COMPLETO ***********')
for dados in relatorios.relatorio_detalhado('22-05-2020'):
    print(dados)