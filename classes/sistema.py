import os
import platform
from datetime import datetime


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
    
    def data_hora(self):
        data_hora_atual = datetime.now()
        data_hora_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")

        return data_hora_formatada