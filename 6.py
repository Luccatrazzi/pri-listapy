#recebendo numero
valor = input('Digite um número:')

#varificando se é positivo, negativo ou nulo
if int(valor) > 0: 
  print('POSITIVO')
elif int(valor) == 0:
  print('NULO')
else:  
  print('NEGATIVO')