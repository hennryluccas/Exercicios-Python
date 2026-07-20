from math import floor
num = float(input('Digite um número real: '))
print('O número {} tem a parte inteira {}!'.format(num, floor(num)))

# Como o professor fez

from math import trunc
num = float(input('Digite um número real '))
print('O número {} tem a parte inteira {}!'.format(num, trunc(num)))

# Dá para fazer sem importar nada

num = float(input('Digite um número real: '))
print('O número {} tem a parte inteira {}!'.format(num, int(num)))