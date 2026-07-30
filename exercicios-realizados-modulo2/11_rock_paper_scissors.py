'''
Crie um programa que faça o computador jogar Jokenpô com você:
'''
from time import sleep
from random import randint
usuario = int(input('Escolha uma opção: \n[ 0 ] Pedra \n[ 1 ] Papel \n[ 2 ] Tesoura \nDigite aqui: '))
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0,2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)
print('-=' * 20)
print('Computador jogou {}'.format(lista[computador]))
print('Jogador jogou {}'.format(lista[usuario]))
if usuario == 0 and computador == 1:
    print('Você PERDEU!')
elif usuario == 0 and computador == 2:
    print('Você GANHOU!')
elif usuario == 1 and computador == 0:
    print('Você GANHOU!')
elif usuario == 1 and computador == 2:
    print('Você PERDEU!')
elif usuario == 2 and computador == 0:
    print('Você PERDEU!')
elif usuario == 2 and computador == 1:
    print('Você GANHOU!')
else:
    print('Empatou!')
print('-=' * 20)