#MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI 'PENSAR' EM UM NUMERO ENTRE 0 E 10.
#SO QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATE ACERTAR. MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSARIOS PARA VENCER.

import random
pc = int(random.randint(0,10))
print(pc)
count = 0
while pc != 11:
    print('-='*10)
    jg = int(input('Escolha um numero: '))
    count += 1
    if jg == pc:
        print('You Win !')
        print(f'Palpites: {count}')
        print('-='*10)
        break        
    elif jg > 11:
        print('Valor Invalido.')
        print('-='*10)
    else:
        print('You Loose !')
        print('-='*10)


