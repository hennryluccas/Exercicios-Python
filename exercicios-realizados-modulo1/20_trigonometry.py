import math
a = float(input('Digite um ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print('O seno de {} é {:.2f}!'.format(a, s))
print('O cosseno de {} é {:.2f}!'.format(a, c))
print('A tangente de {} é {:.2f}!'.format(a, t))
