#importações
import os

#entrada de dados
while True:
    try:
        #usuario informa o nome do arquivo
        arquivo = input("Informe o nome do arquivo(sem extensão): ").strip().lower()

        #abre o arquivo
        with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
            arquivo_aberto = f.read()
            os.system("cls" if os.name == "nt" else "clear")
            
            #mostrar os dados do arquivos
            print(arquivo_aberto)
            while True:
                prosseguir = input("Deseja abrir outro arquivo? (s/n): ").strip().lower()
                if prosseguir == "s" or prosseguir == "n":
                    break
                else:
                    print("Opção inválida.")
        match prosseguir:
            case "s":
                continue
            case "n":
                break
    except Exception as e:
            print(f"Não foi possível ler o arquivo. {e}.")
            continue
            
            #imprime o conteúdo
            print(conteudo)
    except Exception as e:
        print(f"Não foi possivel ler o arquivo:  ")
        continue