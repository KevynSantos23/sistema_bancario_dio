from classes.operacoes import Operacoes
from classes.sistema import Sistema

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
    'LIMITE_SAQUE': 500.0,
    'extrato': [],
    'numero_saques': 0,
    'LIMITE_SAQUES': 3
}
continuar_operando = True

while continuar_operando:

    escolha_operacao = input(menu).upper()
    operacoes = Operacoes(escolha_operacao, conta)

    match escolha_operacao:
            
        case "D":
            sistema.limpar_terminal()
            print("___Depósito___")
            operacoes.operacao_deposito()
            conta["saldo"] = operacoes.dados_conta["saldo"]
            

            continuar_operando = operacoes.continuar_operando()
            
            
            
        case "S":
            sistema.limpar_terminal()
            print("___Saque___")
            operacoes.operacao_sacar()
            conta["saldo"] = operacoes.dados_conta["saldo"]

            continuar_operando = operacoes.continuar_operando()

        case "E":
            print("Extrato")
            print()
        case "Q":
            print("Sair")
            break
        case _:
            print("Opção inválida, por favor selecione novamente a operação desejada.")
