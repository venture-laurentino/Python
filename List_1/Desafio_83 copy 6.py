#CRIE UM PROGRAMA ONDE O USUARIO DIGITE UMA EXPRESSAO QUALQUER QUE USE PARENTESES.
#SEU APLICATIVO DEVERA ANALISAR SE A EXPRESSAO PASSADA ESTA COM OS PARENTESES ABERTOS E FEHCADOS NA ORDEM CORRETA

exp = str(input('Digite a expressao: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha == 0):
    print('Sua expressao esta correta')
else:
    print('Sua expressao esta incorreta')