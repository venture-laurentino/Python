#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
#SE ELE ULTRAPASSAR 80km/h, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
#A MULTA VAI CUSTAR R$7,00 POR CADA Km ACIMA DO LIMITE

import random
vel = float(random.randint (0,150))
print ('Velocidade alcancada: ',vel)
if vel <= 80:
    print ('Voce esta dentro do limite de velocidade')
else:
    print ('Voce esta rapido de mais, tome um presentinho no valor de ${:.2f}'.format((vel-80)*7))