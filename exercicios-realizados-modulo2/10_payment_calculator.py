'''
Elabore um programa que calcule o valor
a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:

- À vista dinheiro/pix: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

produto = float(input('Digite o valor do produto: R$ '))
pagamento = int(input('Qual será a forma de pagamento: \n1 - À vista dinheiro/pix \n2 - À vista no cartão \n3 - Em até 2x no cartão \n4 - 3x ou mais no cartão \nDigite a opção escolhida: '))
a_vista_pix = produto - (produto * 10/100)
a_vista_cartao = produto - (produto * 5/100)
duas_vezes_cartao = produto / 2

if pagamento == 1:
    print('Valor sem desconto R${:.2f} - VALOR COM DESCONTO R${:.2f} (10% DE DESCONTO)'.format(produto, a_vista_pix))
elif pagamento == 2:
    print('Valor sem desconto R${:.2f} - VALOR COM DESCONTO R${:.2f} (5% DE DESCONTO)'.format(produto, a_vista_cartao))
elif pagamento == 3:
    print('Você pagará 2x de R${:.2f}'.format(duas_vezes_cartao))
elif pagamento == 4:
    quantas_vezes = int(input('Em quantas vezes deseja pagar: '))
    tres_ou_mais = (produto + (produto * 20 / 100)) / quantas_vezes
    print('Você pagará {}x de R${:.2f} COM JUROS'.format(quantas_vezes, tres_ou_mais))
    print('Sua compra de R${:.2f} vai acabar custando R${:.2f} no final.'.format(produto, quantas_vezes * tres_ou_mais))
else:
    print('Opção inválida. Selecione as opções 1, 2, 3 ou 4')
