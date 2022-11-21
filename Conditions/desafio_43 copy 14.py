#DESENVOLVA UMA LOGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE SEU IMC E MOSTRE SEU STATUS, DE ACORDO COM A TABELA ABAIXO:
#ABAIXO DE 18.5 - ABAIXO DO PESO
#ENTRE 18.5 E 25 - PESO IDEIAL
#25 ATE 30 - SOBREPRESO
#30 ATE 40 - OBESIDADE
#ACIMA DE 40 - OBESIDADE MORBIDA
#IMC = PESO/ALTURA²

peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso/(altura**2)

if imc <=18.5:
    print('Seu IMC e {:.2f}.\nSe cuide, voce esta abaixo do seu peso ideal.'.format(imc))
elif imc >18.5 and imc <=25:
    print('Seu IMC e {:.2f}.\nVoce esta no seu peso ideal.'.format(imc))
elif imc >25 and imc <=30:
    print('Seu IMC e {:.2f}.\nTome cuidado vc esta acima do peso.'.format(imc))
elif imc >30 and imc <=40:
    print('Seu IMC e {:.2f}.\nProcure um medico, voce esta com obesidade.'.format(imc))
else:
    print('Seu IMC e {:.2f}.\nProcure um medico urgentemente voce esta na fase de obseidade morbida'.format(imc))