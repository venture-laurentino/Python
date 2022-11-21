#ESCREVA UM PROGRAMA QUE LEIA 3 NUMEROS E MOSTRE QUAL E O MAIOR E QUAL E O MENOR.

a = int(input('Digite num: '))
b = int(input('Digite num: '))
c = int(input('Digite num: '))

#Verificando que e o menor

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor numero e: {}'.format(menor))

#Verificando quem e o maior

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior numero e: {}'.format(maior))
