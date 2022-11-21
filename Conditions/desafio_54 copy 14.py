#CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NAO ATINGIRAM A MAIORIDADE E QUATAS JA SAO MAIORES.

from datetime import date       #<--- metodo para importar a data atual
b = date.today().year           #                <---I
mai = 0
men = 0
for c in range(0,7):
    d = int(input('Data de nascimento: '))
    i = b - d
    if i >= 18:
        mai += 1
    else:
        men += 1    
print(f'Maiores: {mai}\nMenores: {men}')