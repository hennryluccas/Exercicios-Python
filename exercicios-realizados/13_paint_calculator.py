print('Obs: Cada litro de tinta pode pintar 2 metros quadrados.')
lar = int(input('Digite a largura da parede: '))
alt = int(input('Digite a altura da parede: '))
a = lar * alt
print('A dimensão da parede é de {}m x {}m e a área total é de {}m²!'.format(lar, alt, a))
l = lar * alt /2
print('Para pintar a área total você precisará de {} litros de tinta!'.format(l))