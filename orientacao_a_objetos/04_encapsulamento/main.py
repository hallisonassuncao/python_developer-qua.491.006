import classes as c
import os

limpar = lambda: os.system("cls" if os.nome == "nt" else "clear")

def main():
    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(nome_fantasia="" , cnpj="" , telefone="" ,endereco="")

    # setando os valores do usuario
    print("Insira os dados do usuario:\n")

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o cpf: ").strip()
    usuario.telefone = input("Informe o telefone: ").strip()
    usuario.endereco = input("Informe o endereco: ").strip().title()

    limpar()

    
    if __name__ == "__main__":
        main()

    