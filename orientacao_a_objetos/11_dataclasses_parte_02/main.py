import PessoaFisica
import PessoaJuridica
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    usuario = PessoaFisica.PessoaFisica(
        email="", telefone="", endereco="",
        nome="", cpf="", idade=0
    )

    empresa = PessoaJuridica.PessoaJuridica(
        email="", telefone="", endereco="",
        razao_social="", nome_fantasia="", cnpj=""
    )

    # input do usuario
    print("Informe os Dados do usuário:\n")
    usuario.nome = input("Informe seu nome: ").strip().title()
    usuario.cpf = input("Informe seu CPF: ").strip()
    usuario.idade = int(input("Informe sua idade: "))
    usuario.email = input("Informe seu email: ").strip().lower()
    usuario.telefone = input("Informe seu telefone: ").strip()
    usuario.endereco = input("Informe seu endereço: ").strip()

    limpar()

    # input da empresa
    print("Informe os Dados da empresa:\n")
    empresa.razao_social = input("Razão Social: ").strip().title()
    empresa.nome_fantasia = input("Nome Fantasia: ").strip().title()
    empresa.cnpj = input("CNPJ: ").strip()
    empresa.email = input("Email da empresa: ").strip().lower()
    empresa.telefone = input("Telefone da empresa: ").strip()
    empresa.endereco = input("Endereço da empresa: ").strip()


    #output
    print(usuario)
    print(usuario)    
if __name__ == "__main__":
    main()
