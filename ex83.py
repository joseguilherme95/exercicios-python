#   Crie um programa onde o usuario digite uma expressão qualquer que use parenteses, seu aplicativo deverá analisar se
#   a expressão passada está com os parenteses abertos e fechados na ordem correta
# MINHA SOLUCAO
expr = str(input('Digite a expressão: '))
pilha = []
aberto = 0
fechado = 0
for simb in expr:
    pilha.append(simb)
    if simb == '(':
        aberto += 1
    if simb == ')':
        fechado += 1
if aberto == fechado:
    print('Expressão correta !!')
else:
    print('Expressão não correta !!'
        )
print(pilha)

#SOLUCAO PROFESSOR
expr = str(input('Digite a expressão: '))
pilha = []
for simb in pilha:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está incorreta ')