menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).upper()

    match opcao:
        case "D":
            print("Depósito")
        case "S":
            print("Saque")
        case "E":
            print("Extrato")
        case "Q":
            print("Sair")
            break
        case _:
            print("Opção inválida, por favor selecione novamente a operação desejada.")
