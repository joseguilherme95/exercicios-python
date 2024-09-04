#   Faça um programa que tenha uma função chamada escreva()
#   que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavél


def escreva(msg):
    tam = len(msg) + 4
    print('~'* tam)
    print(f'  {msg}')
    print('~'* tam)
    print()


#Programa Principal
escreva('José Guilherme')
escreva('Ciêntista de Dados em 2023')
escreva('José-guilherme@outlook.com.br')
