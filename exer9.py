from datetime import datetime

maior_idade=0
menor_idade=0

for i in range(3):
    ano_nascimento=int(input(f"Digite o ano de nascimento da {i+1}ª pessoa:"))

    idade= datetime.now().year - ano_nascimento

    if(idade >= 18):
        maior_idade += 1

    else:
        menor_idade += 1

print("Pessoas maiores de idade:", maior_idade)
print("Pessoas menores de idade:", menor_idade)