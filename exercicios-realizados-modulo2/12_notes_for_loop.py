# Aula sobre repetições (for)

#Exemplo 1
for c in range (1,6):
    print('Oi')
print('FIM')

#Exemplo 2
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('FIM')

#Exemplo 3
s = 0
for c in range (0,4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))

#Exemplo 4
for c in range (0,10):
    n = int(input('Digite um valor: '))
print('Fim')