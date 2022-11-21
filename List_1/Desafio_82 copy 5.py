#CRIE UM PROGRAMA QUE VAI LER VARIOS NUMEROS E COLOCAR EM UMA LISTA
#DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VAO CONTER APENAS OS VALORES PARES E OS VALORES IMPARES DIGITADOS, RESPECTIVAMENTE
#AO FINAL MOSTRE O CONTEUDO DAS TRES LISTAS GERADAS.

lista = []
pares = []
impares = []
op = 1

def relatorio(lista, pares, impares):
    print(f'A lista completa\n{lista}')
    print(f'Numeros pares\n{pares}')
    print(f'Numeros impares\n{impares}')

while op == 1:

    lista.append(int(input('Digite um valor: ')))
    print(' ')
    op = int(input('''Deseja continuar?
    [1] SIM
    [2] NAO
    >>> '''))
    print(' ')

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

relatorio(lista, pares, impares)

    
