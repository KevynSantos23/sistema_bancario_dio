from datetime import datetime
from classes.sistema import Sistema

sistema = Sistema()

class Operacoes ():
    def __init__(self, operacao, conta):

        self.nome_operacao = operacao
        self.dados_conta = conta
        self.data_operacao = datetime.now()

    def operacao_deposito(self,):
                
        valor = float(input("\nQuanto você deseja depositar? "))

        if valor > 0:

            sistema.limpar_terminal()
            self.dados_conta['saldo'] += valor
            print("\nDepósito Realizado")
            print(f"\nNovo saldo: R$ {self.dados_conta['saldo']}")

        else:
            sistema.limpar_terminal()
            print("\nValor Inválido")
            print(f"\nSeu saldo atual é: R$ {self.dados_conta['saldo']}")
            
        return self.dados_conta

    def operacao_sacar(self):

        valor = float(input("\nQuanto você deseja Sacar? ")) 

        valor_validacao = valor <= self.dados_conta['saldo'] and valor > 0 and valor <= self.dados_conta['LIMITE_SAQUE']
        limite_validacao = self.dados_conta['numero_saques'] < self.dados_conta['LIMITE_SAQUES']
        limite_atingido = self.dados_conta['numero_saques'] >= self.dados_conta['LIMITE_SAQUES']

        if valor_validacao and limite_validacao:

            sistema.limpar_terminal()
            self.dados_conta['saldo'] -= valor
            self.dados_conta['numero_saques'] += 1
            print("\nSaque Realizado")
            print(f"\nSeu saldo atual é: R$ {self.dados_conta['saldo']}")

        elif valor > self.dados_conta['saldo']:
            sistema.limpar_terminal()
            print("\nSaldo insuficiente")

        elif limite_atingido:
            sistema.limpar_terminal()
            print("\nVocê atingiu o limite de Saques diários!")

        else:
            sistema.limpar_terminal()
            print("\nValor Inválido")
            print(f"\nSeu saldo atual é: R$ {self.dados_conta['saldo']}")
            
        return self.dados_conta

    def continuar_operando(self):
        resposta = bool
        
        while True:
            continuar_operando = input("""\nRealizar outra operação? [s]- Sim | [n] - Não\n""").upper()
            
            match continuar_operando:
                case "S":
                    sistema.limpar_terminal()
                    resposta = True
                    break
                    
                case "N":
                    sistema.limpar_terminal()
                    resposta = False
                    break
                    
                case _:
                    sistema.limpar_terminal()
                    print("\nOpção Inválida")
                
        return resposta
            