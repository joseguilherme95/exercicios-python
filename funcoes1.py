# ROTINA !!
# def -

#def mostralinha():
#    print('-='*30)

#mostralinha()
#print(f'Cadastro de Clientes')
#mostralinha()
#print(f'Erro !!')
#mostralinha()
#print(f'Sistema de Alunos')
#mostralinha()

#UTILIZANDO PARAMETROS
#def mensagem(msg):
#    print('=-'*30)
#    print(msg)
#    print('=-'*30)
#mensagem('Sistema de Alunos')

#def soma(a, b):
#    print(f'A = {a} e B = {b}')
#    s = a + b
#    print(f'A soma A + B = {s}')

#soma(b=2, a=1)
#soma(8, 6)
#soma(3, 5)
#soma(4, 7)

#EMPACOTAR PARAMETROS !!

#def contador(*núm):   # DIFERENCIAL !! USAR *NÚM para que você não precisa marcar os parâmetros corretamentes igual o exemplo acima.
#       *núm -> após especificar este parâmetro, você pode inserir quantos parâmetros quiser na chamada de função.
#    tam = len(núm)
#    print(f'Recebi os valores {núm} e são ao todo {tam} números')
#
#contador(4, 5, 6, 7)
#contador(1,2, 3)

# EXEMPLO
#TUDO QUE EU FIZER DENTRO DE LST SERÁ ALTERADO NA LISTA VALORES !!!!
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos += 1

valores = [5, 6, 8, 1, 15]
dobra(valores)
print(valores)