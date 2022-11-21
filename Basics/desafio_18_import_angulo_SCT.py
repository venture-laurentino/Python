#FACA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA O CALCULO DO SENO, COSSENO E TANGENTE DESSE ANGULO
# Para este exercicio e necessario a conversao do angulo para radianos com o '.radians'
import math
a = float(input('Digite o angulo: '))
s = math.sin(math.radians(a))
print('Angulo {} tem o SENO  de {:.2f}'.format(a,s))
c = math.cos(math.radians(a))
print('Angulo {} tem o COSSENO de {:.2f}'.format(a,c))
t = math.tan(math.radians(a))
print('Angulo {} tem a TANGENTE {:.2f}'.format(a,t))