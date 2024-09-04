#Crie um programa que tenha uma tupla com várias palavras, depois disso voce deve mostrar para cada palavra quais são
# suas vogais

palavras = ('lapis', 'borracha', 'curso', 'teletom', 'muralha', 'escola')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')