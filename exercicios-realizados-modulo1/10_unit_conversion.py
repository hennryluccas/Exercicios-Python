n1 = int(input('Escreva um valor em metros: '))
cen = n1*100
mili = n1*1000
deci = n1*10
deca = n1/10
hec = n1/100
km = n1/1000
print('{}m é {}cm , {}mm, {}dm, {}dam, {}hm, {}km!'.format(n1, cen, mili, deci, deca, hec, km))