num_1 = int(input('Primeiro Valor: '))
num_2 = int(input('Segundo Valor: '))
continuar = True
while continuar:
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')
    opcao_usuario = int(input('>>>>> Qual é a sua opção: '))
#1
    if opcao_usuario == 1:
            resultado_soma = num_1 + num_2
            print('O resultado da soma entre {} e {} é {}'.format(num_1, num_2, resultado_soma))
#2
    elif opcao_usuario == 2:
            resultado_multiplicar = num_1 * num_2
            print('O resultado da multiplicação entre {} e {} é {}'.format(num_1, num_2, resultado_multiplicar))
#3
    elif opcao_usuario == 3:
        if num_1 > num_2:
            print('O número {} é maior que o {}'.format(num_1, num_2))
        elif num_1 == num_2:
            print('Os dois números são iguais!')
        else:
            print('O número {} é maior que o {}'.format(num_2, num_1))
#4
    elif opcao_usuario == 4:
        num_1 = int(input('Primeiro Valor: '))
        num_2 = int(input('Segundo Valor: '))
#5
    elif opcao_usuario == 5:
        print('Fim do programa. Volte Sempre!')
        continuar = False
    else:
        print('Opção inválida. Tente novamente')
        continuar = True