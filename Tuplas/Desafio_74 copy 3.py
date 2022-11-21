#CRIE UM PROGRAMA QUE VAI GERAR CINCO NUMEROS ALEATORIOS E COLOCAR EM UMA TUPLA.
#DEPOIS DISSO, MOSTRAR A LISTAGEM DE NUMEROS GERADOS E TAMBEM INDIQUE O MENOR E O MAIOR VALOR QUE ESTAO NA TUPLA

import random
num = random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)
print(f'Os numeros sorteados foram: {num}')
print(f'O maior valor foi: {max(num)}')
print(f'O menor valor foi: {min(num)}')






