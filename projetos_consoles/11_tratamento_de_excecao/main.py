# tratamento de excecao
try:
    n = int(input("Informe um número inteiro: "))
    print(f"Número informado: {n}.")
except Exception as e: 
    print(f"Não foi possível exibir o número. {e}.")
finally:
    print("programa encerrado com sucesso!")    
