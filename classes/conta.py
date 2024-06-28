from classes.sistema import Sistema
import random

sistema = Sistema()
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