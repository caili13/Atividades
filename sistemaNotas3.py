media = float(input("Digite a média final do aluno: "))

if media >= 9.0:
    conceito = "A"
elif media >= 8.0:
    conceito = "B"
elif media >= 7.0:
    conceito = "C"
elif media >= 6.0:
    conceito = "D"
else:
    conceito = "E"

print(f"O conceito do aluno é: {conceito}")
