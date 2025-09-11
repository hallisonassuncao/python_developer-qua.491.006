# dicionario
usuario = dict(nome="hallison", idade=35, email="hallison@gmail.com")

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")