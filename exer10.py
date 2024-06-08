pesos=[]

for i in range(5):
    peso=float(input(f"Digite o peso da {i+1}ª pessoa:"))
    pesos.append(peso)

peso_maior= max(pesos)
peso_menor= min(pesos)

print("Maior peso:", peso_maior)
print("Menor peso:", peso_menor)