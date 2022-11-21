#DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-OS EM UMA TUPLA. NO FINAL, MOSTRE:

#A) QUANTAS VEZES APARECEU O VALOR 9.
#B) EM QUE POSICAO FOI DIGITADO O PRIMEIRO VALOR 3.
#C) QUAIS FORAM OS NUMEROS PARES

print('-='*15)
num = int(input('Primeiro numero: ')), int(input('Segundo numero: ')), int(input('Terceiro numero: ')), int(input('Quarto numero: '))

print('-='*15)
print(f'O numero 9 foi digitado {num.count(9)} vezes')

if 3 in num:
    print(f'O numero 3 foi digitado na posicao {num.index(3)+1}')
else:
    print('O valor 3 nao foi digitado')
print('Os valores pares digitados foram: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

