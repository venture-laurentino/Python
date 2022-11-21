#CRIE UM PROGRAMA QUE TENHA UMA TUPLA UNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PRECOS, NA SEQUENCIA.
#NO FINAL, MOSTRE UMA LISTAGEM DE PRECOS, ORGANIZANDO OS DADOS EM FORMA TABULAR.

produtos = 'PC Gamer', 8.000, 'Monitor 2k', 1.800, 'Horizon Forbbiden West', 300, 'Playstation 5', 4.500, 'Manete Xbox One X', 300

for pos in range (0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='') # :.<30 alinhamento à esquerda
    else:
        print(f'${produtos[pos]:>7.3f}') #.3f casas decimais usando a formatação em f, sem necessidade do .format