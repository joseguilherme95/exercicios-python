#   Faça um programa que tenha uma função chama área() que receba as dimensoes de um terreno
#   retangular (largura e comprimento) e mostre a área do terreno

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')



# Programa principal
print(f'== Controle de Terrenos ==')
print(f'-='*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)