#   Crie um programa que tenha uma função chamadad voto(), que vai receber como parametro o ano de nascimento
#   de uma pessoa, retornando um valor literal indicando se a pessoa tem voto negado, opcional, ou obrigatorio nas
#   eleicoes

from datetime import date

def voto(i):
    if i < 16:
        print(f' Voto Negado')
        print(f'Você tem  {idade} anos')
    elif i <= 60:
        print(f'Voto Obrigatório')
        print(f'Você tem {idade} anos')
    else:
        print(f'Voto Opcional')
        print(f'Você tem  {idade} anos')


ano_nascimento = int(input('Insira ano de nascimento: '))
idade = date.today().year - ano_nascimento
voto(idade)