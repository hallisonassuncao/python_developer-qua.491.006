
import calendar

# solicitar o Ano ao usúario

while True:
    try:
        ano = int(input("Digite um ano a partir de 1900: "))
        if ano >= 1900:
            break
        else:
            print("Por favor, digite um ano igual ou superior a 1900.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

# Exibir o Calendario do ano informado
print("\nCalendário do ano", ano)
print(calendar.TextCalendar().formatyear(ano))
