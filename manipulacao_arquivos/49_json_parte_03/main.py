import json

try:
    #usuário informe o arquivo
    arquivo = input("Informe o Arquivo. ").strip().lower()
    #lê json de desserializa para dicionario
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        lista = json.load(f)

    #aplica as conversões
    for dado in lista:
        dado['altura'] = dado["altura"].replace(",", ".")
        dado['altura'] = float(dado['altura'])
        dado['peso'] = float(dado['peso'])

    #serializa o dicionario em json e grava o arquivo
    with open(f"{arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

        #confirmação
        print("Conversão gravada com sucesso. ")
except Exception as e:
    print(f"Não foi possivel converter. {e}.")