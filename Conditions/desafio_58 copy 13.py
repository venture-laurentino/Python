#MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI 'PENSAR' EM UM NUMERO ENTRE 0 E 10.
#SO QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATE ACERTAR. MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSARIOS PARA VENCER.

from random import randint
pc = randint(0,10)
print(pc)
acertou = False
while not acertou:
    jg = int(input('Palpite: '))
    if jg == pc:
        acertrou = True
        break
print('Acertou !')


