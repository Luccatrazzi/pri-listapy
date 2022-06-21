#recebendo valores
nome=input('Digite seu nome: ')
sexo=input('Digite seu sexo: (M ou F)')
altura=input('Digite seu altura: ')
idade=input('Digite sua idade: ')

peso = 0

if sexo == 'M' and float(altura) > 1.70:
  if int(idade) <=40:
    peso = (72.7* float(altura) -58)    
    print('Seu peso ideal é', round(peso, 1))
  else:
    peso = (72.7* float(altura) -45)    
    print('Seu peso ideal é', round(peso, 1))
elif sexo == 'M' and float(altura) <=1.70:
  if int(idade) >40:
    peso = (72.7* float(altura) -50)    
    print('Seu peso ideal é', round(peso, 1))
  else:
    peso = (72.7* float(altura) -58)    
    print('Seu peso ideal é', round(peso, 1))
elif sexo == 'F' and float(altura) >1.50:
    peso = (62.1* float(altura) -44.7)    
    print('Seu peso ideal é', round(peso, 1))
elif sexo == 'F' and float(altura) <=1.50:
  if int(idade) >=35:
    peso = (62.1* float(altura) -45)    
    print('Seu peso ideal é', round(peso, 1))
  else:
    peso = (62.1* float(altura) -49)    
    print('Seu peso ideal é', round(peso, 1))


