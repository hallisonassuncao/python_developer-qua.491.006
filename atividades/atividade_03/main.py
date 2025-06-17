# importa biblioteca
import math
import os

def calcular_area_circulo(raio):
  return math.pi * (raio ** 2)
import math

def calcular_comprimento_circunferencia(raio):
  comprimento = 2 * math.pi * raio
  return comprimento

# Exemplo de uso
raio = int(input("Informe o raio do circulo que deseja calcular: "))
area = calcular_area_circulo(raio)
os.system("cls")
print(f"A área do círculo com raio {raio} é: {area:.2f}: ")
comprimento = calcular_comprimento_circunferencia(raio)
print(f"O comprimento da circunferência com raio {raio} é: {comprimento:.2f}")