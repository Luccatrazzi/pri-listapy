#recebendo valores
nome=input('Digite seu nome:')
idade=input('Digite sua idade:')
sexo=input('Digite seu sexo: (F ou M)')

#verificando salario
if sexo == 'M' and int(idade) >= 30: 
  print(nome, 'seu salário é R$', 100 )
elif sexo == 'M' and int(idade) < 30:
  print(nome, 'seu salário é R$', 50 )
elif sexo == 'F' and int(idade) >= 30:
  print(nome, 'seu salário é R$', 200 )
elif sexo == 'F' and int(idade) < 30:
  print(nome, 'seu salário é R$', 80 )
