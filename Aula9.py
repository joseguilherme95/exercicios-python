# frase = 'Curso em Vídeo Python'
# ====== FATIAMENTO ======
#
#   frase[9:13] - Irá pegar da casa 9 até a casa 12.
#
#   frase[9:21:2] - começar no nove e parar no 21, pulando de 2 em 2
#
#   frase[:5] - Irá começar do 0 até o 4.
#
#   frase[15:] - até o final.
#
#   frase[9::3] - do 9 ate o final e pulando de 3 em 3.
#
#               ANALISANDO UMA STRING.
#   len{frase} - Qual o comprimento da frase.
#
#   frase.count{'o'} - contar quantas vezes aparece a letra 'o'
#
#   frase.count{'o', 0, 13} - Entre o caractere 0 ao caractere 12.
#
#   frase.find{'deo'} - procura a palavra 'deo' e mostra onde ele começa somente uma casa.
#
#   frase.find{'Android'} - retorna o valor -1, caso não exista o valor android na string.
#
#   'Curso' in frase - dentro da variavel frase existe a palavra curso ?  true or false.
#
# TRANSFORMAÇÃO
#
#   frase.replace{'Python', 'Android'} - Onde tiver python substitui por Android
#
#   frase.upper() - Letras em Maiúsculas.
#   frase.lower() - Letras em Mínusculos
#   frase.capitalize() - Todos os caracteres para minusculo e somente o primeiro caractere para maiusculo.
#   frase.title() - analisa quantas palavras têm e faz o capitalize em todas as palavras de início.
#
#                   REMOVENDO ESPAÇOS.
#   frase.strip() - Remove todos os espaços inuteis no inicio e do final da string.
#   frase.rstrip() - remove o espaço da direita(ultimos espaços)
#   frase.lstrip() - remove o espaço da esquerda.
#
#           DIVIDINDO STRING.
#   frase.split() - Divisão dentro da string onde tem espaço. gera uma lista de palavras com a string [0, 1, 2, 3]
#
#           JUNÇÃO !!
#   '-'.join(frase) - juntar todos os elementos de frase e usando o separador '-'.
#
#   