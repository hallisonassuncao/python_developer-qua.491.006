import classes as c

def main():
    # instacia objeto da classe Conta
    cc = c.ContaCorrente(
        titular="Leticia", 
        cpf="123.123.122-89", 
        agencia="0001", 
        Conta="0312214-12", 
        saldo=900.0
    )
    cc.consultar_dados()
    print(f"Saldo: R$ {c.consultar_saldo}")
    
    
if __name__ == "__main__":
    main()    
