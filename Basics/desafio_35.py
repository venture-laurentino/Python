#DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE 3 RETAS E DIGA AO USUARIO SE ELAS PODEM OU NAO FORMAR UM TRIANGULO.

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR trinagulo.')
else:
    print('Os segmentos acima NAO PODEM FORMAR TRIANGULO')
