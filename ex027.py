#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
#Ex Ana maria de souza
#primeiro = Ana
nome = str(input('Insira o nome: ')).upper().split()
print(f'Nome Sobrenome: {nome[0]} {nome[0-1]}')





















#Ultimo = souza

nome = str(input('Insira o nome completo: ')).upper().strip().split()

print(f'Primeiro nomee: {nome[0]}')
print('Ultimo nome: {} '.format(nome[len(nome) -1]))