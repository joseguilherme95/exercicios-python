#Desenvolva um programa que leia o primeiro termo e a razão de uma pa, no final mostre os 10 primeiros termos desta p.a

p1 = int(input('Digite o primeiro termo de uma P.A: '))
razao = int(input('Qual será a razão da sua P.A: '))
termos = int(input('Quantos termos deseja que seja visto: '))
p10 = p1 + ((termos - 1) * razao)


for c in range(p1, p10+1, razao):
    print(c)





































#p1 = int(input('Insira o primeiro termo de uma P.A: '))
#razao = int(input('Insira a razão desta P.A: '))
#termo = int(input('Quantos termos quer procurar: '))
#p10 = p1 + ((termo - 1) * razao)
#for c in range(p1, p10+1 , razao):
#    print(c)