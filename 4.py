#lendo valores
anoCarro = input('Digite o ano do carro:')
precoCarro = input('Digite o preço do carro:')
desconto = 0

#verificando valor do desconto
if int(anoCarro) > 1990:
  desconto = 0.12
else:
  desconto = 0.05

#calculando preço final
descontFinal = int(precoCarro) * desconto
precoFinalCarro = int(precoCarro) - descontFinal
print('O carro é', precoCarro, '. Mas com o desconto de', desconto*100, '%' + ' ele sai por ', precoFinalCarro  )