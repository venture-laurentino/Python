#REFACA O DESAFIO 051, LENDO O PRIMEIRO TERMO E A RAZAO DE UMA PA,
#MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSAO USANDO A ESTRUTURA WHILE

t = int(input('Primeiro termo: '))
r = int(input('Razao: '))
d = t + (10-1) * r                  # <---- formula para o decimo termo
while d > 0:
    print(d, end = ' -- ' )
    break

