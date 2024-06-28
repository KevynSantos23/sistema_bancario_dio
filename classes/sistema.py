from datetime import datetime
import os
import platform
import hashlib
import re


class Sistema():

    sistema = platform.system()

    def index_dicionario(self, chave, valor, lista):
        index = 0
        for i in lista:
            buscador = i.get(f'{chave}')
            if buscador == valor:
                break
            else:
                index+=1
        return index
                
    
    def limpar_terminal(sistema):

        match sistema:
            case "Windows":
                # "Estamos executando no Windows."
                limpar_terminal = os.system('cls')
            case "Linux":
                # "Estamos executando no Linux."
                limpar_terminal = os.system('clear')
            case "Darwin":
                # "Estamos executando no macOS."
                limpar_terminal = os.system('clear')
            case _:
                # "Sistema operacional não reconhecido"
                print("Sistema operacional não reconhecido")
                limpar_terminal = os.system('clear')
        return limpar_terminal
    
    def data_hora(self):
        data_hora_atual = datetime.now()
        data_hora_formatada = data_hora_atual.strftime("%d-%m-%Y %H:%M:%S")

        return data_hora_formatada
    
    def gerar_hash(self,texto):
        
        sha256 = hashlib.sha256()
        texto_bytes = texto.encode('utf-8')
        sha256.update(texto_bytes)
        hash_hex = sha256.hexdigest()
    
        return hash_hex
    
    def validar_senha(senha, tipo):
    
        match tipo:
            case "cliente":
                comprimento_minimo = len(senha) >= 8
                letra_maiuscula = re.search(r'[A-Z]', senha)
                letra_minuscula = re.search(r'[a-z]', senha)
                numero = re.search(r'[0-9]', senha)
                caractere_especial = re.search(r'[!@#$%^&*(),.?":{}|<>]', senha)
    
                if comprimento_minimo and letra_maiuscula and letra_minuscula and numero and caractere_especial:
                    return True
                else:
                    return False
            case "conta":
                comprimento = len(senha) == 4
                if comprimento and type(senha) == int:
                    return True
                else:
                    return False