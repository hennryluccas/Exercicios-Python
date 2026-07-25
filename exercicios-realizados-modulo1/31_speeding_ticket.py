'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem
dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidade = int(input('Qual a velocidade do carro? '))
limite = 80
if velocidade > limite:
    multa = (velocidade - limite) * 7
    print('VOCÊ FOI MULTADO! O valor permitido é 80Km/h \nO valor a pagar é de R${}'.format(multa))
else:
    print('Você está no limite da via! Tenha uma boa viagem!')
