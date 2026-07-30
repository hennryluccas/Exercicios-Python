'''
Refaça o desafio 037 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''

lado1 = int(input('Digite o primeiro lado: '))
lado2 = int(input('Digite o segundo lado: '))
lado3 = int(input('Digite o terceiro lado: '))
#Validade do triângulo
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Pode formar um triângulo.', end=' ')
    if lado1 == lado2 == lado3: #Qual tipo de triângulo
        print('Esse é um triângulo EQUILÁTERO (todos os lados iguais)')
    elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        print('Esse é um triângulo ESCALENO (todos os lados diferentes)')
    else:
        print('Esse é um triângulo ISÓSCELES (dois lados iguais)')
else:
    print('Não é possível formar um triângulo')
