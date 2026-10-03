'''
Crie um programa que leia uma frase qualquer e diga se
ela é um palíndromo, desconsiderando os espaços.
Exemplo: Apos a sopa
'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')

'''
Outra forma de resolver mais fácil!

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')
'''