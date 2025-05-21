# Calculando hipotenusa

from math import hypot
c1 = float(input('Digite o valor do Cateto Oposto: '))
c2 = float(input('Digite o valor do Cateto Adjacente: '))
h = hypot(c1, c2)
print('O valor da hipotenusa é {:.2f}'.format(h))
