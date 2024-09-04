#   Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
frase = str(input('Insira uma frase: ')).strip().upper()
palavras = frase.split()
print(palavras)
junto = ''.join(palavras)
#print(junto)
#print(f'Você digitou a frase: {junto}')
#inverso =''
#for letra in range(len(junto)-1, -1, -1 ):
#    inverso += junto[letra]
#if inverso == junto:
#    print('Temos um Palíndromo !')
#else:
#    print('A frase não é um palindromo.')
#print(inverso, junto)

print(len(junto))