#FACA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO SUA IDADE:
#SE ELE AINDA VAI SE ALISTAR AO SERVICO MILITAR
#SE E A HORA DE SE ALISTAR
#SE JA PASSOU DO TEMPO DE ALISTAMENTO

#SEU PROGRAMA TMB DEVERA MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO

data = int(input('Ano de nascimento: '))
anobase = 2022
idade = anobase - data
if idade < 18:
    print(f'Voce tem {idade} anos e devera se alistar em {18-idade} ano/s')
elif idade == 18:
    print(f'Voce tem {idade} anos, ja e hora de se alistar')
else:
    print(f'Voce tem {idade} anos, ja passou {idade-18} anos do periodo de alistamento.\nVoce ja deve ter se alistado.\nCaso nao tenha, favor comparecer a junta militar mais proxima')