#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
# calcule e mostre o comprimento da hipotenusa

from math import hypot, radians

co = float(input('Insira o cateto oposto: '))
ca = float(input('Insira o cateto adsjacente: '))
hypot = hypot(ca, co)

print(f'Hypotenusa: {hypot}')
























#from math import hypot, radians


#cata = float(input('Insira o cateto adsjacente: '))
#cato = float(input('Insira o cateto Oposto: '))

#hy = hypot(cata, cato)
#print(hy)