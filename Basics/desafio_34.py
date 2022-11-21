#ESCREVA UM PROGRAMA QUE PERGUNTE O SALARIO DE UM FUNCIONARIO E CALCULE O VALOR DO SEU AUMENTO.
#PARA SALARIOS SUPERIORES A R$1250.00, CALCULE UM AUMENTO DE 10%
#PARA OS INFERIORES OU IGUAIS, O AUMENTO E DE 15%

s = float(input('Qual e o seu salario? '))
if s <= 1250:
    print('Voce recebeu reajuste de 15%, seu novo salario e: ${}'.format(s+(s*15/100)))
else:
    print('Voce recebeu reajuste de 10%, seu novo salario e: ${}'.format(s+(s*10/100)))