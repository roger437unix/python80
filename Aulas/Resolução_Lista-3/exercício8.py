'''
Idêntico ao anterior, porém, se o número não for primo, indicar todos os
números pelo qual este é divisível.
'''

import sys
from os import system

system('cls')

print()
while True:
	n = int(input('Informe um nº positivo >=2: '))
	if n >= 2:
		break

ehprimo = True

for i in range (2, n//2+1):
	if n % i == 0:
		if ehprimo:
			print(f'\n{n} não é primo, pois é divisível por:\n')		
			ehprimo = False
		print(f'{i}', end='  ')

if ehprimo:
	print(f'\n{n} é primo.\n')
else:
	print('\n')
