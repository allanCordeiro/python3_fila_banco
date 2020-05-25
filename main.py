from atendimento import Atendimento
from relatorios import Relatorios
import os

def tela_principal():
    os.system('clear')
    print('*'*79)
    print(f'{"Bem-vindo ao sistema de gestão de filas":>55}'.upper())
    print('*'*79)
    while True:
        print('Digite sua opção correspondendo ao menu abaixo:')
        print(' 1. Para cliente')
        print(' 2. para caixa')
        print(' 3. para gestor')
        menu_principal = int(input(' Digite a opção desejada: '))
        if menu_principal == 1:
            tela_cliente()
        elif menu_principal == 2:
            tela_caixa()
        elif menu_principal == 3:
            tela_gerente()
        else:
            print('\n *** ATENÇÃO: A opção digitada é inválida.\n')

def tela_cliente():
    fila = Atendimento()
    os.system('clear')
    print('*' * 79)
    print(f'{"Módulo de clientes":>55}'.upper())
    print('*' * 79)
    while True:
        print('Digite sua opção correspondendo ao menu abaixo:')
        print(' 1. Puxar senha normal')
        print(' 2. Puxar senha cliente prioridade')
        print(' 3. Menu anterior')
        menu_principal = int(input(' Digite a opção desejada: '))
        if menu_principal == 1:
            atender_normal = fila.iniciar_atendimento('normal')
            senha = atender_normal.puxar_senha()
            printar_senha(senha)
            voltar = input('Digite qualquer tecla para voltar ao menu anterior')
            tela_cliente()
        elif menu_principal == 2:
            atender_prioridade = fila.iniciar_atendimento('prioritaria')
            senha = atender_prioridade.puxar_senha()
            printar_senha(senha)
            voltar = input('Digite qualquer tecla para voltar ao menu anterior')
            tela_cliente()
        elif menu_principal == 3:
            tela_principal()
        else:
            print('\n *** ATENÇÃO: A opção digitada é inválida.\n')

def printar_senha(senha:str) -> None:
    print('SUA SENHA DE ATENDIMENTO:')
    print('*' * 40)
    print(senha)
    print('*' * 40)

def tela_caixa():
    os.system('clear')
    print('*' * 79)
    print(f'{"Módulo de caixa":>55}'.upper())
    print('*' * 79)
    no_caixa = int(input('Digite o no do seu caixa: '))
    print('Digite sua opção correspondendo ao menu abaixo:')
    sub_menu_caixa(no_caixa)


def sub_menu_caixa(no_caixa: int):
    while True:
        print('\tDigite a opção correspondente:')
        print('\t1. Chamar a próxima senha')
        print('\t2. Chamar senha prioridade')
        print('\t3. Voltar ao menu anterior')
        sub_menu = int(input('\t Digite a opção desejada: '))
        if sub_menu == 1:
            chama_senha_normal(no_caixa)
            sub_menu_caixa(no_caixa)
        elif sub_menu == 2:
            chama_senha_prioritaria(no_caixa)
            sub_menu_caixa(no_caixa)
        elif sub_menu == 3:
            tela_principal()

def chama_senha_normal(no_caixa: int) -> None:
    fila = Atendimento()
    atender_normal = fila.iniciar_atendimento('normal')
    print('*' *30)
    print(f'{atender_normal.chamar_senha(no_caixa)}')
    print('*' *30)


def chama_senha_prioritaria(no_caixa: int) -> None:
    fila = Atendimento()
    atender_prioridade = fila.iniciar_atendimento('prioritaria')
    print('*' * 30)
    print(f'{atender_prioridade.chamar_senha(no_caixa)}')
    print('*' * 30)


def tela_gerente():
    os.system('clear')
    print('*' * 79)
    print(f'{"MÓDULO DE GERENTE":>55}'.upper())
    print('*' * 79)
    while True:
        print('Digite sua opção correspondendo ao menu abaixo:')
        print(' 1. Para gravar atendimento')
        print(' 2. para relatório simples')
        print(' 3. para relatório detalhado')
        menu_principal = int(input(' Digite a opção desejada: '))
        if menu_principal == 1:
            print(guardar_atendimento())
        elif menu_principal == 2:
            #tela_relatorio_simples()
            break
        elif menu_principal == 3:
            #tela_relatorio_detalhado()
            break
        else:
            print('\n *** ATENÇÃO: A opção digitada é inválida.\n')

def guardar_atendimento():
    limpar_fila = Atendimento.iniciar_atendimento()
    limpar_fila.limpar_fila()
    return f'Arquivo gerado com sucesso!'


if __name__ == "__main__":
    tela_principal()