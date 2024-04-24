from classes.sistema import Sistema
from classes.conta import Conta

conta = Conta()
sistema = Sistema()
sistema.limpar_terminal()

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

continuar_operando = True

while continuar_operando:

    escolha_operacao = input(menu).upper()

    match escolha_operacao:
            
        case "D":
            sistema.limpar_terminal()
            conta.operacao_deposito()
            continuar_operando = conta.operar
            
        case "S":
            sistema.limpar_terminal()
            conta.operacao_sacar()
            continuar_operando = conta.operar

        case "E":
            sistema.limpar_terminal()
            conta.operacao_extrato()
            continuar_operando = conta.operar
            
        case "Q":
            print("Sair")
            break
        case _:
            print("Opção inválida, por favor selecione novamente a operação desejada.")
    