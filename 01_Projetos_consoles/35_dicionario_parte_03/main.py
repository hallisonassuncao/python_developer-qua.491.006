usuario = {
    'nome': "leticia",
    'idade': 36,
    'email': "leticia@gmail.com",
    'profissão': "DBA"

}

# exibir os valores
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")