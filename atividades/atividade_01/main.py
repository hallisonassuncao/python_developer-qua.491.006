# tratamento de exceção
def melhor_combustivel(etanol, gasolina):
    if etanol / gasolina <= 0.7:
        return "Etanol"
    else:
        return "Gasolina"

while True:
    try:
        etanol = float(input("Digite o valor do etanol (R$): "))
        gasolina = float(input("Digite o valor da gasolina (R$): "))
        
        combustivel = melhor_combustivel(etanol, gasolina)
        print(f"O melhor para abastecer é: {combustivel}")
        
        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != 's':
            break
    except ValueError:
        print("Por favor, digite valores válidos.")



