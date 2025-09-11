# todo- atividade: crie um programa que receba do usuario um numero inteiro e o programa calcula o valor da sequencia
# de fibonacci

n = int(input(" Digite um número: "))

a, b =0, 1
for i in range(n):
    print(a)
    a,b =b, a +b

