import os

ARQUIVO = "usuarios.txt"

ADMIN_USUARIO = "admin"
SENHA = "1234"


def carregar_usuarios():
    usuarios = []
   
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, idade = linha.strip().split(";")
                usuarios.append({"nome": nome, "idade": idade})
    return usuarios


def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for u in usuarios:
            arquivo.write(f"{u['nome']};{u['idade']}\n")


def mostrar_menu():
    print("\n---- MENU PRINCIPAL ----")
    print("1 - Cadastrar Usuário")
    print("2 - Listar Usuários")
    print("3 - Buscar Usuário")
    print("4 - Editar Usuário")
    print("5 - Excluir Usuário")
    print("6 - Sair")
    print("-------------------------")


def login():
    print("---- LOGIN DO ADM ----")
    for tentativa in range(3):
        usuario = input("Usuário: ").strip()
        senha = input("Senha: ").strip()

        if usuario == ADMIN_USUARIO and senha == SENHA:
            print("Login realizado com sucesso!")
            return True
        else:
            print("Usuário ou senha incorretos.")
            tentativas_restantes = 2 - tentativa
            if tentativas_restantes >= 0:
                print(f"Tentativas restantes: {tentativas_restantes}")

    print("Tentativas esgotadas. Sistema bloqueado.")
    return False


if login():
    usuarios = carregar_usuarios()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome: ").strip()
            idade = input("Idade: ").strip()
            usuarios.append({"nome": nome, "idade": idade})
            salvar_usuarios(usuarios)
            print("Usuário cadastrado com sucesso!")

        elif opcao == "2":
            print("\n--- LISTA DE USUÁRIOS ---")
            for u in usuarios:
                print(f"Nome: {u['nome']} | Idade: {u['idade']}")

        elif opcao == "3":
            busca = input("Digite o nome a buscar: ").strip().lower()
            encontrados = [u for u in usuarios if busca in u['nome'].lower()]
            if encontrados:
                for u in encontrados:
                    print(f"Nome: {u['nome']} | Idade: {u['idade']}")
            else:
                print("Nenhum usuário encontrado.")

        elif opcao == "4":
            nome = input("Nome do usuário a editar: ").strip()
            for u in usuarios:
                if u['nome'].lower() == nome.lower():
                    u['nome'] = input("Novo nome: ").strip()
                    u['idade'] = input("Nova idade: ").strip()
                    salvar_usuarios(usuarios)
                    print("Usuário atualizado com sucesso!")
                    break
            else:
                print("Usuário não encontrado.")

        elif opcao == "5":
            nome = input("Nome do usuário a excluir: ").strip()
            for u in usuarios:
                if u['nome'].lower() == nome.lower():
                    usuarios.remove(u)
                    salvar_usuarios(usuarios)
                    print("Usuário removido com sucesso!")
                    break
            else:
                print("Usuário não encontrado.")

        elif opcao == "6":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")
