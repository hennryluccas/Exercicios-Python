'''
Melhore o DESAFIO 28 do Mundo 2, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

termo_usuario = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 1
termo = termo_usuario
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} → '.format(termo), end='')
        termo = termo + razao
        contador = contador + 1
    print('FIM')
    mais = int(input('Você deseja quantos termos a mais? '))
print('FIM')
print('Progressão finalizada com {} termos'.format(total))
