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


# class Conta
class Conta:
    def __init__(self, titular, cpf, agencia, numero):
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.numero = numero
        self.saldo = 0.0
        self.movimentacoes = []

    def consultar_dados(self):
        print("---- Dados da Conta ----")
        print("Titular:", self.titular)
        print("CPF:", self.cpf)
        print("Agência:", self.agencia)
        print("Número da Conta:", self.numero)
        print("Saldo: R$", self.saldo)

    def depositar(self, valor):
        self.saldo += valor
        self.movimentacoes.append(f"Depósito de R${valor:.2f}")
        print("Depósito feito com sucesso!")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.movimentacoes.append(f"Saque de R${valor:.2f}")
            print("Saque feito com sucesso!")
        else:
            print("Saldo insuficiente.")

    def imprimir_extrato(self):
        print("---- Extrato ----")
        for item in self.movimentacoes:
            print(item)
        print("Saldo atual: R$", self.saldo)

print("Bem-vindo ao Banco!")

# dados da conta
nome = input("Digite o nome do titular: ")
cpf = input("Digite o CPF: ")
agencia = input("Digite a agência: ")
numero = input("Digite o número da conta: ")

# Criando a conta
minha_conta = Conta(nome, cpf, agencia, numero)

while True:
    print("\n O que deseja fazer?")
    print("1 - Consultar dados")
    print("2 - Depositar valor")
    print("3 - Sacar valor")
    print("4 - Imprimir extrato")
    print("5 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        minha_conta.consultar_dados()
    elif escolha == "2":
        valor = float(input("Digite o valor para depósito: R$"))
        minha_conta.depositar(valor)
    elif escolha == "3":
        valor = float(input("Digite o valor para saque: R$"))
        minha_conta.sacar(valor)
    elif escolha == "4":
        minha_conta.imprimir_extrato()
    elif escolha == "5":
        print("👋 Obrigado por usar o banco. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")