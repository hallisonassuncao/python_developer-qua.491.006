from abc import ABC
from abc import abstractmethod

# classe abstrata

class Conta(ABC):
    @abstractmethod
    def __init__(self, saldo):
        # atributos private
        self.__saldo = saldo
        
    # metodos get e set
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo    

    # metodos de açao
    @abstractmethod
    def consultar_dados(self):
        pass

    @abstractmethod
    def depositar(self, valor):  
        pass  

class ContaCorrente(Conta):
    def __init__(self, titular, cpf, agencia, saldo):
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.conta = Conta
        super().__init__(saldo)


    @property
    def titular(self, titular):
        return self.titular

    @titular.setter
    def titular(self,titular):
        self.titular = titular

    @property
    def cpf(self, cpf):
        return self.cpf

    @cpf.setter
    def cpf(self, cpf):
        self.cpf = cpf

    @property
    def agencia(self, agencia):
        return self.agencia

    @titular.setter
    def agencia(self, agencia):
        self.agencia = agencia    

    @property
    def conta(self, conta):
        return self.conta

    @titular.setter
    def conta(self, conta):
        self.conta = conta  

    # metodos de interface
    def consultar_dados(self):
        print(f"{'-'*20} DADOS DA CONTA {'-'*20}\n")
        print(f"Titular da conta: {self.titular}")
        print(f"CPF do titular: {self.cpf}")
        print(f"Agencia: {self.agencia}")
        print(f"Numero da conta: {self.conta}")
        print(f"Saldo da conta: {self.saldo:2f}")

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        self.saldo = valor
        return self.saldo
    

          
          

    


    



