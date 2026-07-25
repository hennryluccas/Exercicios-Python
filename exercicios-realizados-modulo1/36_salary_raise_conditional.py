'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu pagamento.
Para salários superiores a R$1.250,00 calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Informe o seu salário: R$ '))
if salario <= 1250:
    aumento = salario * 15/100
else:
    aumento = salario * 10/100

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, salario + aumento))
