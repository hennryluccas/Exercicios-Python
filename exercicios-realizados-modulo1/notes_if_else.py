#Possibilidades com if e else

#1
nome = str(input('Digite seu nome: '))
if nome == 'Hennry':
    print('Seu nome é bonito')
else:
    print('Seu nome é comum')
print('Bom dia,', nome.capitalize())

#2
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 5.0:
    print('Sua nota foi {:.1f}! Parabéns! Continue assim!'.format(media))
else:
    print('Sua nota foi {:.1f}! Você precisa se esforçar mais!'.format(media))
print('Bons estudos')
