seconds=input('Digite o valor dos segundos: ')

minutes = int(seconds) / 60
hour = minutes / 60

if minutes < 60:
  print('0 horas,', int(minutes), 'minutos e', int(seconds)%60, 'segundos')
else:
  print(int(hour), 'horas', int(minutes)%60, 'minutos e', int(seconds)%60, 'segundos')  