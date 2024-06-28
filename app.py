from classes.sistema import Sistema
from classes.conta import Conta
from classes.cliente import Cliente


conta = Conta()
cliente = Cliente()
sistema = Sistema()
sistema.limpar_terminal()

boas_vindas = """

Bem vindo ao Sistema Bancario da Dio

    Selecione uma opção:

    [L] - Fazer login
    [C] - Cadastro
    [Q] - Sair

=> """
menu = """

Sistema Bancario da Dio

    Selecione uma opção:

    [P] - Ver perfil
    [O] - Operar
    [Q] - Sair

=> """
operacao = """
Escolha a operação:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
perfil = """
Sistema Bancario da Dio

    Dados da sua conta:


=> """

while True:
    try:
        escolha_operacao = input(boas_vindas).upper()
    
        match escolha_operacao:
            
            case "L":
                login = cliente.cliente_login()
                if login[0] == "validado" and login[1] == "ativo":
                    sistema.limpar_terminal()
                    break
                    
                elif login[0] == "validado" and login[1] == "inativo":
                    sistema.limpar_terminal()
                    while True:
                        try:
                            print("Verificamos que voçê não possui conta corrente ativa.")
                            escolha = input("""Deseja ativa sua conta corrente?
                                            [S] - Sim | [N] - Não""").upper()
                            match escolha:
                                case "S":
                                    conta.conta_ativar(cliente.cliente_dados['cpf'])
                                case "N":
                                    break
                        except ValueError:
                            sistema.limpar_terminal()
                            print("Opção inválida, por favor selecione novamente a operação desejada.\n")
                            continue
                else:
                    sistema.limpar_terminal()
                    print(f"{login}\nCrie sua conta")
                    continue
                            
                        
            case "C":
                sistema.limpar_terminal()
                print("____Cadastro____\n")
                cliente.cliente_cadastro_form()
                sistema.limpar_terminal()
                print("     Seu dados")
                cliente.cliente_exibir_dados()
                while True:
                    try:
                        escolha= input("Deseja ativar sua conta corrente? [S] - sim | [N] - Não").upper()
                        match escolha:
                            case"S":
                                conta.conta_ativar(cliente.cliente_dados['cpf'])
                                break
                            case"N":
                                break
                    except ValueError:
                        sistema.limpar_terminal()
                        print("Opção inválida, por favor selecione novamente a operação desejada.\n")
                        continue
                
            case "Q":
                sistema.limpar_terminal()
                print("Sair")
                exit()
    except ValueError:
        sistema.limpar_terminal()
        print("Opção inválida, por favor selecione novamente a operação desejada.\n")
        continue

while True:
    try:
        menu_escolha = input(menu).upper()
        match menu_escolha:
            case"P":
                sistema.limpar_terminal()
                print("     Seu dados")
                cliente.cliente_exibir_dados()
                break
                
            case"O":
                break
            
            case"Q":
                sistema.limpar_terminal()
                print("Sair")
                exit()
        
    except ValueError:
        sistema.limpar_terminal()
        print("Opção inválida, por favor selecione novamente a operação desejada.\n")
        continue
    