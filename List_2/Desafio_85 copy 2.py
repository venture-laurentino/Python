#CRIE UM PROGRAMA ONDE O USUARIO POSSA DIGITAR SETE VALROES NUMERICOS E CADASTRE-OS EM UMA LISTA UNICA QUE MANTENHA SPERARODS OS VALORES PARES E IMPARES.
#NO FINAL, MOSTRE OS VALORES PARES E IMPARES EM ORDEM CRESCENTE.

import os
os.system('cls')

num_par = []
num_impar = []

for n in range(0,7):
    n = int(input('Digite um numero: '))
    if n  % 2 == 0:
        num_par.append(n)
    else:
        num_impar.append(n)
        
print('-='*10)
print('')
print(f'Numero Pares\n{num_par}\nNumeros Impares\n{num_impar}')
print('')
