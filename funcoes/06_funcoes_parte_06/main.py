# função
def fatorial(n):
    # n!
    return 1 if n == 0 else n * fatorial(n - 1)

import modulo as mo

# algoritmo principal
if __name__ == "__main__":
    while True:
        try:
            entrada = input("Informe um número inteiro positivo (ou 'sair' para encerrar): ").strip()
            if entrada.lower() == "sair":
                print("Programa encerrado.")
                break

            n = int(entrada)
            if n < 0:
                print("Número inválido. Informe um inteiro positivo.")
                continue

            resultado = fatorial(n)
            print(f"Fatorial de {n} é {resultado}")
        except ValueError:
            print("Entrada inválida. Tente novamente com um número inteiro.")
            
            
