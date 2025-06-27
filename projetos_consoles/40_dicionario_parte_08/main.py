chaves = ("nomne", "Idade", "Email", "Telefone", "Profissão")
usuario ={
    chaves[0]:"Hallison",
    chaves[1]: 35,
    chaves[2]:"Email",
    chaves[3]:"Telefone",
    chaves[4]:"Profissão"

}

for chave in chaves:
    print(f"{chaves}: {usuario.get(chave)}")






