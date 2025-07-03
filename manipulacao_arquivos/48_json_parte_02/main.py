import json
import os

def ler_arquivo_json(nome_arquivo):
    try:
        with open(f"{nome_arquivo}.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_arquivo_json(nome_arquivo, dados):
    with open(f"{nome_arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def coletar_dados():
    campos = {
        "nome": ("Informe o nome: ", lambda x: x.strip().title()),
        "idade": ("Informe sua idade: ", int),
        "cpf": ("Informe o CPF: ", lambda x: x.strip()),
        "rg": ("Informe o RG: ", lambda x: x.strip()),
        "data_nasc": ("Informe a data de nascimento: ", lambda x: x.strip()),
        "sexo": ("Informe o gênero: ", lambda x: x.strip()),
        "signo": ("Informe o signo: ", lambda x: x.strip().capitalize()),
        "mae": ("Informe o nome da mãe: ", lambda x: x.strip().title()),
        "pai": ("Informe o nome do pai: ", lambda x: x.strip().title()),
        "email": ("Informe o email: ", lambda x: x.strip().lower()),
        "senha": ("Informe a senha: ", lambda x: x.strip()),
        "cep": ("Informe o CEP: ", lambda x: x.strip().lower()),
        "endereco": ("Informe o endereço: ", lambda x: x.strip().title()),
        "numero": ("Informe o número: ", int),
        "bairro": ("Informe o bairro: ", lambda x: x.strip().title()),
        "cidade": ("Informe a cidade: ", lambda x: x.strip().title()),
        "estado": ("Informe o estado: ", lambda x: x.strip().upper()),
        "telefone_fixo": ("Informe o telefone fixo: ", lambda x: x.strip()),
        "celular": ("Informe o celular: ", lambda x: x.strip()),
        "altura": ("Informe a altura (ex: 1.75): ", float),
        "peso": ("Informe o peso (ex: 70.5): ", float),
        "tipo_sanguineo": ("Informe o tipo sanguíneo: ", lambda x: x.strip().upper()),
        "cor": ("Informe a cor: ", lambda x: x.strip())
    }

    dados_pessoa = {}
    for campo, (mensagem, conversao) in campos.items():
        try:
            valor = input(mensagem)
            dados_pessoa[campo] = conversao(valor)
        except Exception:
            print(f"Valor inválido para o campo {campo}. Tente novamente.")
            return None

    return dados_pessoa

def exibir_pessoas(lista):
    print(f"\n{'-'*25} LISTA DE PESSOAS {'-'*25}\n")
    for pessoa in lista:
        for chave, valor in pessoa.items():
            print(f"{chave.capitalize()}: {valor}")
        print('-' * 50)

def main():
    try:
        nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
        lista_pessoas = ler_arquivo_json(nome_arquivo)
        
        nova_pessoa = coletar_dados()
        if nova_pessoa:
            lista_pessoas.append(nova_pessoa)
            salvar_arquivo_json(nome_arquivo, lista_pessoas)
            exibir_pessoas(lista_pessoas)
    except Exception as e:
        print(f"Não foi possível inserir a pessoa: {e}")

if __name__ == "__main__":
    main()