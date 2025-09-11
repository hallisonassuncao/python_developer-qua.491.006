import classes as c

def main():
    # instancia objeto da classe ContaCorrente
    cc = c.ContaCorrente(
        titular="Leticia", 
        cpf="123.123.122-89", 
        agencia="0001", 
        numero_conta="0312214-12",  
        saldo=900.0
    )

    cc.consultar_dados()
    print(f"\nSaldo: R$ {cc.saldo:.2f}")  

if __name__ == "__main__":
    main()

