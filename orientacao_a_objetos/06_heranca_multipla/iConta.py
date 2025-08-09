from abc import ABC
from abc import abstractmethod

# interface
class iConta(ABC):
    @abstractmethod
    def exibir_dados(self):
        pass

    @abstractmethod
    def fazer_deposito(self, valor):
        pass

    @abstractmethod
    def fazer_saque(self, valor):
        pass

    
    def exibir_dados(self):
        print("DADOS DA CONTA:\n")
        print(f"Nome do titular da conta: {self.nome}.")
        print(f"CPF do titular da conta: {self.cpf}.")
        print(f"Email do titular da conta: {self.email}.")
        print(f"Profissao do titular da conta: {self.profissao}.")
        print(f"Telefone titular da conta: {self.telefone}.")
        print(f"Endereco do titular da conta: {self.endereco}.")
        print(f"Salario do titular da conta: {self.salario}.")
        super().exibir_dados()
