'''
Escreva um programa que leia dois números
inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é
maior
- O segundo valor é
maior
- Não existe valor
maior, os dois são iguais
'''

numero1 = int(input('Escreva o primeiro número inteiro: '))
numero2 = int(input('Escreva o segundo número inteiro: '))
if numero1 > numero2:
    print('O primeiro número é maior que o segundo')
elif numero2 > numero1:
    print('O segundo número é maior que o primeiro')
else:
    print('Não existe valor maior, os dois são iguais')
