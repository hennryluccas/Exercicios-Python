'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''

maior = 0 # Cria a variável que vai guardar o maior peso, começa com 0 só para existir
menor = 0 # Cria a variável que vai guardar o menor peso, começa com 0 só para existir
for pessoas in range(1,6): # repete 5 vezes (pessoa 1 a 5), "pessoas" identifica qual é (pessoa 1, pessoa 2 e assim por diante
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pessoas))) # Lê o peso da pessoa atual sempre um valor novo que o usuário vai deixar
    if pessoas == 1: # pergunta: essa é a primeira pessoa?
        maior = peso # é a primeira, então guarda sem comparar: esse vira o maior "provisório"
        menor = peso # mesma coisa: esse peso vira o menor "provisório"
    else: # a partir da segunda pessoa em diante
        if peso > maior: # o peso novo é maior que o recorde atual?
            maior = peso # se sim, substitui: esse peso vira o novo maior
        if peso < menor: # o peso novo é menor que o recorde atual?
            menor = peso # se sim, substitui: esse peso vira o novo menor
print('O maior peso foi: {}'.format(maior))
print('O menor peso foi: {}'.format(menor))

'''
Na prática é assim que funciona cada etapa

Testando com 70.5 (pessoa 1), 55.2 (pessoa 2), 90.8 (pessoa 3), 60.1 (pessoa 4), 80.3 (pessoa 5)
pessoa 1: maior = 70.5, menor = 70.5
pessoa 2 (55.2): 55.2 > 70.5? não. 55.2 < 70.5? sim → menor = 55.2
pessoa 3 (90.8): 90.8 > 70.5? sim → maior = 90.8
pessoa 4 (60.1): não bate nenhum recorde
pessoa 5 (80.3): não bate nenhum recorde
'''