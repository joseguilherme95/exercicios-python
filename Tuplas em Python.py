#           Variáveis Compostas
#   3 tipos - tuplas, listas, dicionários.
#
#   print(lanche[-1]) = Mostra o último elemento da lista primeiro
#   len(lanche) - para saber. len = comprimento.
#
#   TUPLAS SÃO IMUTÁVEIS !! = NÃO DA PRA ALTERAR A VÁRIÁVEL ENQUANTO O PROGRAMA ESTIVER RODANDO.
#
#   lanche = () tupla
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#print(len(lanche))
#
#for cont in range(0, len(lanche)):
#   print(lanche[cont])

#for comida in lanche:
#   print(f'eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
#
#  A SOMA DE TUPLAS SOMENTE COLA, NÃO É REALIZADA OPERAÇÃO MATEMATICAS NAS MESMAS.
# print(c.count(5)) = ver quantas vezes o numero 5 aparece
# print(c.index(8)) = index = qual posição está o elemento 8.
# print(c.index(5, 1)) = procurando o 5 apartir da posição 1 e não da 0.
# del(lanche) = Apaga a tupla.
#
#
