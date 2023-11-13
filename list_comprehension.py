# Retorna uma lista de números aleatórios e primos

from random import randint
from click import clear

clear()

def primo():	
	while True:
		ref = True
		n = randint(2, 10_000)
		for i in range(2, n//2+2):
			if not n % i:
				ref = False
				break
		if ref:
			return n

lista = [primo() for i in range(10)]

print(f'\n{lista}\n')
