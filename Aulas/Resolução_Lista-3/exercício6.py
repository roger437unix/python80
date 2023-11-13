'''
Usuário digita um número inteiro maior que ‘1’ e programa informa se este é
ou não primo.
'''

import sys
from os import system

system('cls')

print()
while True:
	n = int(input('Informe um nº positivo >=2: '))
	if n >= 2:
		break

for i in range (2, n//2+1):
	if n % i == 0:
		print(f'\n{n} não é primo.\n')
		sys.exit()

print(f'\n{n} é primo.\n')
