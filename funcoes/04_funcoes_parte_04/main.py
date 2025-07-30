# importa módulo
from modulo import limpar_tela, velocidade_media, aceleracao_media

if __name__ == "__main__":
    v = None  

    while True:
        print("1 - Calcular velocidade média.")
        print("2 - Calcular aceleração média.")
        print("3 - Sair do programa.")
        opcao = input("Informe a opção desejada: ").strip()
        limpar_tela()

        if opcao == "1":
            try:
                vi = float(input("Velocidade inicial: ").replace(",", "."))
                vf = float(input("Velocidade final: ").replace(",", "."))
                v = velocidade_media(vi, vf)
                limpar_tela()
                print(f"Velocidade média: {v}")
            except Exception as e:
                print(f"Erro ao calcular velocidade média: {e}")

        elif opcao == "2":
            try:
                if v is None:
                    print("Antes calcule a velocidade média.")
                else:
                    t = float(input("Tempo: ").replace(",", "."))
                    limpar_tela()
                    a = aceleracao_media(v, t)
                    print(f"Aceleração média: {a}")
            except Exception as e:
                print(f"Erro ao calcular aceleração média: {e}")

        elif opcao == "3":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")
