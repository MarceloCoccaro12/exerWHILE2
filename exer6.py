lista=[]

for i in range(6):
     num=int(input("Digite um número par:"))

     if(num % 2 == 0):
          lista.append(num)
     
     if lista:
          soma= sum(lista)

print("Números da lista:", lista)
print("Soma dos números da lista:", soma)