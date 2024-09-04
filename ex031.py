#Desenvolva um programa que pergunte a distancia de uma viagem em km.
#Calcule o preço da passagem cobrando 0,50 por km para viagens até 200km
# e 0,45 para viajens mais longas


dist = float(input('Qual a distancia da viagem ?: '))
viagem_50 = dist * 0.50
viagemmaior50 = dist * 0.45

if dist > 200:
    print(f'O valor da viagem ficará em {viagemmaior50}')
else:
    print(f'O valor da viagem ficará em {viagem_50}')



















#distancia = float(input('Qual será a distância da viagem?: '))

#f distancia <= 200:
#    print('Viagem abaixo de 200KM')
#    print('O valor da passagem será de: {} '.format(distancia * 0.50))
#else:
#    print('Viagem acima de 200KM')
#    print('O valor da passagem será de {}'.format(distancia * 0.45))