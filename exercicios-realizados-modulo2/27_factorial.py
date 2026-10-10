'''
Faça um programa que leia um número
qualquer e mostre o seu fatorial.

Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
'''

from math import factorial
num = int(input('Digite um número para calcularmos o fatorial: '))
c = num
print('{}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    c -= 1
print(factorial(num))
