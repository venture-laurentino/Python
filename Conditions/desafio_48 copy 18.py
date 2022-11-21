#FACA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NUMEROS IMPARES QUE SAO MULTIPLOS DE TRES E QUE SE ENCONTRAM NO INTERVALO DE 1 ATE 500.

s = 0
cont = 0
for c in range(1,501,2):
    if c % 3 ==0:
        s += c
        cont += 1
print(f'A soma de todos os {cont} numeros impares multiplos de 3 foi: {s}')
