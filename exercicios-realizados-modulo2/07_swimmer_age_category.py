'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: Sênior
- Acima: Master
'''

from datetime import date
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano_nascimento

if idade <= 9:
    print('Idade {} - Atleta MIRIM.'.format(idade))
elif idade <= 14:
    print('Idade {} - Atleta INFANTIL.'.format(idade))
elif idade <= 19:
    print('Idade {} - Atleta JUNIOR.'.format(idade))
elif idade <= 20:
    print('Idade {} - Atleta SÊNIOR.'.format(idade))
else:
    print('Idade {} - Atleta MASTER.'.format(idade))
