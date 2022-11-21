##FACA UM PROGRAMA QUE LEIA UM NUMERO INT QUALQUER E MOSTRE O  SEU FATORIAL

#Ex.: 5!=5x4x3x2x1=120

n = int(input('Digite um numero: '))
#c = n
f = 1
while n > 0:
    print(n, end=' ')
    print(' x ' if n > 1 else ' = ', end=' ')
    f *= n
    n -= 1
print(f)