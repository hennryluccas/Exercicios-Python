'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''

cont = 0
maior1000 = 0
soma = 0
barato = 0
nome_barato = ' '
print('-'*30)
print('LOJA DO HENNRY')
print('-'*30)
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    if preço > 1000:
        maior1000 += 1
    soma += preço
    if cont == 1:
        barato = preço
        nome_barato = produto
    else:
        if preço < barato:
            barato = preço
            nome_barato = produto
    continuar = ' '
    while continuar not in 'SN':
        print('-'*30)
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-'*10, 'FIM DO PROGRAMA', '-'*10)
print(f'O total da compra foi R$ {soma:.2f}')
print(f'Temos {maior1000} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi o(a) {nome_barato} que custa R$ {barato}')
