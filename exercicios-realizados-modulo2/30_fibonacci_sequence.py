'''
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci.

Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8
'''

print('-=' *20)
print('Sequência de Fibonacci')
print('-=' *20)

t1 = 0
t2 = 1
contador = 0

n = int(input('Quantos termos deseja mostrar? '))
while contador < n:
    print('{} → '.format(t1), end='')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    contador += 1
print('FIM')
