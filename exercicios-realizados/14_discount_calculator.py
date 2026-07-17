print('Hoje estamos com um desconto de 5% em qualquer produto')
p = float(input('Digite o preço do produto: R$'))
r = p * 5/100
v = p - r
print('O valor final com desconto sairá por {}!'.format(v))

# O professor fez o seguinte

print('Hoje estamos com um desconto de 5% em qualquer produto')
p = float(input('Digite o preço do produto: R$'))
r = p - (p * 5/100)
print('O valor final com desconto sairá por {}!'.format(r))