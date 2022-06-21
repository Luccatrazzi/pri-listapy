a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
c = int(input("Digite o terceiro valor:"))

maior = a


if b > a and b > c:
    maior = b
    if a + c > b:
      print('Triangulo existe')
    else:  
      print('Triangulo não existe')
if c > a and c > b:
    maior = c
    if a + b > c:
      print('Triangulo existe')
    else:  
      print('Triangulo não existe')

menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c


