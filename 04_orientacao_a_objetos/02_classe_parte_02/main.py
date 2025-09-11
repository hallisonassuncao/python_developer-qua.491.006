# classe
class Pessoa:
    # construtor
    def __init__(self, nome, idade, telefone, cpf, email):
        # atributos
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cpf = cpf
        self.email = email

    # método
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, "
              f"meu telefone é {self.telefone}, meu CPF é {self.cpf} e meu email é {self.email}.")

# algoritmo principal
if __name__ == "__main__":
    # instanciar classe com dados personalizados
    usuario = Pessoa("Hallison", 36, "(61)9999-9999", "123.123.123-70", "hallison@uol.com")

    # objeto se apresenta
    usuario.apresentar()

    try:
        # input 
        usuario.nome = input("Informe seu nome: ").strip().title()
        usuario.idade = int(input("Informe sua idade: "))
        usuario.telefone = input("Informe seu telefone: ").strip()
        usuario.cpf = input("Informe seu CPF: ").strip()
        usuario.email = input("Informe seu email: ").strip().lower()

        print("\nDados atualizados com sucesso!\n")
        usuario.apresentar()

    except Exception as e:
        print(f"Ocorreu um erro ao atualizar os dados: {e}")
