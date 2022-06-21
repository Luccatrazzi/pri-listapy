#recebendo valores
num = input('Digite um número de 1 a 5:')

#validando
if int(num) < 1 or int(num) > 5:
  print('Numero inválido!')
else:  
  print('Numero válido!')
  