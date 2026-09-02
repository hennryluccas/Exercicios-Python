'''
Refaça o DESAFIO 11 do módulo 1, mostrando a tábuada de um número que o usuário escolher,
só que agora utilizando um laço for
'''

num = int(input('Digite um valor: '))
for c in range(0, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))