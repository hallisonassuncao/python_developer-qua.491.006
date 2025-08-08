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

    

