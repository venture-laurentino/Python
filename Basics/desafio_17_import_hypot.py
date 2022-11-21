#FACA UM PROGRAMA QUE LEIA O COMPRIMENTO DE UM CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIANGULO RETANGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

#from math import sqrt
#co = float(input('Cateto oposot: '))
#ca = float(input('Cateto adjacente: '))
#coq = (co**2)
#caq = (ca**2)
#h = sqrt(c1q+c2q)

#print('O comprimento da hipotenusa e {:.1f}'.format(h))

import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = math.hypot(co,ca)

print('A hipotenusa e {:.1f}'.format(h))
