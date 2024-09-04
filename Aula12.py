#   CONDIÇÕES ANINHADAS !! se senão

#   if carro.esquerda():
#      bloco1
#   elif carro.direita():
#       bloco2
#   elif carro.ré():
#       bloco3
#   else:
#       print('Mundo!!'

import pandas as pd

tabela = pd.read_csv(r"C:\Users\Jose Guilherme\Desktop\Gui\Intensivão Python\aula2\telecom_users.csv")

print(tabela)
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela.info())
#
#