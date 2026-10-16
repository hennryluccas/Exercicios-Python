'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada valor
serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

print('='*30)
print('{:^30}'.format('BANCO HENNRY'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total = total - ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('-'*30)
print('Volte sempre ao BANCO HENNRY! Tenha um bom dia!')

# Explicação:

'''
1. Volta 1 do Loop:
	• O total é 70. A cédula (ced) é 50.
	• total >= ced? (70 é maior que 50?) Sim!
	• O código faz: total -= ced (70 - 50 = 20).
	• Ele conta uma nota: totalced vira 1.
	• O loop faz a curva e volta para o topo.
2. Volta 2 do Loop:
	• O total agora é 20. A cédula (ced) continua sendo 50.
	• total >= ced? (20 é maior que 50?) Não!
	• O código pula direto para o else.
	• Como totalced é 1 (maior que 0), ele printa: "Total de 1 cédulas de R$ 50".
	• Ele testa os ifs das cédulas: Como ced == 50, ele transforma a cédula em 20.
	• Ele limpa a mão para a próxima contagem: totalced = 0.
	• Ele testa: total == 0? Não, o total ainda é 20.
	• O loop faz a curva e volta para o topo.
3. Volta 3 do Loop:
	• O total é 20. A cédula (ced) agora é 20.
	• total >= ced? (20 é maior que 20?) Sim! (É igual).
	• O código faz: total -= ced (20 - 20 = 0).
	• Ele conta uma nota: totalced vira 1.
	• O loop faz a curva e volta para o topo.
4. Volta 4 do Loop:
	• O total é 0. A cédula (ced) é 20.
	• total >= ced? (0 é maior que 20?) Não!
	• O código pula para o else.
	• Ele printa: "Total de 1 cédulas de R$ 20".
	• Ele testa as cédulas: Como ced == 20, ele mudaria para 10 (mas nem vai dar tempo).
	• Ele limpa a mão: totalced = 0.
	• Ele faz o teste final: total == 0? Sim! O total chegou a zero!
	• O comando break é acionado e desliga o programa.
'''
