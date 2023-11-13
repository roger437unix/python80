from os import system

system('cls')

n = int(input('\nInforme um nº inteiro: '))

if n != 0:
	if n < 0:
		print(f'\n{n} é negativo\n')
	else:
		print(f'\n{n} é positivo\n')
else:
	print('\nÉ o zero\n')
