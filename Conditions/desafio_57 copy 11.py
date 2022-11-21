#FACA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SO ACEITE OS VALORES 'M' OU 'F'.
#CASO ESTEJA ERRADO, PECA A DIGITACAO NOVAMENTE ATE TER UM VALOR CORRETO.

s = str(input('Digite o sexo: ')).upper()
while s != 'M' and s != 'F':
    s = str(input('Valor invalido.\nDigite novamente: '))
if s == 'M':
    print (f'Voce digitou ({s}): Masculino.')
else:
    print(f'Voce digitou ({s}): Feminino.')