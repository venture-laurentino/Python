#FACA UM PROGRAMA QUE LEIA UM NUMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DIGITOS SEPARADOS
#EX.: DIGITE UM NUMERO: 1834
#UNIDADE: 4
#DEZENA: 3
#CENTENA: 8
#MILHAR 1

import random
num = random.randint(0,9999)
n = str(num)
print ('O numero gerado foi: {}'.format(num))
print ('Unidade: {}'.format(n[3]))
print ('Dezena: {}'.format(n[2]))
print ('Centena: {}'.format(n[1]))
print ('Milhar: {}'.format(n[0]))

