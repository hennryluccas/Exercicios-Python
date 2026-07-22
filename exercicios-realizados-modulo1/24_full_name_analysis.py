''' Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo sem considerar espaços.
- Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))

print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))

'''O (strip) elimina a quantidade de espaços iniciais e finais. 
O (len) analisará o comprimento do nome.
E o (count) vai contar quantas vezes repete os espaços na frase.
'''

separa = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
