'''
Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.
'''

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m') #cor amarela
        tot = tot + 1 #Aqui é a contagem de vezes que o número do usuário foi divisível pelo contador
    else:
        print('\033[31m') #cor vermelha
    print('{} '.format(c)) #Aqui é só a contagem, é o print do 1 até o número que o usuário digitou
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2: #Se foi divisível duas vezes significa que o número foi divisível por 1 e por ele mesmo, por isso ele é primo
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO')