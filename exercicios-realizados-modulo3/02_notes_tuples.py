a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)

print('-' * 40)

print(len(c))
# Vai mostrar quantos elementos têm

print('-' * 40)

d = (9, 8, 7)
e = (9, 6, 1)
f = d + e
print(f.count(9)) # Aqui ele mostra quantas vezes o número selecionado aparece

print('-' * 40)

print(f)
print(f.index(9)) # Aqui ele mostra em que posição está o número selecionado
# Se caso tem dois números repetidos, ele vai apresentar a posição do primeiro número selecionado

print('-' * 40)

print(f)
print(f.index(9,1))
'''Aqui o número 9 repete duas vezes, mas eu quero a posição do segundo.
Para isso, mandei o programa começar a procurar o 9 apenas a partir da posição 1 (onde está o número 8).
Assim, ele ignora o primeiro 9 e encontra o próximo que aparece do 8 em diante'''

print('-'*40)

pessoa = ('Hennry', 26, 'M', 1.87)
print(pessoa)

print('-'*40)

pessoa2 = ('Marcos', 25, 'M', 1.80)
del(pessoa2)
# Não é possível modificar uma tupla, mas deletar pode