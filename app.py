menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

conta = {
    'saldo': 0.0,
    'limite': 500.0,
    'extrato': "",
    'numero_saques': 0,
    'LIMITE_SAQUES': 3
}

while True:

    operacao = input(menu).upper()

    match operacao:
        case "D":
            print("Depósito")
            print(f"Novo saldo R$ {conta['saldo']}")
        case "S":
            print("Saque")
            print()
        case "E":
            print("Extrato")
            print()
        case "Q":
            print("Sair")
            break
        case _:
            print("Opção inválida, por favor selecione novamente a operação desejada.")
