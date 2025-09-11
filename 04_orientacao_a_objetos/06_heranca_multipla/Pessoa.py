# superclasse
class Pessoa:

    def __init__(self, nome, cpf, email, profissao, telefone, endereco, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__profissao = profissao
        self.__telefone = telefone
        self.__endereco = endereco
        self.__salario = salario

    # Nome
    @property
    def nome(self):
        return self.__nome  

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # CPF
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    # Email
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    # Profissão
    @property
    def profissao(self):
        return self.__profissao

    @profissao.setter
    def profissao(self, profissao):
        self.__profissao = profissao

    # Telefone
    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    # Endereço
    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    # Salário
    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

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


