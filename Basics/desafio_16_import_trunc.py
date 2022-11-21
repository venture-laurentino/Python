#CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A USA PORCAO INTEIRA
#EX.: DIGITE UM NUMERO: 6.127
#O NUMERO 6.127 TEM A PARTE INTEIRA 6

#import math
from math import trunc
n = float(input('Digite um numero real: '))
#i = math.trunc(n)
i = trunc(n)

print ('A parte inteira desse num. e: {}'.format(i))
