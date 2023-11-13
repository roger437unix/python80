from os import system

system('cls')

dolar = float(input("Informe o valor em dólar: U$ "))
taxa = float(input("Valor da taxa de conversão: R$ "))

real = dolar * taxa

print(f"\nU$ {dolar} equivale a R$ {round(real, 2)}.\n")
