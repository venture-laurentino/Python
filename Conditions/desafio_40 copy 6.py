#CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MEDIA, MOSTRANDO UMA MSG NO FINAL, DE ACORDO COM A MEDIA ATINGIDA.
#ABAIXO DE 5 REPROVADO
#ENTRE 5 E 6.9 RECUPERACAO
#ACIMA OU IGUAL A 7 APROVADO

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1+n2)/2

if m < 5:
    print('Voce foi REPROVADO')
elif m >=5 and m <=6.9:
    print('Voce esta em RECUPERACAO')
else:
    print('Voce foi APROVADO')