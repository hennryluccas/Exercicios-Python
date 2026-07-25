'''
Faça um programa que leia um ano qualquer
e mostre se ele é BISSEXTO.
'''

from datetime import date
ano = int(input('Que ano quer analisar: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))

'''
==   # igual a
!=   # diferente de
>    # maior que
<    # menor que
>=   # maior ou igual a
<=   # menor ou igual a

Caminho 1: divisível por 4 E não divisível por 100

Exemplo: 2024 (divisível por 4, não divisível por 100) → bissexto ✅

-------------------------------------------------------------------------------------------------------------

Caminho 2: divisível por 400 (não importa se é divisível por 100 ou não)

Exemplo: 2000 (divisível por 4, divisível por 100, mas também divisível por 400) → bissexto ✅

-------------------------------------------------------------------------------------------------------------
Ano	  |  Div. por 4?  |	 Div. por 100? 	 |   Div. por 400?	 |   Bissexto?
2024  |  Sim	      |  Não	         |   Não	         |   Sim (caminho 1)
1900  |  Sim	      |  Sim	         |   Não	         |   Não (nenhum caminho bate)
2000  |  Sim	      |  Sim	         |   Sim	         |   Sim (caminho 2, porque é divisível por 400)
'''