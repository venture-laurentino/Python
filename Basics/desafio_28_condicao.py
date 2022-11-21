#ESCREVA UM PROGRAMA QUE FACA O COMPUTADOR 'PENSAR' EM UM NUMERO INTEIRO ENTRE 0 E 5 E PECA PARA O USUARIO TENTAR DESCOBRIR QUAL FOI O NUMERO ESCOLHIDO PELO COMPUTADOR
#O PROGRAMA DEVERA ESCREVER NA TELA SE O USUARIO VENCEU OU PERDEU.

import random
num = int(random.randint(0,5))
#num = random.choice(lista)
print (num)
esc = int(input('Escolha um numero: '))
if esc == num:
    print('You Win!')
else:
    print('You Lose!')