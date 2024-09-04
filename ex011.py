#faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade
#de tinta necessária para pinta-la, sabendo que ccada litro de tinta pinta uma área de 2m²


largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
area = largura * altura
tinta = area / 2
print(f'A area é igual a: {area:0.0f} e será necessário {tinta:0.0f} Litros de tinta.')























#largura = float(input('Qual é largura da parede ? '))
#altura = float(input('Qual a altura da parede ? '))
#area = largura * altura
#tinta = area / 2
#print(f'São necessários {tinta}L de tinta para a pintura de {area}m² de área')
