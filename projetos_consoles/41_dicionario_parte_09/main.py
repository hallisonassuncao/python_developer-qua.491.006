usuarios = [
    {
        'nome': "Maria",
        'idade': 35,
        'email': "maria@gmail.com"
    },
    {
        'nome': "Ciclano",
        'idade': 18,
        'email': "ciclano@gmail.com"
    },
    {
        'nome': "Beltrano",
        'idade': 28,
        'email': "beltrano@gmail.com"
    }
]

# exibe os dados 
for usuario in usuarios:
    print("-"*40)
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario.get(chave)}")