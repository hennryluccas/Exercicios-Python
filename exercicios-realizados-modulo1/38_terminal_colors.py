#Aula de cores
print('\033[4;30;45mOlá, Mundo!\033[m')

nome = 'Hennry'
print('Prazer em te conhecer {}{}{}!'.format('\033[4;30;45m', nome, '\033[m'))

nome = 'Aina'
print('Prazer em te conhecer {}{}{}!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

nome = 'Aina'
print('Prazer em te conhecer {}{}{}!'.format(cores['amarelo'], nome, cores['limpa']))
