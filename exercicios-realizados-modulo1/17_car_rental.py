dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
valor = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${}!'.format(valor))
