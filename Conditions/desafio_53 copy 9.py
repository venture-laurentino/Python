#CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA E UM PALINDROMO, DESCONSIDERANDO OS ESPACOS.

#EX.:
#APOS A SOPA
#A SACADA DA CASA
#A TORRE DA DERROTA
#O LOBO AMA O BOLO
#ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase: ')).upper() .strip()
palavra  = frase.split()
junto = ''.join(palavra)   
inverso =  '' #junto [::-1] - metodo sem for
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} e {inverso}')
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao e um palindromo!')