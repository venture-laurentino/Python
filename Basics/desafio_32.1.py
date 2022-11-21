#FACA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE E BISSEXTO.

from calendar import isleap #forma de modolu
ano = int(input('Digite o ano: '))
if isleap(ano):
    print('O ano e bissexto')
else:
    print('O ano nao e bissexto')