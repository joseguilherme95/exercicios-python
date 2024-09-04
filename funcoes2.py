#   help()  ->> Função !! Ajuda interativa
#
#help(input)

#   DOCSTRINGS   = """ 3 aspas duplas no começo da função !! as quais podem ser consultada pelo comando help !!
#                       como ajuda para uma função.


#   Parâmetros Opcionais:   def somar(a, b, c=0):
#                           def somar(a=0, b=0, c=0):


#   Escopo de variáveis
# Escopo Global -> A variável pode estar embaixo que ela funciona na função acima.
# Escopo Local -> Funciona apenas local, dentro da função.


#   global a -> irá utilizar a variável a de dentro da função como global.


#   Retornando valores !!
#   def somar(a=0, b=0, c=0):
#        s = a + b + c
#        return s
#
# r1 = somar(2, 3, 5)
# r2 = somar(2, 3)
#print(f'Meus resultados deram {r1} e {r2}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Insira um número: '))
if par(num):
    print(f'É par')
else:
    print(f'Não é par ')



# TESTANDO VARIAVEIS !!
#ef teste(b):
 #   global a
#    a = 8
#    b += 4
#    c = 2
#    print(f'A dentro vale {a}')
#    print(f'B dentro vale {b}')
#    print(f'C dentro vale {c}')

#a = 5
#teste(a)
#print(f'A fora vale {a}')