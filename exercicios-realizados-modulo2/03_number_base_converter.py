'''
Escreva um programa que leia um número
inteiro qualquer e peça para o usuário escolher qual será a base
de conversão.

1 - para binário
2 - para octal
3 - para hexadecimal
'''

n = int(input('Digite um número que deseja converter: '))
opcoes = int(input('Para qual sistema numérico você deseja converter: \n1 - Binário \n2 - Octal \n3 - Hexadecimal \nEscolha a sua opção: '))
if opcoes == 1:
    binario = bin(n)
    print('O número {} convertido para binário é {}'.format(n, binario[2:]))
elif opcoes == 2:
    octal = oct(n)
    print('O número {} convertido para octal é {}'.format(n, octal[2:]))
elif opcoes == 3:
    hexadecimal = hex(n)
    print('O número {} convertido para hexadecimal é {}'.format(n, hexadecimal[2:]))
else:
    print('Opção inválida! Escolha 1, 2 ou 3')

