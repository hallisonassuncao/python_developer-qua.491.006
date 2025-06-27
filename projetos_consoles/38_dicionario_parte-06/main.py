# dicionario
usuario = {
    'nome': "Hallison",
    'idade': 35,
    'email': "hallison@gmail.com",
    'profissão': "Tecnico TI"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

print("-" * 40)

chave_para_alterar = input("Qual chave deseja alterar? ").strip().lower()

if chave_para_alterar in usuario:
    novo_valor = input(f"Informe o novo valor de {chave}: ").strip()
    usuario[chave_para_alterar] = novo_valor
else:
    print("Chave inexistente.")

print("-" * 40)

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
  