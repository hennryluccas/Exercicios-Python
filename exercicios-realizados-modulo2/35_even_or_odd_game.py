'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele
conquistou no final do jogo.
'''

from random import randint
print('-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('-'*30)
cont = 0
while True:
    num = int(input('Diga o valor: '))
    escolha_usuario = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    computador = randint(0, 10)
    soma = num + computador
    if escolha_usuario == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {num} e o computador {computador}. Total de {soma} DEU PAR')
            print('-' * 30)
            print('Você GANHOU!')
            print('Vamos jogar novamente?')
            cont += 1
        else:
            print(f'Você jogou {num} e o computador {computador}. Total de {soma} DEU ÍMPAR')
            print('-' * 30)
            print('Você PERDEU!')
            break
    elif escolha_usuario == 'I':
        if soma % 2 == 0:
            print(f'Você jogou {num} e o computador {computador}. Total de {soma} DEU PAR')
            print('-' * 30)
            print('Você PERDEU!')
            break
        else:
            print(f'Você jogou {num} e o computador {computador}. Total de {soma} DEU ÍMPAR')
            print('-' * 30)
            print('Você GANHOU!')
            print('Vamos jogar novamente?')
            cont += 1
    else:
        print('Opção inválida! Escolha apenas P ou I.')
print(f'GAME OVER, você ganhou {cont} vezes')

# Como o professor fez:
'''
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print(' DEU PAR' if total % 2 == 0 else ' DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v = v + 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v = v + 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente?')
print(f'GAME OVER! Você ganhou {v} vezes.')
'''
