
class Conta():
         
    contas = []
    conta_dados = {
        "tipo_conta": "none",
        "numero_conta": "none",
        "senha_conta": "none",
        "titular": "none",
        "cpf": "none",
        "saldo": 0.0,
        "LIMITE_SAQUE": 500.0,
        "extrato": [],
        "numero_saques": 0,
        "LIMITE_SAQUES": 3,
        "conta_ativa": False
    }
    
    def conta_gerar(self, cliente_dados):
        if cliente_dados['idade'] < 18:
            self.conta_dados["tipo_conta"] = "JUVENIL"
        else:
            self.conta_dados["tipo_conta"] = "ADULTO"
            
        sistema.limpar_terminal()
        self.conta_dados["numero_conta"] = self.conta_gerar_numero()
        print(f"O número da sua conta será: {self.conta_dados['numero_conta']}")
        print(f"Tipo: {self.conta_dados['tipo_conta']}")
        
        while True:
            try:
                sistema.limpar_terminal()
                senha_conta = int(input("""Crie sua senha da conta. (essa senha serve para operações bancárias)
                          
                          Critérios:
                        - 4 digitos
                        - Apenas números
                        
                        Informe a senha: 
                        =>  """))
                senha_conta_confirmada = int(input("Confirme sua senha:"))
                    
                if senha_conta != senha_conta_confirmada:
                    sistema.limpar_terminal()
                    print("Inválido!\nA comfirmação foi diferente da senha informada\n")
                    continue
                elif senha_conta == senha_conta_confirmada:
                    senha_validada = sistema.validar_senha(senha_conta, "conta")
                    if senha_validada == True:
                        sistema.limpar_terminal()
                        self.conta_dados["senha_conta"] = senha_conta
                        print("Sua senha foi salva\n")
                        break
                    else:
                        sistema.limpar_terminal()
                        print("Sua senha não atende aos critérios\n")
                        continue
                    
            except ValueError:
                print("Inválido!\n")
                continue
        
        self.conta_dados["titular"] = cliente_dados["nome"]
        self.conta_dados["cpf"] = cliente_dados["cpf"]
        self.conta_exibir_dados()
        
        return
    
    def conta_exibir_dados(self):
        sistema.limpar_terminal()
        exibir_dados = print(f"""Seus dados
        
        Número da conta:                 {self.conta_dados["numero_conta"]}
        Tipo da conta:                   {self.conta_dados["tipo_conta"]}
        Titular:                         {self.conta_dados["titular"]}
        CPF:                             {self.conta_dados["cpf"]}
        Saldo:                           {self.conta_dados["saldo"]}
        Limite de saque:                 {self.conta_dados["LIMITE_SAQUE"]}
        Qtd de saques diários:           {self.conta_dados["LIMITE_SAQUES"]}
        Conta_ativa:                     {self.conta_dados["conta_ativa"]}
        """)
        
        return exibir_dados
    
    def conta_trazer_dados(self, cliente):
        for conta in self.contas:
            if conta["cpf"] == cliente:
                self.conta_dados = conta
        return
    
    def conta_editar_dados(self, chave, valor):
        self.conta_dados[f"{chave}"] = valor
        return
    
    def conta_salvar_dados(self):
        for conta in self.contas:
            if conta["cpf"] == self.conta_dados['cpf']:
                conta = self.conta_dados
        return
    
    
    def conta_desativar(self, cliente_dados):
        for conta in self.contas:
            if cliente_dados["cpf"] == conta["cpf"]:
                self.conta_trazer_dados(cliente_dados["cpf"])
                self.conta_dados["conta_ativa"] = False
        return
    
    def conta_gerar_numero(self):
        
        conta_numero = []
        
        for _ in range(7):
            numero_aleatorio = random.randint(0, 9)
            conta_numero.append(numero_aleatorio)
            
        conta_numero = ' '.join(map(str, conta_numero))
        conta_numero = conta_numero[:-1] + '-' + conta_numero[-1]
            
        return conta_numero
        
    def operacao_deposito(self):
        
        print("__Depósito__")
        valor = float(input("Quanto você deseja depositar? "))
                
        if valor > 0:

            sistema.limpar_terminal()
            self.conta_dados["saldo"] += valor
            self.adicionando_extrato(valor, "Depósito")
            sistema.limpar_terminal()
            print(f"""\nDepósito realizado!
                             Seu saldo atual é: R$ {self.conta_dados["saldo"]}""")
            self.continuar_operando()

        else:
            sistema.limpar_terminal()
            print(f"""\nValor Inválido
                             Seu saldo atual é: R$ {self.conta_dados["saldo"]}""")
            self.continuar_operando()
            
            
        return 

    def operacao_sacar(self):

        print(self.conta_dados["saldo"])
        valor = float(input("\nQuanto você deseja Sacar? ")) 

        validacao_valor = valor <= self.conta_dados["saldo"] and valor > 0 and valor <= self.conta_dados["LIMITE_SAQUE"] and self.conta_dados["numero_saques"] < self.conta_dados["LIMITE_SAQUES"]
        
        if validacao_valor:

            sistema.limpar_terminal()
            self.conta_dados["saldo"] -= valor
            self.conta_dados["numero_saques"] += 1
            self.adicionando_extrato(valor, "Saque")
            print(f"""\nSaque Realizado
                             Seu saldo atual é: R$ {self.conta_dados["saldo"]}""")

        elif valor > self.conta_dados["saldo"]:
            sistema.limpar_terminal()
            print("\nSaldo insuficiente")

        elif self.conta_dados["numero_saques"] >= self.conta_dados["LIMITE_SAQUES"]:
            sistema.limpar_terminal()
            print("\nVocê atingiu o limite de Saques diários!")

        else:
            sistema.limpar_terminal()
            print(f"""\nValor Inválido
                             Seu saldo atual é: R$ {self.conta_dados["saldo"]}""")
            
        return 
    
    def operacao_extrato(self):
        sistema.limpar_terminal()
        registro = reversed(self.conta_dados["extrato"])
        
        print("""                               ____Extrato____\n""")
        print("""   Data/Hora                          Valor              Operação\n""")
        for x in registro:
            print(f"""{x['data_hora']}                  {x['valor']}                   {x['operacao']}""")
        
        self.continuar_operando()
        return
    
    def adicionando_extrato(self, valor, operacao):
        data_hora_registrada = sistema.data_hora()
        
        registro = {
            'data_hora': data_hora_registrada,
            'valor': valor,
            'operacao': operacao
        }
        
        self.conta_dados["extrato"].append(registro)
        return
    
    def continuar_operando(self):
        
        while True:
            try:
                continuar_operando = input("""\nRealizar outra operação? [s]- Sim | [n] - Não\n""").upper()
            
                match continuar_operando:
                    case "S":
                        sistema.limpar_terminal()
                        continuar_operando = True
                        break
                    
                    case "N":
                        sistema.limpar_terminal()
                        continuar_operando = False
                        break
            except ValueError:
                sistema.limpar_terminal()
                print("\nOpção Inválida")
        return continuar_operando
    