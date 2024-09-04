#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente.

from math import sin, cos, tan, radians
angulo = float(input('Insira o valor do angulo: '))
angulo = radians(angulo)

seno = sin(angulo)
cos = cos(angulo)
tan = tan(angulo)

print(f'Valor do angulo: {angulo}')
print(f'Valor do seno: {seno}')
print(f'Valor do cosseno: {cos}')
print(f'Valor do tan: {tan}')



















#from math import sin, cos, tan, radians

#angulo = float(input('Insira o valor do angulo: '))
#angulo = radians(angulo)

#print(f'Valor do seno: {sin(angulo):.1f}')
#print(f'Valor do Cosseno: {cos(angulo):.1f}')
#print(f'Valor da tangente: {tan(angulo):.1f}')