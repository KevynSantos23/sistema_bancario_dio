from classes.sistema import Sistema

sistema = Sistema()

class Conta():
         
    saldo = 0.0
    LIMITE_SAQUE = 500.0
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    operar = bool
    
                
        
    def operacao_deposito(self):
        
        print("__Depósito__")
        valor = float(input("Quanto você deseja depositar? "))
                
        if valor > 0:

            sistema.limpar_terminal()
            self.saldo += valor
            self.adicionando_extrato(valor, "Depósito")
            sistema.limpar_terminal()
            print(f"""\nDepósito realizado!
                             Seu saldo atual é: R$ {self.saldo}""")
            self.continuar_operando()

        else:
            sistema.limpar_terminal()
            print(f"""\nValor Inválido
                             Seu saldo atual é: R$ {self.saldo}""")
            self.continuar_operando()
            
            
        return 

    def operacao_sacar(self):

        print(self.saldo)
        valor = float(input("\nQuanto você deseja Sacar? ")) 

        validacao_valor = valor <= self.saldo and valor > 0 and valor <= self.LIMITE_SAQUE and self.numero_saques < self.LIMITE_SAQUES
        
        if validacao_valor:

            sistema.limpar_terminal()
            self.saldo -= valor
            self.numero_saques += 1
            self.adicionando_extrato(valor, "Saque")
            print(f"""\nSaque Realizado
                             Seu saldo atual é: R$ {self.saldo}""")

        elif valor > self.saldo:
            sistema.limpar_terminal()
            print("\nSaldo insuficiente")

        elif self.numero_saques >= self.LIMITE_SAQUES:
            sistema.limpar_terminal()
            print("\nVocê atingiu o limite de Saques diários!")

        else:
            sistema.limpar_terminal()
            print(f"""\nValor Inválido
                             Seu saldo atual é: R$ {self.saldo}""")
            
        return 
    
    def operacao_extrato(self):
        sistema.limpar_terminal()
        registro = reversed(self.extrato)
        
        print("""                               ____Extrato____\n""")
        print("""Data/Hora                     Valor            Operação\n""")
        for x in registro:
            print(f"""{x['data_hora']}           {x['valor']}               {x['operacao']}""")
        
        self.continuar_operando()
        return
    
    def adicionando_extrato(self, valor, operacao):
        data_hora_registrada = sistema.data_hora()
        
        registro = {
            'data_hora': data_hora_registrada,
            'valor': valor,
            'operacao': operacao
        }
        
        self.extrato.append(registro)
        return
    
    def continuar_operando(self):
        
        while True:
            continuar_operando = input("""\nRealizar outra operação? [s]- Sim | [n] - Não\n""").upper()
            
            match continuar_operando:
                case "S":
                    sistema.limpar_terminal()
                    self.operar = True
                    break
                    
                case "N":
                    sistema.limpar_terminal()
                    self.operar = False
                    break
                    
                case _:
                    sistema.limpar_terminal()
                    print("\nOpção Inválida")
                
        return 
    