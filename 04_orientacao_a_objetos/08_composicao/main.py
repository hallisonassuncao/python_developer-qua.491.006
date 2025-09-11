import classes as c

def main():
    proprietario = c.Pessoa(nome="", cpf="", email="", telefone="", endereco="")

    carro = c.Veiculo(
        modelo="", fabricante="", cor="",
        placa="", ano="", proprietario=None
    )

    # Inputs
    print("DADOS DO PROPRIETÁRIO:")
    proprietario.nome = input("Informe o nome: ").strip().title()
    proprietario.cpf = input("Informe o CPF: ").strip()
    proprietario.email = input("Informe o email: ").strip().lower()
    proprietario.telefone = input("Informe o telefone: ").strip()
    proprietario.endereco = input("Informe o endereço: ").strip().title()

    print("\nDADOS DO VEÍCULO:")
    carro.fabricante = input("Informe o fabricante: ").strip().title()
    carro.modelo = input("Informe o modelo: ").strip().title()
    carro.cor = input("Informe a cor do carro: ").strip()
    carro.placa = input("Informe a placa do carro: ").strip().upper()
    carro.ano = input("Informe o ano do carro: ").strip()

    carro.proprietario = proprietario

    print("\nExibindo os dados do veículo:")
    print(f"Fabricante: {carro.fabricante}")
    print(f"Modelo: {carro.modelo}")
    print(f"Cor do veículo: {carro.cor}")
    print(f"Placa do veículo: {carro.placa}")
    print(f"Ano do veículo: {carro.ano}")
    print("Dados do proprietário do veículo:")
    print(f"Nome: {carro.proprietario.nome}")
    print(f"CPF: {carro.proprietario.cpf}")
    print(f"Email: {carro.proprietario.email}")
    print(f"Telefone: {carro.proprietario.telefone}")
    print(f"Endereço: {carro.proprietario.endereco}")

if __name__ == "__main__":
    main()
