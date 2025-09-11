from Pessoa import Pessoa
from Conta import Conta

class ContaCorrente(Pessoa, Conta):
    def __init__(self, nome, cpf, email, profissao, telefone,
                 endereco, salario, agencia, numero, saldo):
        Pessoa.__init__(self, nome, cpf, email, profissao, telefone, endereco, salario)
        Conta.__init__(self, agencia, numero, saldo)

    def exibir_dados(self):
        print("DADOS DA CONTA CORRENTE:\n")
        Pessoa.exibir_dados(self)
        Conta.exibir_dados(self)
