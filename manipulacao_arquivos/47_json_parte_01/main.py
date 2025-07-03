
# importações 
import json

try:
    arquivo = input("Informe o nome do arquivo (Sem Extensão): ").strip().lower()
    # lê o json desserializa em um dicionario
    with open(f"{arquivo}.json",  "r", encoding="utf-8") as f:
        dados = json.load(f)

        #ouput
        print(f"{'-'*20} DADOS {'-'*20}\n")
        for dado in dados:
            for chave in dado:
                print(f"{chave.capitalize()}: {dado.get(chave)}")
                print('-'*40)
except Exception as e:
    print(f"Não foi possivel ler arquivo JSON. {e}.")
