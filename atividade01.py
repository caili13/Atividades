cadastro = []

for i in range(3):
    nome = input("Digite um nome: ")
    idade = int(input("Digite a idade: "))
    cadastro.append({"nome": nome, "idade": idade})
    
print("\nLista de cadastrados: ") 
for pessoa in cadastro:
    print(pessoa["nome"], "-",pessoa["idade"], "Anos")