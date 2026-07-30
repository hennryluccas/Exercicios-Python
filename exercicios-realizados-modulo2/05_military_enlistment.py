'''
Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date
ano_nascimento = int(input('Escreva o ano de nascimento: '))
idade_servico_militar = 18
idade_usuario = date.today().year - ano_nascimento
falta_completar = idade_servico_militar - idade_usuario
ultrapassou_idade = idade_usuario - idade_servico_militar


if idade_usuario < idade_servico_militar:
    print('Você só vai se alistar quando completar 18 anos. Isso será daqui a {} anos, em {}. FIQUE ATENTO!'.format(falta_completar, date.today().year + falta_completar))
elif idade_usuario == idade_servico_militar:
    print('Está na hora de se alistar! Vá pessoalmente a uma Junta de Serviço Militar mais próxima.')
else:
    print('Já passou da hora de você se alistar! Já se passaram {} anos. Foi em {}.'.format(ultrapassou_idade, date.today().year - ultrapassou_idade))
