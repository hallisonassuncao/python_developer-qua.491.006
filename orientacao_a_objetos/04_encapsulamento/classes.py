# superclasse
class pessoa:
    def __init__(self, telefone, endereco):
       self.__telefone = telefone # private
       self.__endereco = endereco # private

       # metodos de acesso

       # metodo get telefone
       @property
       def telefone(self):
           return self.__telefone

       # metodo set telefone
       @telefone.setter
       def telefone(self, telefone):
           self.__telefone = telefone

      
              




