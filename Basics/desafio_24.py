#CRIE UM PROGRAMAR QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMECA OU NAO COM A PALAVRA 'SANTO'

c = str(input('Cidade: ')).strip()
print(c[:5].upper() == 'SANTO') #apos inserir a quantidade de casas colocamos o == para determinar qual a palavra procuramos como se fosse o 'in'
#print ('Possui a palavra Santo ? {}'.format('Santo' in c )) #>>> usando o 'in'