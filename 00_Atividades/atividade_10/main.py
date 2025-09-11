# TODO - atividade: faça um CRUD (Create, Read, Update, Delete) em um JSON.

# Opções do menu:
#- Criar novo arquivo JSON (usuário irá informar o diretório).
#- Abrir arquivo JSON (usuário irá informar o diretório).
#- Cadastrar novo usuário em um JSON.
#- Listar todos os usuários de um arquivo JSON.
#- Pesquisar por um usuário de um arquivo JSON.
#- Alterar dados de um usuário em um arquivo JSON.
#- Deletar usuário de um arquivo JSON.
#- Sair do programa

# Dados do usuário:
#- Nome
#- Data de nascimento
#- CPF
#- E-mail
#- Telefone
#- Filme favorito do usuário

import json
import os

def criar_arquivo_json(caminho):
    with open(caminho, 'w') as arquivo:
        json.dump([], arquivo)
    print("Arquivo criado com sucesso!")

def abrir_arquivo_json(caminho):
    if os.path.exists(caminho):
        with open(caminho, 'r') as arquivo:
            return json.load(arquivo)
    else:
        print("Arquivo não encontrado.")
        return []

def salvar_arquivo_json(caminho, dados):
    with open(caminho, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def cadastrar_usuario(dados):
    usuario = {
        "nome": input("Nome: "),
        "data_nascimento": input("Data de nascimento: "),
        "cpf": input("CPF: "),
        "email": input("E-mail: "),
        "telefone": input("Telefone: "),
        "filme_favorito": input("Filme favorito: ")
    }
    dados.append(usuario)
    print("Usuário cadastrado!")

def listar_usuarios(dados):
    for i, usuario in enumerate(dados):
        print(f"{i+1}. {usuario}")

def buscar_usuario(dados):
    cpf = input("Digite o CPF: ")
    for usuario in dados:
        if usuario["cpf"] == cpf:
            print(usuario)
            return
    print("Usuário não encontrado.")

def alterar_usuario(dados):
    cpf = input("CPF do usuário a alterar: ")
    for usuario in dados:
        if usuario["cpf"] == cpf:
            usuario["nome"] = input("Novo nome: ")
            usuario["data_nascimento"] = input("Nova data de nascimento: ")
            usuario["email"] = input("Novo e-mail: ")
            usuario["telefone"] = input("Novo telefone: ")
            usuario["filme_favorito"] = input("Novo filme favorito: ")
            print("Usuário atualizado.")
            return
    print("Usuário não encontrado.")

def deletar_usuario(dados):
    cpf = input("CPF do usuário a deletar: ")
    for usuario in dados:
        if usuario["cpf"] == cpf:
            dados.remove(usuario)
            print("Usuário deletado.")
            return
    print("Usuário não encontrado.")

def main():
    dados = []
    caminho = ""

    while True:
        print("\nMENU:")
        print("1 - Criar novo arquivo JSON")
        print("2 - Abrir arquivo JSON")
        print("3 - Cadastrar novo usuário")
        print("4 - Listar usuários")
        print("5 - Buscar usuário por CPF")
        print("6 - Alterar usuário")
        print("7 - Deletar usuário")
        print("8 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            caminho = input("Informe o caminho do novo arquivo: ")
            criar_arquivo_json(caminho)
        elif opcao == "2":
            caminho = input("Informe o caminho do arquivo: ")
            dados = abrir_arquivo_json(caminho)
        elif opcao == "3":
            cadastrar_usuario(dados)
            salvar_arquivo_json(caminho, dados)
        elif opcao == "4":
            listar_usuarios(dados)
        elif opcao == "5":
            buscar_usuario(dados)
        elif opcao == "6":
            alterar_usuario(dados)
            salvar_arquivo_json(caminho, dados)
        elif opcao == "7":
            deletar_usuario(dados)
            salvar_arquivo_json(caminho, dados)
        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()