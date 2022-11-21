#DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZAO DE UM PA (PROGRESSAO ARITIMETICA).
#NO FINAL MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSAO.

t = int(input('Primeiro termo: '))
r = int(input('Razao: '))
d = t + (10-1) * r                  # <---- formula para o decimo termo
for c in range(t, d, r):
    print(c, end = ' -- ' )