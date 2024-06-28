
class Cliente():

    clientes = []
    
    cliente_dados = {
        "index": 0,
        "nome": "none",
        "data_nascimento": "none",
        "idade": 0,
        "cpf": "none",
        "endereco": "none",
        "telefone": "none",
        "email": "none",
        "nome_responsavel": "none",
        "data_nascimento_responsavel": "none",
        "idade_responsavel": 0,
        "cpf_responsavel": "none",
        "telefone_responsavel": "none",
        "conta_corrente_ativa": False,
        "cliente_senha": ""
        }
        
    def cliente_ativar_conta(self, cliente_dados):
        for conta in self.contas:
            if cliente_dados == conta["cpf"]:
                self.conta_dados["conta_ativa"] = True
        return 
    
    def cliente_exibir_dados(self):
        exibir_dados = print(f"""
        
        Nome:                   {self.cliente_dados["nome"]}
        Nascimento:             {self.cliente_dados["data_nascimento"]}
        Idade:                  {self.cliente_dados["idade"]}
        CPF:                    {self.cliente_dados["cpf"]}
        Endereço:               {self.cliente_dados["endereco"]}
        Telefone:               {self.cliente_dados["telefone"]}
        Email:                  {self.cliente_dados["email"]}
        Nome responsavel:       {self.cliente_dados["nome_responsavel"]}
        Idade responsavel:      {self.cliente_dados["idade_responsavel"]}
        CPF responsavel:        {self.cliente_dados["cpf_responsavel"]}
        Telefone responsavel:   {self.cliente_dados["telefone_responsavel"]}
        \n""")
        
        return exibir_dados
    
    def cliente_cadastro_form(self):
        
        while True:
            nome = input("\nInsira seu nome completo:\n").upper()
            try:
                nome_validado = self.cliente_validar_form("nome", nome)
                if nome_validado == False:
                    sistema.limpar_terminal()
                    print("Inválido.\n")
                    continue
                else:
                    self.cliente_dados["nome"] = nome_validado
                    sistema.limpar_terminal()
                    break
            except ValueError:
                print("Inválido.\n")
                continue
                
        while True:
            data_nascimento = input("\nInsira sua data de nascimento (formato: DD/MM/AAAA): \n")
            data_nascimento_validado = self.cliente_validar_form("data_nascimento", data_nascimento)
                
            if data_nascimento_validado == False:
                sistema.limpar_terminal()
                print("Inválido.\n")
                continue
            else:
                data_atual = datetime.now()
                ano_atual = int(data_atual.strftime("%Y"))
                    
                if int(data_atual.strftime("%m")) >= int(data_nascimento_validado.strftime("%m")) and int(data_atual.strftime("%d")) >= int(data_nascimento_validado.strftime("%d")):
                    idade = (ano_atual - int(data_nascimento_validado.strftime("%Y")))
                else:
                    idade = (ano_atual - int(data_nascimento_validado.strftime("%Y"))) -1
                        
                sistema.limpar_terminal()
                confirmar_idade = str(input(f"Sua idade é {idade}?\n[S] - Sim | [N] - Não\n")).upper()
                if confirmar_idade == "S":
                    self.cliente_dados["data_nascimento"] = data_nascimento_validado
                    self.cliente_dados["idade"] = idade
                    sistema.limpar_terminal()
                    print("\nConfirmado")
                    break
                else:
                    continue
                
        while True:
            endereco = input("\nInsira seu endereço completo:\n").upper()
            try:
                endereco_validado = self.cliente_validar_form("endereco", endereco)
                if endereco_validado == False:
                    sistema.limpar_terminal()
                    print("Inválido.\n")
                    continue
                else:
                    self.cliente_dados["endereco"]= endereco_validado
                    sistema.limpar_terminal()
                    break
            except ValueError:
                sistema.limpar_terminal()
                print("Inválido.\n")
                continue
                
        while True:
            try:
                telefone = int(input(f"\nInsira seu telefone:\n! Apenas números (11 digitos)\n"))
                try:
                    telefone_validado = self.cliente_validar_form("telefone", telefone)
                    if telefone_validado == False:
                        continue
                    else:
                        self.cliente_dados["telefone"] = telefone_validado
                        sistema.limpar_terminal()
                        break
                except ValueError:
                    print("Inválido!\n")
                    continue
                    
                    
            except ValueError:
                    print("Inválido!\n")
                    continue
                
        while True:
            email = input("\nInsira seu email completo:\n")
            try:
                email_validado = self.cliente_validar_form("email", email)
            
                if email_validado == False:
                    sistema.limpar_terminal()
                    print("Inválido!\n")
                    continue
                else:
                    self.cliente_dados["email"]= email_validado
                    sistema.limpar_terminal()
                    break
            except ValueError:
                print("Inválido!\n")
                continue
        
        while True:
            cpf = input("\nInsira seu cpf:\n! Apenas números (11 digitos)\n")
            try:
                cpf_validado = self.cliente_validar_form("cpf", cpf)
                if cpf_validado == False:
                    print("Inválido!\n")
                    continue
                else:
                    self.cliente_dados["cpf"]= cpf_validado
                    sistema.limpar_terminal()
                    break
                
            except ValueError:
                    print("Inválido!\n")
                    continue

        if self.cliente_dados["idade"] < 18:
            while True:
                nome_responsavel = input("\nNome do responsavél: \n")
                try:
                    nome_responsavel_validado = self.cliente_validar_form("nome", nome_responsavel)
                    
                    if nome_responsavel_validado == False:
                        sistema.limpar_terminal()
                        print("Inválido.\n")
                        continue
                    else:
                        self.cliente_dados["nome_responsavel"]= nome_responsavel_validado
                        sistema.limpar_terminal()
                        break
                except ValueError:
                    sistema.limpar_terminal()
                    print("Inválido.\n")
                    continue
                
            while True:
                data_nascimento_responsavel = input("\nData de nascimento do responsavél (formato: DD/MM/AAAA): \n")
                data_nascimento_responsavel_validado = self.cliente_validar_form("data_nascimento", data_nascimento_responsavel)
                
                if data_nascimento_responsavel_validado == False:
                    sistema.limpar_terminal()
                    print("Inválido.\n")
                    continue
                else:
                    data_atual = datetime.now()
                    ano_atual = int(data_atual.strftime("%Y"))
                    
                    if int(data_atual.strftime("%m")) >= int(data_nascimento_responsavel_validado.strftime("%m")) and int(data_atual.strftime("%d")) >= int(data_nascimento_responsavel_validado.strftime("%d")):
                        idade = (ano_atual - int(data_nascimento_responsavel_validado.strftime("%Y")))
                    else:
                        idade = (ano_atual - int(data_nascimento_responsavel_validado.strftime("%Y"))) -1
                    
                    if idade > 18:
                        sistema.limpar_terminal()
                        confirmar_idade = str(input(f"A idade do responsavél é: {idade}?\n[S] - Sim | [N] - Não\n")).upper()
                        if confirmar_idade == "S":
                            self.cliente_dados["data_nascimento_responsavel"]= data_nascimento_responsavel_validado
                            self.cliente_dados["idade_responsavel"]= idade
                            sistema.limpar_terminal()
                            print("\nConfirmado")
                            break
                        else:
                            continue
                    else:
                        continue
                    
            while True:
                cpf_responsavel = input("\nCPF do responsavél:\n! Apenas números (11 digitos)\n")
                try:
                    cpf_responsavel_validado = self.cliente_validar_form("cpf", cpf_responsavel)
                    if cpf_responsavel_validado == False:
                        print("Inválido!\n")
                        continue
                    else:
                        self.cliente_dados["cpf_responsavel"]= cpf_responsavel_validado
                        sistema.limpar_terminal()
                        break
                
                except ValueError:
                    print("Inválido!\n")
                    continue
                
            while True:
                try:
                    telefone_responsavel = int(input(f"\nTelefone do responsavél:\n! Apenas números (11 digitos)\n"))
                    telefone_responsavel_validado = self.cliente_validar_form("telefone", telefone_responsavel)
                    if telefone_responsavel_validado == False:
                        print("Inválido!\n")
                        continue
                    else:
                        self.cliente_dados["telefone_responsavel"]= telefone_responsavel_validado
                        sistema.limpar_terminal()
                        break
                except ValueError:
                    print("Inválido!\n")
                    continue
                
            while True:
                try:
                    sistema.limpar_terminal()
                    senha_cliente = input("""Crie sua senha de usuário. (essa senha serve para ter acesso ao sistema)
                          
                          Critérios:
                        - Pelo menos 8 caracteres
                        - Pelo menos uma letra maiúscula
                        - Pelo menos uma letra minúscula
                        - Pelo menos um número
                        - Pelo menos um caractere especial
                        
                        Informe a senha: 
                        =>  """)
                    senha_cliente_confirmada = input("Confirme sua senha:")
                    
                    if senha_cliente != senha_cliente_confirmada:
                        sistema.limpar_terminal()
                        print("Inválido!\nA comfirmação foi diferente da senha informada\n")
                        continue
                    elif senha_cliente == senha_cliente_confirmada:
                        senha_validada = sistema.validar_senha(senha_cliente)
                        if senha_validada == True:
                            sistema.limpar_terminal()
                            self.cliente_dados["cliente_senha"]= senha_cliente
                            print("Sua senha foi salva\n")
                        else:
                            sistema.limpar_terminal()
                            print("Sua senha não atende aos critérios\n")
                            continue
                
                except ValueError:
                    print("Inválido!\n")
                    continue
        self.cliente_salvar_dados()
            
        return
    
    def cliente_validar_form(self,tipo_dado_form, dado_form):
        match tipo_dado_form:
            case "nome":
                nome_validado = dado_form.strip().split() 
                if len(nome_validado) >= 2:               
                    validacao = dado_form
                else:
                    validacao = False
                
            case "data_nascimento":
                try:
            # Converter a string para um objeto datetime
                    validacao = datetime.strptime(dado_form, "%d/%m/%Y")
                    return validacao
                except ValueError:
                    print("Formato de data inválido. Por favor, digite no formato DD/MM/AAAA.")
                    validacao = False
                    
            case "endereco":
                endereco_validado = dado_form.strip().split() 
                if len(endereco_validado) >= 2:             
                    validacao = dado_form
                else:
                    validacao = False
                
            case "telefone":
                
                dado_form = str(dado_form)
                if len(dado_form) == 11:
                    validacao = f"({dado_form[:2]}) {dado_form[2:6]}-{dado_form[6:]}"
                else:
                    validacao = False
                    
            case "email":
                padrao = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
                
                if re.match(padrao, dado_form):
                    validacao = dado_form
                else:
                    validacao = False
                    
            case "cpf":
                dado_form = ''.join(filter(str.isdigit, dado_form))
                
                if len(dado_form) == 11:
                    
                    validacao = f"{dado_form[:9]}-{dado_form[9:]}"
                else:
                    validacao = False
                
        return validacao
    
    def cliente_editar_dados(self, chave, valor): 
        self.cliente_trazer_dados(self.cliente_dados["cpf"])
        self.cliente_dados[f"{chave}"] = valor
        self.cliente_salvar_dados()
        
        return
    
    def cliente_salvar_dados(self): 
        for cliente in self.clientes:
            if self.cliente_dados["cpf"] == cliente["cpf"]:
                cliente = self.cliente_dados
            else:
                self.clientes.append(self.cliente_dados)
        return
    
    def cliente_trazer_dados(self, buscador):
        for cliente in self.clientes:
            if buscador == cliente["cpf"]:
                self.cliente_dados = cliente
        return
    
    def cliente_login(self):
        sistema.limpar_terminal()
        login = {
            "cpf": "",
            "cliente_senha": ""
        }
        
        while True:
            try:
                print("____Login____\n")
                login["cpf"] = int(input("CPF: "))
                login["cpf"] = str(login["cpf"])
                login["cliente_senha"] = input("Senha: ")
                
                for cliente in self.clientes:
                    if cliente["cpf"] == login["cpf"] and cliente["conta_corrente_ativa"] == True:
                        
                        self.cliente_trazer_dados(login["cpf"])
                        conta.conta_trazer_dados(login["cpf"])
                        
                        login_validado = ["validado", "ativo"]
                        break
                    elif cliente["cpf"] == login["cpf"] and cliente["conta_corrente_ativa"] == False:
                        self.cliente_trazer_dados(login["cpf"])
                        login_validado = ["validado", "inativo"]
                        break
                    else:
                        login_validado = "invalidado"
                        break
            except ValueError:
                sistema.limpar_terminal()
                print("\nInválido\n")
                continue
            
            return login_validado
