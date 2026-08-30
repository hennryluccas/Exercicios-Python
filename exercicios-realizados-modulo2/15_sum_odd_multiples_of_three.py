'''
Faça um programa que calcule a soma entre todos os números ímpares
que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
s = 0
for c in range(3, 501, 6):
    print(c)
    s += c
print('O somatório dos números ímpares que são múltiplos de três é: {}'.format(s))

#Se eu não quiser mostrar todos os números ímpares que são múltiplos de três, posso fazer o cálculo direto
s = 0
for c in range(3, 501, 6):
    s += c
print('O somatório dos números ímpares que são múltiplos de três é: {}'.format(s))