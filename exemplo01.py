limiteDiario = 200

saldo = int(input("Digite o saldo bancário: "))
saque = int(input("Digite o valor do saque: "))

if saque <= saldo and saque <= limiteDiario:
    saldoFinal = saldo - saque
    print("Saque realizado com sucesso!")
    print("Saldo final é:", saldoFinal)
elif saque > saldo:
    print("Saque não permitido: saldo insuficiente.")
elif saque > limiteDiario:
    print("Saque não permitido: ultrapassa o limite diário.")
else:
    print("Nenhuma das ações será executada!")
