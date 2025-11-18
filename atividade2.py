valor = int(input("Digite o valor:"))

quantidade_notas = valor // 50
print("Quantidade de notas de 50:", quantidade_notas)
resto = valor % 50

quantidade_notas_20 = resto // 20
print("Quantidade de notas de 20:", quantidade_notas_20)
resto = resto % 20

quantidade_notas_10 = resto // 10
print("Quantidade de notas de 10:", quantidade_notas_10)
resto = resto % 10

quantidade_notas_5 = resto // 5
print("Quantidade de notas de 5:", quantidade_notas_5)
resto = resto % 5
150
if resto != 0:
    print("Não é possível sacar o valor exato com notas de 50, 20, 10 e 5.")