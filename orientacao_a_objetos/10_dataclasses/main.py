import Pessoa


def main():
    # instancia a Classe Pessoa
    usuario = Pessoa.Pessoa(
        nome="",
        email="",
        cpf="", 
        idade=0, 
        altura=0.0
    )
 
    # imputs
    usuario.nome = input("Informe seu nome:").strip().title()
    usuario.email = input("Informe seu email:").strip().lower()
    usuario.cpf = input("Informe seu CPF:").strip()
    usuario.idade = int(input("Informe a sua idade:"))
    usuario.altura = float(input("Informe a sua altura:").replace(",",","))

    # output
    print(usuario)


if __name__ == "__main__":
    main()    