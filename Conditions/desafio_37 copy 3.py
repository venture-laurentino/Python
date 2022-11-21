#ESCREVA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E PECA PARA O USUARIO ESCOLHER QUAL SERA A BASE DE CONVERSAO:
#1 PARA BINARIO
#2 PARA OCTAL
#3 PARA HEXADECIMAL

num = int(input('Numero:'))
conv = int(input('Qual a base de conversao?\n1 para BINARIO\n2 para OCTAL\n3 para HEXADECIMAL\n:'))

if conv == 1:
    print('BINARIO')
elif conv == 2:
    print('OCTAL')
elif conv == 3:
    print('HEXADECIMAL')
else:
    print('Valor Invalido !')
    