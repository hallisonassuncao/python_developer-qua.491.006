# TODO - atividade: crie um programa de aplicativo de banco, onde :
# - o Usuario cria uma conta no banco com os seguintes dados:

# --Titular da conta
# --Cpf do titular
# --Agencia
# --Numero da conta
# --Saldo

# O usuario pode fazer no programa:

# -Consultar dados
# -Depositar Valor
# -Sacar valor
# -Imprimir extrato (entendo-se: gerar arquivo com os dados da conta)
# -Sair do programa.
# NOTE - o nome da classe é conta

# Primeiro, criamos a classe Conta


class Conta:
    def __init__(self, titular, cpf, agencia, numero):
        self.titular = titular       # Nome da pessoa
        self.cpf = cpf               # CPF da pessoa
        self.agencia = agencia       # Número da agência
        self.numero = numero         # Número da conta
        self.saldo = 0.0             # Saldo começa zerado
        self.movimentacoes = []      # Lista para guardar extrato

    def consultar_dados(self):
        print("---- Dados da Conta ----")
        print("Titular:", self.titular)
        print("CPF:", self.cpf)
        print("Agência:", self.agencia)
        print("Número da Conta:", self.numero)
        print("Saldo: R$", self.saldo)

    def depositar(self, valor):
        self.saldo += valor
        self.movimentacoes.append(f"Depósito de R${valor}")
        print("Depósito feito com sucesso!")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.movimentacoes.append(f"Saque de R${valor}")
            print("Saque feito com sucesso!")
        else:
            print("Saldo insuficiente.")

    def imprimir_extrato(self):
        print("---- Extrato ----")
        for item in self.movimentacoes:
            print(item)
        print("Saldo atual: R$", self.saldo)

        # Classe Conta 
class Conta:
    def __init__(self, titular, cpf, agencia, numero):
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.numero = numero
        self.saldo = 0.0
        self.movimentacoes = []

    def consultar_dados(self):
        print("\n---- Dados da Conta ----")
        print("Titular:", self.titular)
        print("CPF:", self.cpf)
        print("Agência:", self.agencia)
        print("Número da Conta:", self.numero)
        print("Saldo: R$", self.saldo)

    def depositar(self, valor):
        self.saldo += valor
        self.movimentacoes.append(f"Depósito: R${valor:.2f}")
        print("Depósito realizado!")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.movimentacoes.append(f"Saque: R${valor:.2f}")
            print("Saque realizado!")
        else:
            print("Saldo insuficiente.")

    def imprimir_extrato(self):
        print("\n---- Extrato ----")
        for item in self.movimentacoes:
            print(item)
        print("Saldo atual: R$", self.saldo)