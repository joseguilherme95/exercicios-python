# Listas utilizam-se []
# lista = ['Pão', 'Manteiga', 'Queijo', 'Brocolis']
# lista.append('Amendoim') #-> Adicionando um elemento a lista.
# lista.insert(0,'xuxu') # -> Inseri um objeto na posição desejada da lista

# del(lista[0]) # -> apaga um objeto da lista !!!
# lista.pop(1) #Utilizado para apagar algum elemento da lista.
# lista.remove('Amendoim') #Metodo utilizado também para remover um item da lista.
# print(lista)
#
#
# valores = [8,2,5,4,9,3,0] -> criar uma lista com estes valores.
# valores.sort() -> ordenar a lista.
# valores.sort(reverse=True) -> ordenar a lista de forma reversa
# len(valores) -> contar o tamanho da lista(elementos).

## APARTIR DO MOMENTO QUE IGUALO UMA LISTA A OUTRA O PYTHON CRIA UMA LIGAÇÃO ENTRE ELAS. O VALOR É ALTERADO NAS DUAS.
# B = a[:] -> DESTE MODO ELE CRIA APENAS UMA CÓPIA E NÃO CRIA UMA LIGAÇÃO ENTRE OS DOIS.
#
#
lista = []
lista.append(4)
lista.append(6)
lista.append(8)
#for v in lista:
#    print(f'Os valores são: {v}')
#for c, v in enumerate(lista):   # -> enumerate procura o elemento em sua casa de origem..
#    print(f'Na posição {c} encontrei o valor: {v}')

#valores = []
#for cont in range (0, 5):
#    valores.append(int(input('insira um valor na lista: ')))
#
#for c, v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}')