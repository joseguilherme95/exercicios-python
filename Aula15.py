# while true
#   if mato
#       passo
#   if buraco
#       pula
#   if moeda
#       pega
#   if trofeu
#       pula
#       break
#
s = 0
while True:
    n = int(input('Insira um número: '))
    if n == 999:
        break
    s += n
print('A soma dos números é {}'.format(s))