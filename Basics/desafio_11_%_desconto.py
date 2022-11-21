#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO
#CALCULO DE PORCENTAGEM - %/100*VALOR
#EX: 20% DE 200 >>> 20/100=0.2 >> 0.2*200=40
#EX.2: VALOR * % / 100

v = int(input ('Qual o valor do produto? '))
p = v - (v * 5 / 100)
#p = 5/100
#d = p*v

#print ('O valor do produto e ${} e com 5%, de desconto ele sai a {}' .format (v, v-d))
print ('O valor do produto e ${} e com 5%, de desconto ele sai a {}' .format (v, p))
