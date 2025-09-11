import os

# Lista
nomes = ["Fulano", "Ciclano", "Beltrano", "João", "Maria", "Jose"]

# Exibe os valores sem o item isolado
for i in range(len(nomes)):
    print(f"{i}: {nomes[i]}")
print("-" * 60)

try:
    i = int(input("Informe o índice que deseja separar: "))
    
    if 0 <= i < len(nomes): 
        nome_isolado = nomes.pop(i)

        # Limpa a tela
        os.system("cls" if os.name == "nt" else "clear")

        print(f"Nome isolado: {nome_isolado}")
    else:
        print("Índice inválido!")  

except ValueError:
    print("Erro: Você deve digitar um número inteiro.")
except Exception as e:
    print(f"Não foi possível executar a operação. Erro: {e}.")
