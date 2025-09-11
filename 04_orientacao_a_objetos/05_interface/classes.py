from abc import ABC, abstractmethod

# Classe abstrata
class Conta(ABC):
    @abstractmethod
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    # Getter
    @property
    def saldo(self):
        return self.__saldo

    # Setter
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    # Métodos abstratos
    @abstractmethod
    def consultar_dados(self):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

# Classe concreta
class ContaCorrente(Conta):
    def __init__(self, titular, cpf, agencia, numero_conta, saldo):
        self._titular = titular
        self._cpf = cpf
        self._agencia = agencia
        self._numero_conta = numero_conta
        super().__init__(saldo)

    # Getters e Setters
    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        self._titular = valor

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        self._cpf = valor

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, valor):
        self._agencia = valor

    @property
    def numero_conta(self):
        return self._numero_conta

    @numero_conta.setter
    def numero_conta(self, valor):
        self._numero_conta = valor

    # Implementação dos métodos abstratos
    def consultar_dados(self):
        print(f"{'-'*20} DADOS DA CONTA {'-'*20}")
        print(f"Titular da conta: {self.titular}")
        print(f"CPF do titular: {self.cpf}")
        print(f"Agência: {self.agencia}")
        print(f"Número da conta: {self.numero_conta}")
        print(f"Saldo da conta: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor de depósito inválido.")
        return self.saldo

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido.")
        return self.saldo
