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
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = agencia
        self.__conta = Conta
        super().__init__(saldo)


    @property
    def titular(self, titular):
        return self.__titular

    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    @property
    def cpf(self, cpf):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def agencia(self, agencia):
        return self.__agencia

    @titular.setter
    def agencia(self, agencia):
        self.__agencia = agencia    

    @property
    def conta(self, conta):
        return self.__conta

    @titular.setter
    def conta(self, conta):
        self.__conta = conta  

    # metodos de interface
    def consultar_dados(self):
        print(f"{'-'*20} DADOS DA CONTA {'-'*20}\n")
        print(f"Titular da conta: {self.__titular}")
        print(f"CPF do titular: {self.__cpf}")
        print(f"Agencia: {self.__agencia}")
        print(f"Numero da conta: {self.__conta}")
        print(f"Saldo da conta: {self.__saldo:2f}")

    def depositar(self, valor):
        self.__saldo += valor
        return self.__saldo

    def sacar(self, valor):
        self.__saldo -= valor
        return self.__saldo
    

          
          

    


    



