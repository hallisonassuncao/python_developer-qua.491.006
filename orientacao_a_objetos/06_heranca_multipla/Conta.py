import iConta

# superclasse
class Conta(iConta):
    # Construtor
    def __init__(self, agencia, numero, saldo):
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo

    # agência
    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    # número
    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    # saldo
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            print("Saldo não pode ser negativo.")

    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor de depósito deve ser positivo.")

    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido.")

    
    def exibir_dados(self):
        print(f"Agência: {self.agencia}")
        print(f"Número: {self.numero}.")
        print(f"Saldo: R$ {self.saldo:.2f}.")

    def fazer_deposito(self, valor):
        self.saldo +=valor
        return self.saldo
    
    def fazer_saque(self, valor):
        self.saldo -= valor
        return self.saldo
    
    
