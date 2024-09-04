#   Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa.
#   o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
#   calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então
#   o empreestimo será negado.






valor_casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário?: '))
anos = int(input('Em quantos anos deseja pagar? '))
meses = anos * 12
salario_30 = (salario * 30) / 100
prestacao = (valor_casa / meses)

if prestacao > salario_30:
    print('O EMPRESTIMO FOI NEGADO !!!')
else:
    print('Emprestimo concedido com sucesso !!')









#print(prestacao, salario_30)x = (10 * '-=')
#print(f'{x}BANCO-BND{x}')
#valor_casa = float(input('Insira o valor da Casa: '))
#salario = float(input('Qual é o seu salário? '))
#anos = int(input('Quantos anos gostaria de pagar a casa? '))
#salario_30 = (salario * 30) / 100
#meses = (anos * 12)
#prestacao = (valor_casa / meses)
#
#if prestacao > salario_30:
#    print('REPROVADO, PRESTAÇÃO ACIMA DE 30% DO SALÁRIO!')
#elif prestacao < salario_30:
#    print('APROVADO, VOCÊ PODE FAZER A COMPRA DA CASA !')
#else:
 #   print('Deseja algo mais ? ')
