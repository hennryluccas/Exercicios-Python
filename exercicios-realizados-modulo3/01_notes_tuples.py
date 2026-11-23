# Aula de Tuplas

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

print('-'*40)

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])

print('-'*40)

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Eu comi pra caramba!')

print('-'*40)

print(len(lanche))

print('-'*40)

for cont in range(0, len(lanche)):
    print(cont)

print('-'*40)

for cont in range(0, len(lanche)):
    print(lanche[cont])

print('-'*40)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('-'*40)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('-'*40)

print(sorted(lanche))
#Ele vai organizar em ordem alfabética