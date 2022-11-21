#FACA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE TODA A SUA TABOADA

n = int(input ('INSERT A NUMBER: '))
#print ('YOUR SUM TABLE IS: \n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}' .format(n+1, n+2, n+3, n+4, n+5, n+6, n+7, n+8, n+9))
#print ('YOUR SUB TABLE IS: \n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}' .format(n-1, n-2, n-3, n-4, n-5, n-6, n-7, n-8, n-9))
#print ('YOUR MULT TABLE IS: \n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}' .format(n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9))
#print ('YOUR DIV TABLE IS: \n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}' .format(n/1, n/2, n/3, n/4, n/5, n/6, n/7, n/8, n/9))

print ('-'*12) #USADO PARA INSERIR O CONTEUDO ENTRE ASPAS VARIAS VEZES, MULTIPLICADO PELO NUMERO DE VEZES QUE VC QUER Q ELE SE REPITA
print ('{} + {} = {}'.format(n, 2, n+2))
print ('{} - {} = {}'.format(n, 2, n-2))
print ('{} * {} = {}'.format(n, 2, n*2))
print ('{} / {} = {}'.format(n, 2, n/2))
print ('-'*12)