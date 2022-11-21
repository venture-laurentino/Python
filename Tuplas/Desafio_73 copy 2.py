#CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA LISTA DE MELHORES JOGOS, NA ORDEM DE COLOCACAO. DEPOIS MOSTRE
#A) APENAS OS 5 PRIMEIROS COLOCADOS
#B) OS ULTIMOS 4 COLOCADOS
#C) LISTA COM OS JOGOS EM ORDEM ALFABETICA
#D) EM QUE POSICAO NA TABELA ESTA O RED DEAD REDEMPTION 2

games = ('Horizon Forbidden West', 'The Witcher 3', 'Chrono Trigger', 'Megaman', 'Shadow of the Colossus', 'Elden Ring',  
'Kena: Bridge of Spirit', 'Red Dead Redemption 2', 'God of War', 'Days Gone', 'Mortal Kombat 11', 'World of Warcraft', 'Dungeons & Dragons',
'Sekiro', 'Dark Souls', 'Dragon Age Origins', 'Last of Us', 'Shadow of War', 'Batman',
'Call of Duty Warzone',  )

print('-='*15)
print('Games Favoritos')
print('-='*15)
print(sorted(games))
print('-='*15)
print(f'''Os 5 melhores sao: 
{(games[:5])}''')
print('-='*15)
print(f'''Os 4 ultimos colocados sao:
{games[-4:]}''')
print('-='*15)
print(f'Red Dead Redemption esta na psicao {games.index("Red Dead Redemption 2")}')
