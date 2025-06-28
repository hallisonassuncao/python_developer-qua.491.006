# TODO - atividade: Crie um programa que faça as seguintes funções:
# 1 - Cadastre um novo usuário
# 2 - Liste todos os usuários cadastrados
# 3 - Altere os dados de um usuário
# 4 - Fazer o sorteio de um usuario
# 5 - Exclua um usuário
# 6 - Saia do programa
# NOTE - dados do usuário:
# - Nome completo
# - Data de Nascimento
# - E-mail
# - CPF
# - Telefone
# - Gênero
# - Data do cadastro (pegar do sistema)
# - Hora do cadastro ((pegar do sistema)

import os
import random

usuario = []

while True:
    # menu
    print("1 - Cadastre um novo usuario")
    print("2 - Liste todos os usuarios cadastrados")
    print("3 - Altere os dados")
    print("4 - Fazer o sorteio de um usuario")
    print("5 - Exclua um usuario")
    print("6 - Sair do programa")
    opcao = input("Informe a opção desejada: ")
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            try:
                novo_nome = input("Informe novo nome: ").title().strip()
                usuario.append(novo_nome)
                print(f"{novo_nome} inserido com sucesso!")
            except Exception as e:
                print(f"Não foi possível inserir o novo nome. Erro: {e}")

        case "2":
            if usuario:
                print("usuarios cadastrados:")
                for i, nome in enumerate(usuario, start=1):
                    print(f"{i} - {nome}")
            else:
                print("Nenhum usuário cadastrado.")

        case "3":
            if usuario:
                for i, nome in enumerate(usuario, start=1):
                    print(f"{i} - {nome}")
                try:
                    indice = int(input("Digite o número do usuário que deseja alterar: ")) - 1
                    if 0 <= indice < len(usuario):
                        novo_nome = input("Digite o novo nome: ").title().strip()
                        usuario[indice] = novo_nome
                        print("Nome alterado com sucesso!")
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Nenhum usuário para alterar.")

            if usuario:
               sorteado = random.choices  
        case "4":
            if usuario:
                sorteado = random.choice(usuario)
                print(f"O usuário sorteado foi: {sorteado}")
            else:
                print("Nenhum usuário para sortear.")
        
        case "5":
            if usuario:
                for i, nome in enumerate(usuario, start=1):
                    print(f"{i} - {nome}")
                try:
                    indice = int(input("Digite o número do usuário que deseja excluir: ")) - 1
                    if 0 <= indice < len(usuario):
                        removido = usuario.pop(indice)
                        print(f"Usuário {removido} removido com sucesso!")
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Nenhum usuário para excluir.")
        
        case "6":
            print("Encerrando o programa.")
            break

        case _:
            print("Opção inválida.")


        
        
                    

          

