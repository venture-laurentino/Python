#FACA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE E BISSEXTO.
#AND - E TAMBEM
#!= - DIFERENTE DE
#OR - OU

ano = int(input('Qual ano quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('O ano {} e BISSEXTO'.format(ano))
else:
    print ('O ano {} NAO e BISSEXTO'.format(ano))