'''
Idêntico ao anterior, porém, se o número não for primo, indicar o primeiro
número (exceção do número 1) que este é divisível.
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
		print(f'\n{n} não é primo, pois é divisível por: {i}\n')
		sys.exit()

print(f'\n{n} é primo.\n')
