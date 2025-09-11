import datetime

# Lista de filmes com suas classificações e salas
filmes = [
    ("A Múmia", "Livre", 1),
    ("De Volta ao Planeta dos Macacos", 12, 2),
    ("Poeira no Asfalto", 14, 3),
    ("Bandas de Rock anos 90", 16, 4),
    ("O Melhor de Tudo", 18, 5)
]

# Solicita nome e idade do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

while True:
    # Exibe o menu de filmes
    print("\nMenu de filmes:")
    for filme, classificacao, sala in filmes:
        print(f"- Sala {sala}: {filme} - {classificacao} anos")

    # Solicita a escolha do filme
    escolha = int(input("\nEscolha a sala do filme que deseja assistir: "))

    # Encontra o filme correspondente
    filme_escolhido = None
    for filme, classificacao, sala in filmes:
        if sala == escolha:
            filme_escolhido = (filme, classificacao, sala)
            break

    # Verifica se a escolha é válida
    if filme_escolhido:
        nome_filme, classificacao, sala = filme_escolhido
        
        # Verifica se o usuário tem idade suficiente
        if idade >= classificacao:
            agora = datetime.datetime.now()
            print("\n---🎫 Ingresso 🎫---")
            print(f"Nome: {nome}")
            print(f"Filme: {nome_filme}")
            print(f"Sala: {sala}")
            print(f"Data e Hora: {agora.strftime('%d/%m/%Y %H:%M')}")
            print("TENHA UM BOM FILME!!!")
            break
        else:
            print("\nVocê não tem idade suficiente para assistir a este filme. Escolha outro.")
    else:
        print("\nEscolha inválida. Tente novamente.")