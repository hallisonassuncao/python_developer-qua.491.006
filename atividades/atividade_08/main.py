# TODO - atividade : crie um programa que receba de um professor varias notas de uma aluno de 0 a 10
# ( não importa quantas notas). ao final do programa , a media das notas deverar se calculada e informada, e em seguida o programa ira
# informar se o aluno:

# foi aprovado, caso a media for maior ou igual a 7
# ficou em recuperacao , caso media for entre 5 e 7
# Ficou reprovado , caso media for menor que 5

# Lista de Notas
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
