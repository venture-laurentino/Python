#FACA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOTRANDO EM SEGUIDA O PRIMEIRO E ULTIMO NOME SEPARADAMENTE
    #EX.: ANA MARIA DE SOUZA
    #PRIMEIRO: ANA
    #ULTIMO: SOUZA

nome = str(input('Digite o nome: ')).upper()
div = nome.split()
print ('Primeiro nome: {}'.format(div[0]))
print ('Ultimo nome: {}'.format(div[len(div)-1])) # O -1 indica a ultima posicao , ou seja o ultimo nome da string, seguido do len(variavel)