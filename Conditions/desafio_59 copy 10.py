#CRIE UM PROGRAMA QUE LEIA 2 VALORES E MOSTRE UM MENU NA TELA:
#[1]SOMAR
#[2]MULTIPLICAR
#[3]MAIOR
#[4]NOVOS NUMEROS
#[5]SAIR DO PROGRAMA

#SEU PROGRAMA DEVERA REALIZAR A OPERACAO SLICITADA EM CADA CASO
print('=-'*15)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
print('=-'*15)
while op != 5:
    op = (int(input('''Escolha uma das opcoes a seguir:
[1]SOMAR
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NUMEROS
[5]SAIR DO PROGRAMA
Digite a opcao desejada: ''')))
    print('=-'*15)
    if op == 1:
        print(f'Voce selecionou SOMAR: {n1} + {n2} = {n1+n2}')
        print('=-'*15)
    elif op == 2:
        print(f'Voce selecionou MULTIPLICAR: {n1} x {n2} = {n1*n2}')
        print('=-'*15)
    elif op == 3:
        if n1 > n2:
            print(f'Voce selecionou MAIOR: {n1}')
            print('=-'*15)
        else:
            print(f'Voce selecionou MAIOR: {n2}')  
            print('=-'*15)  
    elif op == 4:
        print('Informe os novos numeros.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=-'*15)
print('FIM DO PROGRAMA.')
print('=-'*15)


