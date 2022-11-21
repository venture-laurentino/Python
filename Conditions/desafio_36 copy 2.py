#ESCREVA UM PROGRAMA PARA APROVAR O EMPRESTIMO BANCARIO PARA A COMPRA DE UMA CASA.
#O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALARIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
#CALCULE O VALOR DA PRESTACAO MENSAL, SABENDO QUE ELE NAO PODE EXCEDER 30%   DO SALARIO OU ENTAO O EMPRESTIMO SERA NEGADO.

casa = float(input('Valor da casa: '))
salario = float(input('Valor do salario: '))
parcela = int(input('Parcelas: '))
prest = casa/parcela
vp = salario*30/100

if prest >vp:
    print('O seu salario e ${}\nSua parcela supera 30%, do salario, totalizando ${:.2f} portanto seu emprestimo foi NEGADO.\nAumente o valor da parcela para tentar negociar.'.format(salario, prest))
else:
    print('Parabens, emprestimo APROVADO em {}x mensais de ${:.2f}.'.format(parcela, prest))