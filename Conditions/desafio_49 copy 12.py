#REFACA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NUMERO QUE O USUARIO ESCOLHER, SO QUE AGORA ITILIZANDO UM LACO FOR.

num = int(input('Digite um numero: '))
print('''ADD - ADICAO
SUB - SUBTRACAO
MULT - MULTIPLICACAO
DIV - DIVISAO''')
typ = str(input('Operacao: ')).lower()

print('=-'*7)
for c in range(1,11):
    if typ == 'add':
        print(f'{num} + {c} = {num+c}')
    if typ == 'sub':
        print(f'{num} - {c} = {num-c}')
    if typ == 'mult':
        print(f'{num} x {c} = {num*c}')
    if typ == 'div':
        print('{} / {} = {:.2f}'.format(num, c, num/c))
print('=-'*7)