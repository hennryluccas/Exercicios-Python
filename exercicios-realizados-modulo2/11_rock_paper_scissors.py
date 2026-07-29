'''
Crie um programa que faça o computador jogar Jokenpô com você:
'''

from random import randint
usuario = int(input('Escolha uma opção: \n1 - Pedra \n2 - Papel \n3 - Tesoura \nDigite aqui: '))
lista = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0,2)
print('Eu escolho {}'.format(lista[computador]))

if usuario == 1 and computador == 1:
    print('Você PERDEU!')
elif usuario == 1 and computador == 2:
    print('Você GANHOU!')
elif usuario == 2 and computador == 0:
    print('Você GANHOU!')
elif usuario == 2 and computador == 2:
    print('Você PERDEU!')
elif usuario == 3 and computador == 0:
    print('Você PERDEU!')
elif usuario == 3 and computador == 1:
    print('Você GANHOU!')
else:
    print('Empatou!')
