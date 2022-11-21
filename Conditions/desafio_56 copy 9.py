#DESENVOLVA UM PROGROAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA, MOSTRE:

# A MEDIA DE IDADE DO GRUPO
# QUAL E O NOME DO HOMEM MAIS VELHO.
# QUANTAS MULHERS TEM MENOS DE 20 ANOS

p1 = str(input('Primeira pessoa: '))
ip1 = int(input('Idade: '))
sp1 = str(input('Sexo: ')).lower()
print('=-'*15)
p2 = str(input('Segunda pessoa: '))
ip2 = int(input('Idade: '))
sp2 = str(input('Sexo: ')).lower()
print('=-'*15)
p3 = str(input('Primeira pessoa: '))
ip3 = int(input('Idade: '))
sp3 = str(input('Sexo: ')).lower()

m_maior = p1
f_menor = 0

if ip1 > ip2 and ip1 > ip3 and sp1 == 'm':
    m_maior = p1
elif ip2 > ip1 and ip2 > ip3 and sp2 == 'm':
    m_maior = p2
elif ip3 > ip2 and ip3 > ip1 and sp3 == 'm':
    m_maior = p3

if ip1 < 20 and sp1 == 'f':
    f_menor += 1
if ip2 < 20 and sp2 == 'f':
    f_menor += 1
if ip3 < 20  and sp3 == 'f':
    f_menor += 1

m = (ip1+ip2+ip3)/3

print('A media de idade entre eles e {:.0f}'.format(m))
print('O nome do home mais velho e: ',m_maior)
print(f_menor, 'mulheres com menos de 20 anos')


