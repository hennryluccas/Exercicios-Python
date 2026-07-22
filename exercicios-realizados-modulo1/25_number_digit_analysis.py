'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
'''

num = int(input('Informe um número'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

'''
Como funciona essa lógica (usando 1234 como exemplo):
Unidade:  1234 // 1    = 1234   →  1234 % 10 = 4
Dezena:   1234 // 10   = 123    →   123 % 10 = 3
Centena:  1234 // 100  = 12     →    12 % 10 = 2
Milhar:   1234 // 1000 = 1      →     1 % 10 = 1
'''