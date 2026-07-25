"""
Crie um programa que leia um número inteiro
e mostre na tela se ele é PAR ou ÍMPAR
"""

numero = int(input('Digite um número qualquer: '))
if numero % 2 == 0:
    print('PAR')
else:
    print('IMPAR')

'''
A lógica matemática por trás disso (bem antiga, inclusive):
todo número par pode ser escrito como "2 × alguma coisa" (ex: 10 = 2×5).
Todo número ímpar é sempre "2 × alguma coisa, mais 1" (ex: 9 = 2×4 + 1).
É exatamente esse "+1 sobrando" que o % está capturando.

ATENÇÃO

10 ÷ 2 = 5    (quociente: quantas vezes 2 cabe em 10)
2 × 5 = 10    (confere: 2 vezes 5 dá exatamente 10)
resto = 10 - 10 = 0     ← não sobrou nada

7 ÷ 2 = 3     (quociente: 2 cabe 3 vezes em 7, sem passar)
2 × 3 = 6     (confere: 2 vezes 3 dá 6, não 7)
resto = 7 - 6 = 1     ← sobrou 1
'''