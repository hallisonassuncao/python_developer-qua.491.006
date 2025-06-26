usuario = {
    'nome': "leticia Camila",
    'idade': 36,
    'email': "leticia.camilaa@gmail.com",
    'profissão': "DBA"

}

# exibir os valores
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

    