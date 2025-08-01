class Pessoa:
    # atributos
    nome = "Hallison"
    idade = 36
    telefone = "(61)9999-9999"
    cpf = "123.123.123-70"
    email = "hallison@uol.com"

    # método
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, "
              f"meu telefone é {self.telefone}, meu CPF é {self.cpf} e meu email é {self.email}.")

# programa principal
if __name__ == "__main__":
    # instaciar classe
    usuario = Pessoa()