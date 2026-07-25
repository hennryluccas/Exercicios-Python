'''
Escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador pensar
usuario = int(input('Em um número entre 0 e 5, qual o computador pensou? ')) #O usuário tenta adivinhar
print('PROCESSANDO...')
sleep(1) # Faz o computador parar 1 segundo
if usuario == computador:
    print('Parabéns, você acertou!')
else:
    print('Você perdeu! O computador pensou no número {}'.format(computador))

