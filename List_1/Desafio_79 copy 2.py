#CRIE UM PROGRAMA ONDE O USUARIO POSSA DIGITAR VARIOS VALORES NUMERICOS E CADASTRE-OS EM UMA LISTA.
#CASO O NUMERO JA EXISTA LA DENTRO ELE NAO SERA ADICIONADO.
#NO FINAL, SERAO EXIBIDOS TODOS OS VALORES UNICOS DIGITADORS, EM ORDEM CRESCENTE.

valores = []
op = 1

while op == 1:

    valores.append(int(input('Digite um valor: ')))
    print(' ')
    
    op = int(input('''Deseja continuar ? 
    
    [1] SIM
    [2] NAO
    >>> '''))
    print(' ')

valores = list(set(valores))
valores.sort()
print(valores)

