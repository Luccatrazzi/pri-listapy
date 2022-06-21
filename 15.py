#recebendo valores
tipo=input('Digite o numero correspondente: (1: Residência, 2: Comércio ou 3: Indústria) ?')
kw=input('KW/h consumido? ')
total = 0

if int(tipo) == 1:
  total = int(kw) * 1,29
  print('R$',total)
elif int(tipo) == 2:
  total = int(kw) * 0,60
  print('R$',total)
elif int(tipo) == 3:
  total = int(kw) * 0,48
  print('R$',total)
