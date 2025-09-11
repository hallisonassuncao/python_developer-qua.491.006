
try:
    arquivo = input("Informe o Nome do Arquivo: (Sem Extensão): ").strip().lower()
    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
        texto = f.read()
        print(f"Texto Gravado: \n{texto}")

        novo_texto = input("Digite o Novo Texto: \n")
        nova_gravacao = f"{novo_texto}"

        with open(f"{arquivo}.txt", "w", encoding="utf-8") as f:
            f.write(nova_gravacao)
        print(f"Gravação feita com sucesso.")

        with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
            texto_final = f.read()
except Exception as e:
    print(f"Não foi possível atualizar o conteudo. {e}.")
