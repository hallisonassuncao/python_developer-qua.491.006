class Conta:
    def __init__(self, agencia, numero, saldo=0.0):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def exibir_dados(self):
        print(f"\nAgência: {self.agencia}")
        print(f"Conta: {self.numero}")
        print(f"Saldo: R$ {self.saldo:.2f}")

    def fazer_deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def fazer_saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saque inválido. Verifique o saldo ou o valor informado.")

def main():
    print("=== Bem-vindo ao sistema bancário ===")

    # Criando a conta
    agencia = input("Digite o número da agência: ")
    numero = input("Digite o número da conta: ")

    try:
        saldo_inicial = float(input("Digite o saldo inicial: "))
    except ValueError:
        print("Valor inválido. O saldo será definido como R$ 0.00.")
        saldo_inicial = 0.0

    conta = Conta(agencia, numero, saldo_inicial)

    while True:
        print("\n--- Menu ---")
        print("1. Exibir dados da conta")
        print("2. Fazer depósito")
        print("3. Fazer saque")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            conta.exibir_dados()

        elif opcao == "2":
            try:
                valor = float(input("Digite o valor do depósito: "))
                conta.fazer_deposito(valor)
            except ValueError:
                print("Valor inválido.")

        elif opcao == "3":
            try:
                valor = float(input("Digite o valor do saque: "))
                conta.fazer_saque(valor)
            except ValueError:
                print("Valor inválido.")

        elif opcao == "4":
            print("Encerrando o sistema. Obrigado!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa principal
if __name__ == "__main__":
    main()
