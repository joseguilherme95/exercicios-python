#   Melhore o desafio 061 perguntando para o usuario se ele quer mostrar mais alguns termos.
#   O programa encerra quando ele disser que quer 0 termos.



p1 = int(input('Insira o primeiro termo de uma P.A: '))
r = int(input('Insira a razão da P.A: '))
termo = p1
total = 0
count = 1
mais_termos = 10

while mais_termos != 0:
    total += mais_termos
    while count <= total:
        print(termo)
        termo += r
        count += 1
        print('Pausa')
        mais_termos = int(input('Quantos termos mais deseja visualizar: '))