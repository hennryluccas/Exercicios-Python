'''
Desenvolva um programa que leia o nome, idade e
sexo de 4 pessoas. No final do programa, mostre:

- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos

'''

soma_idades = 0  # cria o acumulador da soma das idades, começa em 0
maior_idade = 0  # cria a variável que vai guardar a maior idade entre os homens, começa em 0
nome_homem_mais_velho = ''  # cria a variável que vai guardar o nome ligado à maior_idade, começa vazia
meninas = 0  # cria o contador de mulheres com menos de 20 anos, começa em 0

for pessoa in range(1, 5):  # repete 4 vezes (pessoa 1 a 4)
    print('---- {}ª PESSOA ----'.format(pessoa))  # mostra o cabeçalho de qual pessoa está sendo lida
    nome = str(input('Nome: '))  # lê o nome da pessoa atual
    idade = int(input('Idade: '))  # lê a idade da pessoa atual
    sexo = str(input('Sexo [M/F]: ')).upper()  # lê o sexo e converte pra maiúsculo, pra aceitar 'm' ou 'M'
    soma_idades = soma_idades + idade  # soma a idade dessa pessoa ao total acumulado
    if sexo == 'M':  # verifica se essa pessoa é homem
        if idade > maior_idade:  # compara: essa idade é maior que o recorde atual?
            maior_idade = idade  # se sim, substitui o recorde de idade
            nome_homem_mais_velho = nome  # e substitui o nome junto, pra manter os dois sincronizados
    else:  # se não é homem (ou seja, é mulher)
        if sexo == 'F' and idade < 20:  # verifica se é mulher E tem menos de 20 anos
            meninas = meninas + 1  # se sim, soma 1 ao contador de meninas

media = soma_idades / 4  # calcula a média dividindo a soma total pela quantidade de pessoas
print('A  média de idade do grupo é {}'.format(media))  # mostra a média final
print('O homem mais velho é {}, com {} anos'.format(nome_homem_mais_velho, maior_idade))  # mostra o nome e idade do homem mais velho
print('Ao todo são {} mulheres com menos de 20 anos'.format(meninas))  # mostra o total de mulheres jovens contadas