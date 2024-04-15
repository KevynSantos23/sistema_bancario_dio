import os
import platform

class Sistema():

    sistema = platform.system()

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