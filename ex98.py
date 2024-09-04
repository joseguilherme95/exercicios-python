#   FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO  CHAMADA CONTADOR () QUE RECEBA 3 PARÂMETROS: INICIO, FIM, E PASSO
#   E REALIZE A CONTAGEM, SEU PROGRAMA TEM QUE REALIZAR 3 CONTAGENS ATRAVÉS DA  FUNCAO CRIADA
#   DE 1 ATE 10, DE 1 EM 1
#   DE 10 ATÉ 0, DE 2 EM 2
#   UMA CONTAGEM PERSONALIZADA
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'=-'*20)
    print(f'Contagem de {i} até o {f} de {p} em {p}')
    sleep(2)

    if i < f:
        c = i
        while c <= f:
            print(f'{c} ', end='')
            sleep(0.5)
            c += p
        print(f'FIM')

    else:
        c = i
        while c >= f:
            print(f'{c} ', end='')
            sleep(0.5)
            c -= p
        print('FIM')
    print(f'=-'*20)

contador(10, 2, 1)
contador(20, 100, 24)

print(f'Agora é a sua vez de personalizar a contagem !!')
ini = int(input('DIgite o inicio:   '))
fim = int(input('Digite o fim: '    ))
passo = int(input('Digite o passo:  '))

contador(ini, fim, passo)
