from classes.sistema import Sistema
from classes.conta import Conta
from datetime import datetime
import re

sistema = Sistema()
conta = Conta()

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
