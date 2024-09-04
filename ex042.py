#   RRefaça o desafio do triangulo acrescentando o recurso de mostrar que tipo de triângulo será formado
#   EQUILÁTERO: TODOS OS LADOS IGUAIS.
#   ISOSCELES: DOIS LADOS IGUAIS.
#   ESCALENO: TODOS OS LADOS DIFERENTES.
print('TIPOS DE TRIANGULO !!!')

l1 = int(input('Insira o valor do lado: '))
l2 = int(input('Insira o valor do lado: '))
l3 = int(input('Insira o valor do lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('É POSSÍVEL FORMAR UM TRIANGULO')
    if l1 == l2 and l1 == l3:
        print('TRIANGULO EQUILÁTERO: TODOS OS LADOS IGUAIS !')
    elif l1 == l2 or l3 == l2 or l3 == l1:
        print('TRIANGULO ISOSCELES: DOIS LADOS IGUAIS !')
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print('TRIANGULO ESCALENO: TODOS OS LADOS DIFERENTES !!')
else:
    print('NÃO É POSSIVEL FORMAR UM TRIANGULO !!')

