
import os
import random

nomes = []  # não se esqueça de inicializar sua lista!

while True:
    print("1 - Inserir nome na lista")
    print("2 - Exibir lista")
    print("3 - Sortear nome")
    print("4 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            try:
                novo_nome = input("Informe o nome: ").title().strip()
                os.system("cls" if os.name == "nt" else "clear")
                nomes.append(novo_nome)
                print("Nome inserido com sucesso!")
            except Exception as e:
                print(f"Não foi possível inserir o nome na lista. {e}.")
            finally:
                continue

        case "2":
            try:
                nomes.sort()
                for nome in nomes:
                    print(nome)
                print('-' * 40)
            except Exception as e:
                print(f"Não foi possível exibir a lista. {e}.")
            finally:
                continue

        case "3":
            try:
                if not nomes:
                    raise ValueError("A lista está vazia.")
                i = random.randint(0, len(nomes) - 1)
                print(f"Nome sorteado: {nomes[i]}")
            except Exception as e:
                print(f"Erro ao sortear nome: {e}")
            finally:
                continue

        case "4":
            print("Programa encerrando.")
            break

        case _:
            print("Opção inválida.")
            continue

            

