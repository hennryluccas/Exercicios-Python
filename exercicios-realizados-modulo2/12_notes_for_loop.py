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
    s += n # ou posso usar s = s + n
print('O somatório de todos os valores foi {}'.format(s))

#Exemplo 4
for c in range (0,10):
    n = int(input('Digite um valor: '))
print('Fim')

#Exemplo 5
for c in range (6, 0, -1): # O -1 serve para representar uma contagem regressiva, ou seja, ele vai contar para trás
    print(c)
print('FIM')

#Exemplo 6
for c in range (0, 7, 2): #Agora ele vai contar de 0 a 6 pulando de dois em dois
    print(c)
print('FIM')
