'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

soma = 0
maior = 0
menor = 0
contador = 0
resposta = 'S'
while resposta == 'S':
    num = int(input('Digite um número: '))
    soma = soma + num
    contador = contador + 1
    if contador == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
media = soma / contador
print(f'Você digitou {contador} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
