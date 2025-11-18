print("=== Calculadora Simples ===")
print("Escolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação desejada: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == "1":
    resultado = num1 + num2
    operacao = "+"
elif opcao == "2":
    resultado = num1 - num2
    operacao = "-"
elif opcao == "3":
    resultado = num1 * num2
    operacao = "x"
elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
        operacao = "÷"
    else:
        print("Erro: divisão por zero não é permitida!")
        exit()
else:
    print("Opção inválida!")
    exit()

print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")