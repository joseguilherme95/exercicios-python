#Crie um programa que leia o nome completo de uma pessoa e mostre:
#   O nome com todas as letrras maiusculas.
#   O Nome com todas as letras minusculas
#   Quantas letras ao todo (sem considerar os espaços)
#   Quantas letras tem o primeiro nome.


nome = str(input('Insira o nome: '))

print(f'Maiuscula: {nome.upper()}')
print(f'Minuscula: {nome.lower()}')
print(f'Quantas letras ao todo: {len(nome) - nome.count(" ")}')
separa = nome.split()
print(f'Quantas letras o primeiro nome: {len(separa[0])}')


















#nome = str(input('Insira o nome: ')).strip()
#print(f'O nome em maíusculo: {nome.upper()}')
#print(f'O nome em minusculo: {nome.lower()}')
#print('O nome tem {} letras sem considerar os espaços'.format(len(nome) - nome.count(' ')))
#separa = nome.split()
#print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0]))#)