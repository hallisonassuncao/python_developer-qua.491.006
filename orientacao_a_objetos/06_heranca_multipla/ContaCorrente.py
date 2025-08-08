import Pessoa
import Conta

# subclasse
class ContaCorrente(Pessoa, Conta):
    def __init__(self, nome, cpf, email, profissao, telefone,
    endereco, salario, agencia, numero, saldo):
        Pessoa.__init__(self, nome, cpf, email, profissao, telefone,
    endereco, salario)
        Conta.__init__(self, agencia, numero, saldo)
        
        
        