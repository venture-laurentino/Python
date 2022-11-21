#ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PRECO NORMAL E CONDICAO DE PAGAMENTO:
#A VISTA DINHEIRO/CHEQUE - 10% DE DESCONTO
#A VISTA NO CARTAO - 5% DE DESCONTO
#EM ATE 2X NO CARTAO - PRECO NORMAL
#3X OU MAIS NO CARTAO - ACRESCIMO DE 20%

v = float(input('Valor do produto: '))
p = int(input('Quantidade de parcelas: '))
f = str(input('Forma de pagamento: ')).upper()

if p == 1 and f == 'DINHEIRO' or f == 'CHEQUE':
    print('O produto custa ${}, porem nessa condicao ele sai a ${}'.format(v,v-(v*10/100)))
elif p == 1 and f == 'CARTAO':
    print('O produto custa ${}, porem nessa condicao ele sai a ${}'.format(v,v-(v*5/100)))
elif p == 2 and f == 'CARTAO':
    print(f'O produto sai pelo preco normal de ${v}.')
elif p >=3 and f == 'CARTAO':
    print('O produto custa ${}, porem nessa condicao ele sai a ${}'.format(v,v+(v*20/100)))