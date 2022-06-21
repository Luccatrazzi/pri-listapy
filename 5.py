#recebendo valores
precoCusto = input('Digite o preço de custo:')
precoVenda = input('Digite o preço de venda:')

#calculando o lucro ou prejuizo
lucroPreju = float(precoVenda) - float(precoCusto)

#exibindo valores
if lucroPreju > 0:
  print('Você teve um lucro de R$', round(lucroPreju, 2))
elif lucroPreju == 0:  
  print('Você não obteve lucro nem prejuízo')
else:
  print('Você teve um prejuízo de R$', round(lucroPreju, 2))
