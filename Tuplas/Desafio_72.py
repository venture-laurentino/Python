#CRIE UM PROGRAMA QUE TENHA UM ATUPLA TOTLAMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSO, DE ZERO ATE VINTE
#SEU PROGRAMA DEVERA LER UM NUMERO PELO TECLADO ENTRE 0 E 20 E MOSTRA-LO POR EXTENSO

cont = 'Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'

fim = False

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if num >= 0 and num <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Voce digiou o numero {cont[num]}')


