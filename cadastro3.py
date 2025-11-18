cadastro = []

for i in range(1):
    nome = input("Digite um nome: ")
    idade = int(input("Digite a idade: "))
    cidade = input(("Digite o nome da sua cidade: "))
    cadastro.append({"nome": nome, "idade": idade, "cidade": cidade})
    
print("\nLista de cadastrados: ") 
for pessoa in cadastro:
    print(pessoa["nome"], "-",pessoa["idade"], "Anos","-", pessoa["cidade"])
    print("Seja Bem Vindo (a)!")