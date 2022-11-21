#CRIE UM PROGRAMA QUE LEIA UM NUMERO INT E MOSTRE NA TELA SE ELE E PAR OU IMPAR

num = int(input('Digite um numero: '))
res = num % 2 #com essa formula identificamos se e par ou impar. Qualquer numero par o resto da divisao sera 0 e impar sera 1
if res == 0:
    print('O numero {} e PAR.'.format(num))
else:
    print('O numero {} e IMPAR.'.format(num))

