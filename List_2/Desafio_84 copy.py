#FACA UM PROGRAMA QUE LEIA NOME E PESO DE VAIRAS PESSOAS, GUARDANDO TUDO EM UMA LISTA.
#NO FINAL, MOSTRE:

#A) QUANTAS PESSOAS FORAM CADASTRADAS.
#B) UMA LISTAGEM COM AS PESSOAS MAIS PESADAS.
#C) UMA LISTAGEM COM AS PESSOAS MAIS LEVES.

import os
os.system('cls')

pessoas = []
dados = []
count = 0
maior = 0
menor = 0
op = 1

#def relatorio(count, maior, menor):
#    print(f'As pessoas mais pesadas')

while op == 1:
    
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    print('')
    op = int(input('''DESEJA CONTINUAR ?    
    [1] SIM
    [2] NAO
    >>> '''))
    count += 1
    print('')
    os.system('cls')

for p in pessoas:
    if p[1] >= 65:
        maior += 1
        print(f'{p[0]} e pesado(a)')
    else:
        menor += 1
        print(f'{p[0]} e leve')

print(f'Temos {maior} pessoas pesadas e {menor} pessoas leves.')






