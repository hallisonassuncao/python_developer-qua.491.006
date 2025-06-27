# Dicionário inicial
usuario = {
    'nome': "Hallison",
    'idade': 40,
    'email': "hallison@gmail.com"
}

print("Dados atuais:")
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

usuario['profissão'] = input("\nInforme a profissão: ").strip()

print("\n" + "-"*40)
print("Dados atualizados:")
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
