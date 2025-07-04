
import json
import os

usuarios = []
novo_arquivo = ""

while True:
    usuario = {}
    print("1 - Cadastrar Novo Usuário. ")
    print("2 - Salvar Arquivo Json. ")
    print("3 - Fazer Leitura do Json. ")
    print("4 - Sair do Programa. ")
    opcao = input("Informe a Opção Desejada: ")
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            usuario['nome'] = input("Informe o Nome: ").strip().title()
            usuario['idade'] = int(input("Informe a Idade: "))
            usuario['email'] = input("Informe o E-mail: ").strip().lower

            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")

            print("Usuario Cadastrado com Sucesso.")
            continue
        case "2":
            novo_arquivo = input("Informe o Nome do Arquivo: ").strip().lower
            with open(f"50_json_parte_04/{novo_arquivo}.json", "w", encoding="utf-8") as f:  # fazer uma correção desta linha 28
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            os.system("cls" if os.name == "nt" else "clear")
            print("Arquivo Salvo com Sucesso.")
            continue
        case "3":
            if not novo_arquivo:
                novo_arquivo = input("Informe o Nome do Arquivo: ").strip().lower()
                with open(f"50_json_parte_04/{novo_arquivo}.json", "r", encoding="utf-8") as f:
                    dados = json.load(f)
                print(f"{'-'*20} USUÁRIOS {'-'*20}\n")
                for usuario in dados:
                    for chave in usuario:
                        print(f"{chave.capitalize()}: {usuario.get(chave)}")
                    print('-'*40)
                    continue
        case "4":
            print("Programa Encerrado. ")
        case _:
            print("Opção Inválida. ")
            continue
