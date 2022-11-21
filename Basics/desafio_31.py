#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAGEM EM km E CALCULE O PRECO DA PASSAGEM, COBRANDO R$0.50 POR KM PARA VIAGENS ATE 200km E R$0.45 PARA VIAGENS MAIS LONGAS.

dist = float(input('Qual a distancia voce vai percorrer? '))
if dist <= 200:
    print ('Voce ira pagar: ${}'.format(dist*0.5))
else:
    print ('Voce ira pagar: ${}'.format(dist*0.45))