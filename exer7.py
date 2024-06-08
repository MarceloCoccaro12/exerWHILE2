a1=int(input("Digite o primeiro termo:"))
r=int(input("Digite a razão:"))

for i in range(10):

    an = a1 + i * r

    print(f"Termo {i+1}: {an}")