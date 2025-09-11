def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def diagnostico(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    while True:
        nome = input("Digite seu nome: ")
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))

        imc = calcular_imc(peso, altura)
        imc_arredondado = round(imc, 2)
        diag = diagnostico(imc)

        print(f"\n{nome}, seu IMC é {imc_arredondado}")
        print(f"Diagnóstico: {diag}\n")

        repetir = input("Deseja calcular novamente? (s/n): ").strip().lower()
        if repetir != 's':
            break



