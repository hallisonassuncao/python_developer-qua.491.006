import math
import os 

# Funções lambda
area_circulo = lambda r: math.pi * r**2
circunferencia = lambda r: 2 * math.pi * r
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

# Algoritmo principal
if __name__ == "__main__":
    try:
        limpar() 
        
        raio = float(input("Informe o raio do círculo: "))
        
        area = area_circulo(raio)
        circ = circunferencia(raio)
        
        print(f"\n Área do círculo: {area:.2f}")
        print(f" Circunferência do círculo: {circ:.2f}")
    except Exception as e:
        print(f"❌ Erro ao calcular: {e}")
