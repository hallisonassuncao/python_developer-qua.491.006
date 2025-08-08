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

    # Método para exibir os dados da pessoa
    def exibir_dados(self):
        print(f"{'-'*20} DADOS PESSOAIS {'-'*20}")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"E-mail: {self.email}")
        print(f"Profissão: {self.profissao}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")
        print(f"Salário: R$ {self.salario:.2f}")

