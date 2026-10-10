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



'''
COMO FUNCIONA (pense numa escada)

termo                = o número da PA que eu falo em cada degrau
contador             = o degrau em que estou
total                = o degrau onde quero chegar
mais                 = quantos degraus subir nessa rodada

Exemplo: primeiro termo 5, razão 3

Rodada 1:
  mais = 10, então total = 0 + 10 = 10
  subo do degrau 1 ao 10: 5 → 8 → 11 → 14 → 17 → 20 → 23 → 26 → 29 → 32
  paro com contador = 11 e termo = 35

O programa pergunta "quantos termos a mais?" e a pessoa digita 5

Rodada 2:
  mais = 5, então total = 10 + 5 = 15
  NÃO volto pro chão: contador continua em 11 e termo continua em 35
  subo do degrau 11 ao 15: 35 → 38 → 41 → 44 → 47

O programa pergunta de novo e a pessoa digita 0
  mais = 0, o while de fora para e o programa acaba

RESUMO
  while de fora   = pergunta "quer subir mais?"
  while de dentro = sobe os degraus até a meta
  contador e termo não voltam pro zero entre as rodadas, por isso a PA continua de onde parou
'''