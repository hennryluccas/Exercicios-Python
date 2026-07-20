n1 = int(input('Escolha um número: '))
dob = n1*2
tri = n1*3
raiz = n1**(1/2)
print('O número que você escolheu é {} \nO seu dobro é {}, \nO seu triplo é {} \nE a sua raiz quadrada é {:.3}'.format(n1, dob, tri,raiz))

# Posso fazer no esquema do exercício anterior, posso fazer direto

n1 = int(input('Escolha um número: '))
print('O número que você escolheu é {} \nO seu dobro é {}, \nO seu triplo é {} \nE a sua raiz quadrada é {:.3}'.format(n1, (n1*2), (n1*3), (n1**(1/2))))