'''
Calcula e mostra o fatorial de um número inteiro positivo.
Obs.: Por definição o fatorial de “zero” e “um” é igual a “um”.
'''

from os import system

def fatorial(numero):
	fat = 1
	for i in range(numero, 1, -1):
		fat *= i
	return fat


if __name__ == '__main__':
	system('cls')
	print()
	while True:
		n = int(input('Informe um número positivo: '))
		if n >= 0:
			break

	print(f'\n{n}! = {fatorial(n)}\n')
