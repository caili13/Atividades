# Constantes
AVIOES = 4
MAX_PASSAGEIROS = 857

# Variáveis globais
aviaoID = [0] * AVIOES
assentos = [0] * AVIOES
modelos = [""] * AVIOES
nomesAviao = [""] * AVIOES
reservasFeitas = [0] * AVIOES
passageiros = []
inicioAssentos = [0] * AVIOES
quantidade = 0


# Função para configurar aviões
def configurarAviao():
    global quantidade

    try:
        quantidade = int(input(f"Quantos aviões você deseja configurar? (Máximo de {AVIOES}): "))
    except ValueError:
        print("Valor inválido.")
        return

    if quantidade <= 0 or quantidade > AVIOES:
        print("Quantidade inválida!\n")
        return

    posicaoAtual = 0

    for i in range(quantidade):
        print(f"\n--- Cadastro do Avião {i + 1} ---")
        nomesAviao[i] = input("Qual o nome do avião? ")
        aviaoID[i] = i + 1
        try:
            assentos[i] = int(input("Quantos assentos o avião possui? "))
        except ValueError:
            print("Número inválido de assentos. Pulando avião...")
            continue

        if posicaoAtual + assentos[i] > MAX_PASSAGEIROS:
            print("Limite total de passageiros excedido! Encerrando cadastro...")
            quantidade = i
            break

        inicioAssentos[i] = posicaoAtual
        posicaoAtual += assentos[i]
        reservasFeitas[i] = 0

    print("\nConfiguração concluída.\n")


# Função para reservar assento
def reservarAssento():
    if quantidade == 0:
        print("Nenhum avião configurado ainda.\n")
        return

    print("\n--- Reservar Assento ---")
    for i in range(quantidade):
        print(f"{i + 1} - {nomesAviao[i]} ({assentos[i]} assentos)")

    try:
        escolha = int(input("Escolha o avião: ")) - 1
        if escolha < 0 or escolha >= quantidade:
            print("Avião inválido.\n")
            return
    except ValueError:
        print("Entrada inválida.\n")
        return

    if reservasFeitas[escolha] >= assentos[escolha]:
        print("Este avião está lotado!\n")
        return

    nome_passageiro = input("Nome do passageiro: ")
    passageiros.append({
        "aviao": nomesAviao[escolha],
        "nome": nome_passageiro
    })
    reservasFeitas[escolha] += 1
    print(f"Reserva realizada com sucesso para {nome_passageiro} no avião {nomesAviao[escolha]}.\n")


# Mostra o status dos aviões
def statusAviao():
    if quantidade == 0:
        print("Nenhum avião configurado.\n")
        return

    print("\n--- Status dos Aviões ---")
    for i in range(quantidade):
        if assentos[i] == 0:
            continue
        print(f"Avião: {nomesAviao[i]}")
        print(f"Assentos: {assentos[i]}")
        print(f"Reservas feitas: {reservasFeitas[i]}")
        print(f"Assentos disponíveis: {assentos[i] - reservasFeitas[i]}")
        print("-" * 30)
    print()


# Lista todas as reservas feitas
def reservas():
    if not passageiros:
        print("Nenhuma reserva realizada ainda.\n")
        return

    print("\n--- Reservas Efetuadas ---")
    for r in passageiros:
        print(f"{r['nome']} - Avião: {r['aviao']}")
    print()


# Função principal (menu)
def main():
    while True:
        print("------- Menu -------")
        print("1 - Configurar aviões e assentos")
        print("2 - Realizar uma reserva")
        print("3 - Listar status dos aviões")
        print("4 - Listar reservas efetuadas")
        print("5 - Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida!\n")
            continue

        if opcao == 1:
            configurarAviao()
        elif opcao == 2:
            reservarAssento()
        elif opcao == 3:
            statusAviao()
        elif opcao == 4:
            reservas()
        elif opcao == 5:
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida!\n")


# Execução do programa
if __name__ == "__main__":
    main()
