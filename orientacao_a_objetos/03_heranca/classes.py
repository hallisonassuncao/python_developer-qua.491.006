# Superclasse
class Pessoa:
    def __init__(self, telefone, endereco):
        self.telefone = telefone
        self.endereco = endereco

    def exibir_dados(self):
        print(f"Telefone: {self.telefone}") 
        print(f"Endereço: {self.endereco}")  

# Subclasse Pessoa Física
class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        super().__init__(telefone, endereco)

    def exibir_dados(self):
        print(f"Nome: {self.nome}") 
        print(f"CPF: {self.cpf}") 
        super().exibir_dados()    

# Subclasse Pessoa Jurídica
class PessoaJuridica(Pessoa):
    def __init__(self, nome_fantasia, cnpj, telefone, endereco):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(telefone, endereco)

    def exibir_dados(self):
        print(f"Nome da Empresa: {self.nome_fantasia}")  
        print(f"CNPJ: {self.cnpj}")
        super().exibir_dados()
