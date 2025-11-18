opcao = 0 

while opcao != 4:
    print("\n======MENU======")
    print("1 - Dizer olá")
    print("2 - Somar dois números")
    print("3 - Contar até 5")
    print("4 - Sair")
    
    opcao = int (input("Escolha uma opção: "))
if opcao == 1:
        nome = input("Qual o seu nome: ")
        print("Olá", nome, "Seja bem vindo (a)!")
        
elif opcao == 2:
    a = int(input("Digite o primeiro numero: "))
    a = int(input("Digite o segundo numero: "))
    print("A soma é: ", a + b)
    
elif opcao == 3: 
    for i in range(1,6):
        print(i)
        
elif opcao == 4:
    print("Saindo do sistema...")
    
else:
    print("Opção inválida. Tente novamente ")
    
    
    