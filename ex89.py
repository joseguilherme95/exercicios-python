#   Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#   no final mostre, um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
#   individualmente

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar ? [S/N]: '))
    if resp in 'nN':
        break
print('=-'*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno: 999 interrompe'))
    if opc == 999:
        print('finalizando...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

print(ficha)
print(f'ENTENDENDO: {len(ficha) -1}')