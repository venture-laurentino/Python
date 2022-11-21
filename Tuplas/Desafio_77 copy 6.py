#CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VARIAS PALAVRAS (NAO USAR ACENTOS).
#DEPOIS DISSO, VOCE DEVE MOSTRAR, PARA CADA PALAVRA, QUAIS SAO AS SUAS VOGAIS.

palavras = 'JOGOS', 'MAQUINAS', 'COMPUTADOR', 'TECLADO', 'MOUSE'

for p in palavras:
    print(f'\nNa palavra {p} temos: ', end=' ')
    for letra in p:        
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')