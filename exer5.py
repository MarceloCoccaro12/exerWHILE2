soma=0

for num in range(1,501,2):
    if(num % 3 == 0):
        soma += num
    print(num)
print("Soma dos intervalos:", soma)