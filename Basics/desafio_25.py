#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM 'SILVA' NO NOME

nome = str(input('Qual o seu nome: '))
print ('O nome possui Silva ? {}'.format('SILVA'in nome.upper())) #podemos utilizar o .upper ou .lower dependendo da busca , para q o programa converta todas as letras para identificar se o nome existe indepente das letras maiusculas ou minusculas
