#LEITURA DE ARQUIVOS
with open("texto.txt", "r", encoding="utf-8") as f:
    texto = f.read()

    #Saida de dados
    print(texto)