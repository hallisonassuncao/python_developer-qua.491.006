# declaracao de variaveis
x = float(input("Informe o valor de x: ").replace(",", "."))
y = float(input("Informe o valor de y: ").replace(",", "."))

# soma
print(f"{'-'*20} escolha a operação {'-'*20}\n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# usuario escolhe a operacao desejada
operador = input(" Informe a operacao desejada: ").strip()

 # match case
match operador: 
    case"1":
        print(f" A soma dos valores é {x+y}.")
    case "2": 
        print(f" A subtracao dos valores é {x-y}.")   
    case "3":
        print(f" A Multiplicação dos valores é {x*y}.")  
    case "4":
         print(f" A Divisão dos valores é {x/y}.")   
    case _: # default
        print("Operação invalida.")        

