#DESENVOLVA UM PROGRAMA QUE LEIA SEIS NUMEROS INT E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES.
#SE O VALOR DIGITADO FOR IMPAR DESCONSIDERE-O.

s = 0
for c in range(0,6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        s += n
print (f'A soma dos numeros pares e {s}')