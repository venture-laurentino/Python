#FACA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
    #QUANTAS VEZES APARECE A LETRA 'A'
    #EM QUE POSICAO ELA APARECE A PRIMEIRA VEZ
    #EM QUE POSICAO ELA APRECE A ULTIMA VEZ

frase = str(input('Digite uma frase: ')).upper() #coloque o .upper para determinar um padrao para encontrar a letra especifica para facilitar independente mais. ou mins.
print ('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print ('Sua primeira posicao e: {}'.format(frase.find('A')))
print ('Sua ultima posicao e: {}'.format(frase.rfind('A')))
