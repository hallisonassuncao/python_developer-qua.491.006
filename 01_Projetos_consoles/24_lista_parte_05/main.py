itens =[
    "Açai",
    "Cenoura",
    "Café",
    "Cuscuz",
    "Ovos",
    "Requeijao",
    "Leite",
    "Arroz"
]

for i in range(len(itens)):
    print(f"índice {i}: {itens[i]}")

try:
    i = int(input("Informe a posição do índice a ser alterada: "))
    if i >= 0 and i <= len(itens):
        itens[i] = input('Informe o novo valor: ').capitalize().strip()

    else:
        print('Índice inválido!')
except Exception as e:
    print(f'Não foi possível alterar o tem da lista {e}.')
finally:
    for i in range(len(itens)):
        print(f"Índice {i}: {itens[i]}.")