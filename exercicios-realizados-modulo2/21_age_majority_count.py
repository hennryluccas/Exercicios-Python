'''
Crie um programa que leia o ano de nascimento de
sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.

21 anos
'''

from datetime import date
menores = 0
maiores = 0
for c in range(0,7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print('{} pessoas NÃO ATINGIRAM A MAIORIDADE!'.format(menores))
print('{} pessoas ATINGIRAM A MAIORIDADE!'.format(maiores))

