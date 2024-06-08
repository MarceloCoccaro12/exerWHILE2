soma_idades= 0 
idade_h_velho= 0
nome__h_velho= ""
mulheresmenos_20= 0

for i in range(5):
    nome= input("Digite seu nome:")
    idade= int(input("Digite sua idade:"))
    sexo= input("Digite seu sexo (M) ou (F):")

    soma_idades += idade

    if(sexo == "M") and (idade > idade_h_velho):
        idade_h_velho= idade
        nome__h_velho= nome
    
    if(sexo == "F") and (idade < 20):
        mulheresmenos_20+= 1

media= soma_idades / 5

print("A média de idade das pessoas é de:{:.1f}".format(media))
print(f"O homem velho se chama {nome__h_velho} e tem idade de {idade_h_velho} anos.")
print(f"Existem {mulheresmenos_20} menores de 20 anos")