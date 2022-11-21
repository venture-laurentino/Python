#ESCREVA UM PROGRAMA QUE LEIA DOIS NUMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA MSG:
#O PRIMEIRO VALOR E MAIOR
#O SEGUNDO VALOR E MAIOR
#NAO EXISTE VALOR MAIOR, OS DOIS SAO IGUAIS

n1 = int(input('Digite num 1: '))
n2 = int(input('Digite num 2: '))
maior = n1
if n1>n2:
    print(f'{n1} e o maior valor\n{n2} e o segundo maior valor')
elif n2>n1:
    print(f'{n2} e o maior valor\n{n1} e o segundo maior valor')
else:
    print('Nao existe valor maior, os dois sao iguais')
