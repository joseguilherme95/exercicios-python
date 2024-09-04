#Faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra 'a'
# em que posição ela aparece a primeira vez.
# em que posição ela aparece a última vez.


frase = str(input('Insira uma frase: ')).upper().strip()
xletraA = frase.count('A')
posicao1 = frase.find('A')
posicao2 = frase.rfind('A')

print(f'Letra a aparece {xletraA} vezes')
print(f'Aparece pela primeira vez na casa {posicao1 + 1}')
print(f'Aparece por ultimo na casa {posicao2}')













#frase = str(input('Insira uma frase: ')).upper().strip()
#letraa = frase.count('A')
#print(f'A letra "A" aparece {letraa} vezes')
#primeira = frase.find('A')
#print(f'A letra "A" aparece na {primeira + 1} casa')
#print('A letra "A" aparece por último na casa {}'.format(frase.rfind('A')))
