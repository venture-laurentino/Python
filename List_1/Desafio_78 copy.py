#FACA UM PROGRAMA QUE LEIA 5 VALORES NUMERICOS E GUARDE-OS EM MA LISTA
#NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIGITADO E AS SUAS RESPECTIVAS POSICOES NA LISTA.

lista = []
maior = 0
menor = 0

for n in range (0,5):
    lista.append(int(input('Digite um numero: ')))

print(f'Sua lista e {lista}')
lista.sort()
print(f'Sua lista ordenada e {lista}')
print(f'O maior numero da lista e o {max(lista)}')
print(f'O menor numero da lista e o {min(lista)}')
