import os
import platform

class Sistema():

    sistema = platform.system()

    def limpar_terminal(sistema):
        
        match sistema:
            case "Windows":
                # "Estamos executando no Windows."
                resposta = limpar_terminal = os.system('cls')
            case "Linux":
                # "Estamos executando no Linux."
                resposta = limpar_terminal = os.system('clear')
            case "Darwin":
                # "Estamos executando no macOS."
                resposta = limpar_terminal = os.system('clear')
            case _:
                # "Sistema operacional não reconhecido"
                print("Sistema operacional não reconhecido")
                resposta = limpar_terminal = os.system('clear')
        return resposta