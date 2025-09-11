import os

lista = []

while True:
    # menu
    print("1 - Cadastro novo nome na lista")
    print("2 - Liste todos os nomes da lista")
    print("3 - Pesquise por um nome na lista")
    print("4 - Altere um nome na lista")
    print("5 - Exclua um nome da lista")
    print("6 - Sair do programa")
    opcao = input("Informe a opção desejada: ")
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            try:
                novo_nome = input("Informe novo nome: ").title().strip()
                lista.append(novo_nome)
                print(f"{novo_nome} inserido com sucesso!")
            except Exception as e:
                print(f"Não foi possível inserir o novo nome. Erro: {e}")
                
        case "2":
            try:
                if lista:
                    print("Nomes cadastrados:")
                    for i, nome in enumerate(lista, start=1):
                        print(f"{i}. {nome}")
                else:
                    print("A lista está vazia.")
            except Exception as e:
                print(f"Não foi possível exibir a lista: {e}")
            finally:
                continue

        case "3":
            try:
                nome_pesquisa = input("Informe o nome a ser pesquisado: ").title().strip()
                if nome_pesquisa in lista:
                    print(f"{nome_pesquisa} está na lista.")
                else:
                    print(f"{nome_pesquisa} não foi encontrado.")
            except Exception as e:
                print(f"Erro ao pesquisar nome: {e}")
        
        case "4":
            try:
                nome_antigo = input("Informe o indice a ser alterado: ").title().strip()
                if nome_antigo in lista:
                    novo_nome = input("Digite o novo nome: ").title().strip()
                    indice = lista.index(nome_antigo)
                    lista[indice] = novo_nome
                    print(f"{nome_antigo} foi alterado para {novo_nome}.")
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Nome alterado com sucesso.")
                else:
                    print(f"{nome_antigo} não está na lista.")
            except Exception as e:
                print(f"Erro ao alterar nome: {e}")

        case "5":
            try:
                nome_excluir = input("Digite o nome que deseja excluir: ").title().strip()
                if nome_excluir in lista:
                    lista.remove(nome_excluir)
                    print(f"{nome_excluir} foi removido da lista.")
                else:
                    print(f"{nome_excluir} não foi encontrado.")
            except Exception as e:
                print(f"Erro ao excluir nome: {e}")

        case "6":
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida.")
