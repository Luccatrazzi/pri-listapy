#lendo idade
anoNascimento = input("Digite seu ano de nascimento: ")
anoAtual = input("Digite o ano atual: ")

#calculando idade
idade = int(anoAtual) - int(anoNascimento)

#verificando se é maior de idade
if idade >= 18:
  print('Você tem ', idade ,' anos e é maior de idade')
else:
  print('Você tem ', idade ,' anos e NÃO é maior de idade')

