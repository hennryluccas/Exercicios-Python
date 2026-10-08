'''
Melhore o jogo do DESAFIO 30 do Mundo 1 onde o
computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
'''

# Como eu fiz:

from random import randint
computador = randint(0,10)
usuario = -1
tentativas = 0

print('----JOGO DA ADIVINHAÇÃO----')
while usuario != computador:
    usuario = int(input('Digite o número que o computador está pensando: '))
    tentativas += 1
print('PARABÉNS! VOCÊ GANHOU!')
print('Foram necessárias {} tentativas'.format(tentativas))

# Como o professor fez:

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
