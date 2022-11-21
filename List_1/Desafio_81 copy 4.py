#CRIE UM PROGRAMA QUE VAI LER VARIOS NUMEROS E COLOCAR EM UMA LISTA.
#DEPOIS DISSO MOSTRE:
#A - QUANTOS NUMEROS FORAM DIGITADOS
#B - A LISTA DE VALORES, ORDENADA DE FORMA DESCRESCENTE
#C - SE O VALOR 5 FOI DIGITADO E ESTA OU NAO NA LISTA

num = []
count = 0
count_5 = 0
op = 1

def relatorio(count, num):
    print(f'Foram digitados {count} numeros')
    print(f'Sua lista em ordem decrescente\n{num}')
  
while op == 1:

    print('-='*15)
    num.append(int(input('Digite um valor: ')))
    print(' ')
    op = int(input('''Deseja continuar?
    [1] SIM
    [2] NAO
    >>> '''))
    print(' ')  
           

num.sort(reverse=True)

relatorio(count, num)

if 5 in num:
    print(f'O numero 5 aparece na lista {num.count(5)} vez(s)')
else:
    print('O numero 5 nao aparece na lista')

