'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
EX: Ana Maria de Souza
Primeiro = Ana
Último = Souza
'''

nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('Seu primeiro nome é: {}'.format(lista[0]))
print('Seu último nome é: {}'.format(lista[-1]))

'''
partes[0] = 'Ana'
partes[1] = 'Maria'
partes[2] = 'de'
partes[3] = 'Souza'

partes[-1] = 'Souza'   ← o último
partes[-2] = 'de'      ← o penúltimo
partes[-3] = 'Maria'
partes[-4] = 'Ana'
'''