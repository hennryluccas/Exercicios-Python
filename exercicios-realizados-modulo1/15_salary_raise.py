v = float(input('Qual é o valor do seu salário atual?: R$'))
sa = v + (v * 15/100)
print('Com um aumento de 15%, seu novo salário será de: R${:.2f}'.format(sa))