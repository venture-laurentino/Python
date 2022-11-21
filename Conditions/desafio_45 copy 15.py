#CRIE UM PROGRAMA  QUE FACA O COMPUTADOR JOGAR JOKENPO COM VOCE

from random import randint
from time import sleep #PARA DETERMINAR UM TEMPO PARA APARECER ALGO NA TELA
itens = ('PEDRA', 'PAPEL', 'TESOURA')
maquina = randint(0,2)
#print('O NPC jogou {}'.format(itens[maquina]))
print('''Suas opcoes:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
player = int(input('Sua jogada: '))
print('JO')
sleep(0.5) #IO TEMPO QUE VAI DEMORAR PARA Q A PROXIMA FRASE APARECA NA TELA
print('KEN')
sleep(0.5)
print('PO!!!')
print('=-'*11)
print('O NPC jogou {}'.format(itens[maquina]))
print('O Player jogou {}'.format(itens[player]))
print('=-'*11)
if maquina == 0:
    if player == 0:
        print('EMPATE!')
    elif player == 1:
        print('VOCE VENCEU!')
    elif player == 2:
        print('O NPC VENCEU!')
elif maquina == 1:
    if player == 1:
        print('EMPATE!')
    elif player == 0:
        print('O NPC VENCEU!')
    elif player == 2:
        print('VOCE VENCEU!')
elif maquina == 2:
    if player == 2:
        print('EMPATE!')
    elif player == 1:
        print('O NPC VENCEU!')
    elif player == 0:
        print('VOCE VENCEU!')

    