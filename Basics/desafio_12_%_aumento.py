#FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO

s = float(input ('Valor do salario: $ '))
p = s + (s * 15 / 100)
#v = p+s
#p = 15/100
#a = p*s

print ('Parabens, voce recebeu um aumento de 15%\nSeu novo salario e ${}' .format (p))