'''
Desenvolva uma lógica que leia o peso e
a altura de uma pessoa, calcule seu IMC e mostre
seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: abaixo do peso
- Entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- Acima de 40: obesidade mórbida
'''

peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura ** 2

if imc < 18.5:
    print('ABAIXO DO PESO. Seu IMC é {:.2f}'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('PESO IDEAL. Seu IMC é {:.2f}'.format(imc))
elif imc >= 25 and imc <= 30:
    print('SOBREPESO. Seu IMC é {:.2f}'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Você está com OBESIDADE. Seu IMC é {:.2f}'.format(imc))
else:
    print('Você está com OBESIDADE MÓRBIDA. Seu IMC é {:.2f}'.format(imc))
