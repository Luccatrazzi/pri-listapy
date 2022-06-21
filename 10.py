#Recebendo mes
mes = input('Digite o número do mês: (de 1 a 12)')

while int(mes) < 1 or int(mes) > 12:
  print('mes inválido')
  mes = input('Digite novamente:')

if int(mes) == 1:
  print('Janeiro')
elif int(mes) == 2:
  print('Fevereiro')
elif int(mes) == 3:
  print('Março')
elif int(mes) == 4:
  print('Abril')
elif int(mes) == 5:
  print('Maio')
elif int(mes) == 6:
  print('Junho')
elif int(mes) == 7:
  print('Julho')
elif int(mes) == 8:
  print('Agosto')
elif int(mes) == 9:
  print('Setembro')
elif int(mes) == 10:
  print('Outubro')
elif int(mes) == 11:
  print('Novembro')
elif int(mes) == 12:
  print('Dezembro')