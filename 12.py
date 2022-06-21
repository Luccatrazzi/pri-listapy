#recebendo valores
num1=input('Digite o primeiro número: ')
num2=input('Digite o segundo número: ')
num3=input('Digite o terceiro número: ')

#adicionando lista e ordenando
array=[int(num1), int(num2), int(num3)] 
array.sort()
print(array[0], array[1], array[2])
