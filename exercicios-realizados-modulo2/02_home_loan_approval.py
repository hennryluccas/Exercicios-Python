'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
do salário ou então o empréstimo será negado.
'''

valor_da_casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Quanto é o seu salário? R$ '))
tempo = int(input('Em quantos anos deseja pagar? '))

parte_do_salario = salario * 30/100
prestacao = valor_da_casa / (tempo * 12)


if prestacao > parte_do_salario:
    print('Você NÃO PODE financiar essa casa. A prestação (R${:.2f}) excede o limite de R${:.2f} (30% do seu salário).'.format(prestacao, parte_do_salario))
else:
    print('Você foi APROVADO para financiar essa casa, o valor a pagar todos os meses será de R$ {:.2f}'.format(prestacao))
