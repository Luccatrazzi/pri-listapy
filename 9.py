#lendo valores
combustivel = input('Digite o tipo de combustível do carro: (álcool, gasolina ou diesel)')
precoCarro = input('Digite o preço do carro:')
desconto = 0

#verificando valor do desconto
if combustivel == 'álcool' or combustivel == 'alcool':
  desconto = 0.25
elif  combustivel == 'gasolina':
  desconto = 0.21
else:
  desconto = 0.14

#calculando preço final
descontFinal = int(precoCarro) * desconto
precoFinalCarro = int(precoCarro) - descontFinal
print('O carro é', precoCarro, '. Mas com o desconto de', round(desconto*100, 2), '%' + ' ele sai por ', precoFinalCarro  )