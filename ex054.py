#   Crie um programa que leia o ano de nascimento de sete pessoas no final mostre quantas pessoas
#   ainda não atingiram a maioridade e quantas ja são maiores.

import datetime
ano_atual = datetime.date.today().year
print(ano_atual)
menor = 0
maior = 0
for c in range(1, 7):
    ano_nascimento = int(input('Insira o ano de nascimento: '))
    if ano_atual - ano_nascimento < 18:
        menor += 1
    elif ano_atual - ano_nascimento >= 18:
        maior += 1
print(f'{menor} Pessoas são menores de idade !')
print(f'{maior} pessoas são maiores de idade !')




