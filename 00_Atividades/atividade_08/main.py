notas = []

print("Digite as notas do aluno (de 0 a 10). Digite 'sair' para finalizar.")

while True:
    entrada = input("Informe uma nota: ")
    
    if entrada.lower() == "sair":
        break 
    
    try:
        nota = float(entrada)
        
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Erro: A nota deve estar entre 0 e 10.")
    except ValueError:
        print("Erro: Digite um número válido.")
 
if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia do aluno: {media:.2f}")

# media do Aluno
    if media >= 7:
        print("Situação: Aprovado! ")
    elif 5 <= media < 7:
        print("Situação: Recuperação! ")
    else:
        print("Situação: Reprovado! ")
else:
    print("Nenhuma nota foi inserida.")
