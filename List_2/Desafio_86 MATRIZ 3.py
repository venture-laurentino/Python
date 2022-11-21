#CRIE UM PROGRAMA QUE CIRE UMA MATRIZ DE DIMENSAO 3X3 E PREENCHA COM VALROES LIDOS PELO TECLADO
#NO FINAL, MOSTRE A MATRIZ NA TELA COM A FORMATACAO CORRETA

import os
os.system('cls')

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-='*30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()