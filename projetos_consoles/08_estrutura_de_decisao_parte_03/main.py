# Declaração de variáveis
aluno = input("Informe o nome do aluno: ")
media = float(input("Informe a média do aluno: ").replace(",", "."))

# Condição para aprovação
if media >= 7.0:
    print(f"{aluno} foi aprovado!")
elif media >= 5.0:
    print(f"{aluno} está de recuperação.")
else:
    print(f"{aluno} foi reprovado.")


# estrutura de decisao
