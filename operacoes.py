from datetime import datetime
from sistema import Sistema

sistema = Sistema()

class Operacoes ():
    def __init__(self, operacao, conta):

        self.nome_operacao = operacao
        self.dados_conta = conta
        self.data_operacao = datetime.now()

        match self.nome_operacao:

            case "D":
                
                
                valor = float(input("\nQuanto você deseja depositar? "))

                if valor > 0:

                    sistema.limpar_terminal()
                    self.dados_conta['saldo'] += valor
                    print("\nDepósito Realizado")

                else:
                    print("\nValor Inválido")
                    