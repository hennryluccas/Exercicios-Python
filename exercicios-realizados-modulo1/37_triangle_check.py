'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
ou não formar um triângulo.
'''

lado1 = int(input('Digite o primeiro lado: '))
lado2 = int(input('Digite o segundo lado: '))
lado3 = int(input('Digite o terceiro lado: '))

if lado1 > lado2 and lado1 > lado3:
    maior = lado1
if lado2 > lado1 and lado2 > lado3:
    maior = lado2
if lado3 > lado1 and lado3 > lado2:
    maior = lado3

soma_total = lado1 + lado2 + lado3
soma_dois_menores = soma_total - maior
if soma_dois_menores > maior:
    print('PODE formar um triângulo')
else:
    print('NÃO PODE formar um triângulo')
