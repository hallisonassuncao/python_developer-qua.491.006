
import json
import os

pessoa = {}

try:
    arquivo = input("Informe o arquivo: ").strip().lower()

    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        pessoas = json.load(f)

    # usuário informa os dados da nova pessoa
    pessoa['nome'] = input("informe o nome: ").strip().title()
    pessoa['idade'] = int(input("informe a idade: "))
    pessoa['cpf'] = input("informe o CPF: ").strip()
    pessoa['rg'] = input("informe o RG: ").strip()
    pessoa['data_nasc'] = input("informe a data de nascimento: ").strip()
    pessoa['sexo'] = input("informe o genero: ").strip()
    pessoa['signo'] = input("informe o signo: ").strip().capitalize()
    pessoa['mae'] = input("informe o nome da mãe: ").strip().title()
    pessoa['pai'] = input("informe o nome do pai: ").strip().title()
    pessoa['email'] = input("informe o email: ").strip().lower()
    pessoa['senha'] = input("informe a senha: ")
    pessoa['endereco'] = input("informe o endereço: ").strip().title()
    pessoa['numero'] = int(input("informe o numero: "))
    pessoa['bairro'] = input("informe o bairro: ").strip().capitalize()
    pessoa['cidade'] = input("informe a cidade: ").strip().title()
    pessoa['estado'] = input("informe o estado: ").strip().upper()
    pessoa['telefone_fixo'] = input("informe o telefone: ").strip()
    pessoa['celular'] = input("informe o celular: ").strip()
    pessoa['altura'] = float(input("informe a altura: ").replace(",", "."))
    pessoa['peso'] = float(input("informe o peso: ").replace(",", "."))
    pessoa['tipo_sanguineo'] = input("informe o tipo sanguineo: ").strip().capitalize()
    pessoa['cor'] = input("informe a cor: ").strip()

    pessoas.append(pessoa)

    with open(f"{arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(pessoas, f, ensure_ascii=False, indent=4)

    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        pessoas = json.load(f)
    print(f"{'-'*20} LISTA DE PESSOAS {'-'*20}")
    for pessoa in pessoas:
        for chave in pessoas:
            print(f"{chave.capitalize()}: {pessoa.get(chave)}")
        print('-'*58)

except Exception as e:
    print(f"Não foi possível inserir pessoa. {e}")
