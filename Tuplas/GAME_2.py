
import random

game =True
count_l = 0
count_npc = 0

while game == True:
    print('-='*50)
    landin = int(input('Landin, estou pensando em um numero entre 1 e 5, qual em qual numero eu estou pensando? '))
    npc = random.randint(1,5)
    print('-='*50)
    if landin == npc:
        count_l += 1
        print(f'O NPC tirou {npc}, Landin WINS !!! =)')
        print(f'Landin obteve {count_l} vitorias')
    else:
        count_npc += 1
        print(f'O NPC tirou {npc}, Landin LOOSE !!! =(')
        print(f'NPC obteve {count_npc} vitorias')
    print('-='*50)