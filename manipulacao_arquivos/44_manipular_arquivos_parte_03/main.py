import os
while True:
    try:
        novo_texto = input("Digite o Texto: \n")
        nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
        with open(f"44_manipular_arquivo_parte_03/{nome_arquivo}.txt", "w", encoding="utf-8") as f:
            f.write(novo_texto)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"nome_arquivo.txt gravado com sucesso!")
        with True:
             prosseguir = input("Deseja gravar um novo arquivo? (s/n): ").strip().lower()
        if prosseguir == "s" or prosseguir == "n":
             break
        else:
             print("Opção inválida.")
             continue
        match prosseguir:
             case "s":
                  continue
             case "n":
                  break
    except Exception as e:
            print(f"Não foi possível gravar o arquivo: {e}.")
            continue