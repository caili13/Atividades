n1 = int(input("Digite nota 1: "))
n2 = int(input("Digite nota 2: "))
n3 = int(input("Digite nota 3: "))


media = (n1 + n2 + n3) / 3  

if media >= 7:
    situacao = "Aprovado"
elif media >= 4:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("Média:", media)
print("Situação:", situacao)