from click import clear

def fatorial(n):
	fat = 1

	for i in range(n, 1, -1):
		fat *= i
	return fat


if __name__ == '__main__':
	clear()
	while True:
		try:			
			num = int(input('\nInforme um nº inteiro: '))
			fat = fatorial(num)
			print(f'\n{num}! = {fat}\n')
			break
		except ValueError:
			print('Oops, somente nºs inteiros são aceitos.\n')
		except:
			print('Erro inesperado\n')
