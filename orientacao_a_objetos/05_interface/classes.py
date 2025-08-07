class Conta:
    def __init__(self, titular, cpf, agencia, n_conta, saldo):
        # atributos private
        self.__saldo = saldo
        
    # metodos get e set
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo    