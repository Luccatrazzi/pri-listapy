#lendo valores
valor1 = input("Digite um numero:")
valor2 = input("Digite outro numero:")
maior = 0

#verificando maior
if int(valor1) > int(valor2):
  maior = valor1
else:
  maior = valor2  

if int(valor1) == int(valor2):
  print('IGUAIS')
else:
  print('DIFERENTES!', maior, 'é maior')


