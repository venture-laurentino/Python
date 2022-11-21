import random

game = True
hp_player = 100
hp_monstro = 60

while game == True:

    def resultado_ataque(monstro, player_dado ):
        print(f'O monstro tirou {monstro}\nVc atacou e tirou {player_dado}')

    def hp_m(hp_monstro):
        print(f'Voce conseguiu ferir o monstro\nO Hp do monstro foi reduzido para {hp_monstro}') 

    def hp_p(hp_player):
        print(f'Vc foi ferido\nO seu Hp foi reduzido para {hp_player}')

    monstro = random.randint(1,20)
    player_dado = random.randint(1,20)

    print('-='*30)
    print('''Tem um Troll das cavernas logo a sua frente, o que vc faz? 

    [1] ATACAR
    [2] DEFENDER
    [3] FUGIR

    ''')
    print('-='*30)

    player = int(input('Qual a sua acao? '))

    if player == 1:        
        resultado_ataque(monstro, player_dado )

        if player_dado >= monstro:
            hp_monstro = hp_monstro - player_dado
            hp_m(hp_monstro)

        else:
            hp_player = hp_player - monstro            
            hp_p(hp_player)         
        
    elif player == 2:
        print(f'O monstro atacou {monstro}')
        print(f' Vc decidiu defender e conseguiu a pontuacao {player_dado}')
        if player_dado >= monstro:
            print('Vc defendeu o ataque do monstro com sucesso')
        else:
            print('Vc nao conseguiu se defender e foi ferido')
            
    else:
        print('Vc decidiu fugir')
        game = False

