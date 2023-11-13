from os import system

system('cls')

n = int(input("Digite um nº inteiro: "))

if n >= 0:
	print(f"\n{n} é positivo.\n")
else:
	print(f"\n{n} é negativo.\n")
