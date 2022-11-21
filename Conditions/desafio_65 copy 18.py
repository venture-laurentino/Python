#CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO.
#NO FINAL DA EXECUCAO, MOSTRE A MEDIA ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E O MENOR VALOR LIDO.
#O PROGRAMA DEVE PERGUNTAR AO USUARIO  SE ELE QUER OU NAO CONTINUAR A DIGITAR VALORES.


resp = 'S'
num = cont = soma = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    resp = str(input('Deseja continuar ? [S/N] : '))
    soma += num
    cont += 1
    media = soma/cont

    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
#print('FIM')
print ('''
Foram digitados {} valores
A soma de todos eles e {}
A media entre eles e {:.2f}
O maior numero e {}
O menor numero e {}'''.format(cont, soma, media, maior, menor))