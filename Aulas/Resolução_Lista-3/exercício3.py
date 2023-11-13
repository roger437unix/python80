'''
Calcula e mostra o fatorial de um número inteiro positivo.
Obs.: Por definição o fatorial de “zero” e “um” é igual a “um”.
'''

from os import system
system('cls')

print()
while True:
	n = int(input('Informe um número positivo: '))
	if n >= 0:
		break

fat = 1

for i in range(n, 1, -1):
	fat *= i

print(f'\n{n}! = {fat}\n')
