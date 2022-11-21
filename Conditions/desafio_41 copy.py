#A CONFEDERACAO NACIONAL DE NATACAO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE:
#ATE 9 ANOS: MIRIM
#ATE 14 ANOS: INFANTIL
#ATE 19 ANOS: JUNIOR
#ATE 20 ANOS: SENIOR
#ACIMA: MASTER

data = int(input('Ano de nascimento: '))
anobase = 2022
idade = anobase - data

if idade <= 9:
    print(f'Voce tem {idade} anos e pertence a categoria MIRIM')
elif idade >9 and idade <=14:
    print(f'Voce tem {idade} anos e pertence a categoria INFANTIL')
elif idade >14 and idade <=19:
    print(f'Voce tem {idade} anos e pertence a categoria JUNIOR')
elif idade == 20:
    print(f'Voce tem {idade} anos e pertence a categoria SENIOR')
else:
    print(f'Voce tem {idade} anos e pertence a categoria MASTER')