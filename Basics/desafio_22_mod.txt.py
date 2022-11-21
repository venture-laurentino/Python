#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
    #O NOME COM TODAS AS LETRAS MAIUSCULAS
    #O NOME COM TAS AS LETRAS MINUSCULAS
    #QUANTAS LETRAS AO TD SEM CONSIEDERAR ESPACOS
    #QUANTAS LETRAS TEM O PRIMEIRO NOME
    

nome = str(input('Digite o nome: ')).strip() #podemos colocar o .satrip na variavel para corrigir possiveis erros de espaco durante o codigo
print ('UPPER: {}'.format(nome.upper()))
print ('LOWER: {}'.format(nome.lower()))
print ('QNTD DE LETRAS SEM ESPACOS: {}'.format(len(nome)-nome.count(' ')))
print ('O PRIMEIRO NOME TEM {} LETRAS'.format(nome.find(' '))) #nesse caso find ira encontrar o primeiro espaco, ou seja contara todas as letras tem antes de chegar ao primeiro espaco





