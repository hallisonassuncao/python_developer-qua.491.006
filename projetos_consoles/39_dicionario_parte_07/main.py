# Dicionário inicial
usuario = {
    'nome': "Hallison",
    'idade': 35,
    'email': "hallison@gmail.com",
    'profissão': "Tecnico TI"
}

# Exibe os dados atuais
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
print("-" * 40)

# Usuário informa a chave que deseja excluir
chave = input("Informe a chave que deseja excluir: ").lower().strip()

# Verifica se a chave existe
if chave in usuario:
    # Excluir a chave
    del usuario[chave]
    print(f"\nChave '{chave}' removida com sucesso!")
else:
    print("\nChave inexistente.")

print("-" * 40)

# Exibe os dados atualizados
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")





