from os import system

system('cls')

n = int(input("Digite um nº inteiro >= 0: "))

if n % 2 == 0:
	print(f"\n{n} é par\n")
else:
	print(f"\n{n} é impar\n")