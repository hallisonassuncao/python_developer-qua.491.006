import os
os.system

#declaracão de variaveis
nome = input("Informe seu nome: ") 
idade =  int(input("Informe sua idade: "))
altura = float(input("Informe sua altura em metros: ").replace(",", "."))

#estrutura de decisão
if idade >= 12 and altura >= 1.15:
    print(f"{nome} esta autorizado a entrar.")
else:
    print(f"{nome} não esta autorizado a entrar.")