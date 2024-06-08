import math
num=0
resultado=0

while True:
    num=int(input("Digite um número:"))
    resultado=math.factorial(num)

    if(num > 0):
        print(f"O fatorial de {num} é igual a {resultado}")
    
    else:
        print("Não é possível calcular")

