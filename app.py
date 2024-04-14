from operacoes import Operacoes
from sistema import Sistema

sistema = Sistema()
sistema.limpar_terminal()

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

    escolha_operacao = input(menu).upper()

    match escolha_operacao:

        case "D":
            sistema.limpar_terminal()
            print("Depósito")
            operacao_deposito = Operacoes(escolha_operacao, conta)
            conta["saldo"] = operacao_deposito.dados_conta["saldo"]
            print(f"\nNovo saldo R$ {conta['saldo']}")
            
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
