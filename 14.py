#recebendo hora/aula
nivel = input('Qual nível? (1,2 ou 3) ')
aula = input('Quantas horas de aula? ')
total = 0

#calculando
if int(nivel)  == 1:
  total = int(aula) * 12
  print("R$ ", total)
elif int(nivel)  == 2:
  total = int(aula) * 17
  print("R$ ", total)
elif int(nivel)  == 3:
  total = int(aula) * 25
  print("R$ ", total)