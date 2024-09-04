#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado.
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$ 60,00 por dia e R$0.15 por km rodado.


km = float(input('Quantos km foram percorridos?: '))
dias = int(input('Quantos dias o carro foi alugado?: '))
dia = dias * 60
km_rodado = km * 0.15
print(f'O total a pagar é de {dia + km_rodado}')

























#km = float(input('Qual a kilometragem rodada ? '))
#dias = int(input('Quantidade de dias utilizado? '))
#preco_km = km * 0.15
#preco_dia = dias * 60

#print(f'O preço por km rodado é de {preco_km} e o preço por dia é de {preco_dia}')
#print(f'Total de R${preco_dia + preco_km:.1f}')