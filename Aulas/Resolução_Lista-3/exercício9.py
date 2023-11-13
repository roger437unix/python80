'''
Usuário informa um número inteiro que determina a quantidade de números
primos que devem ser listados a partir do primeiro número primo.

Informe um nº: 20

2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71
'''

import sys
from os import system
from numba import jit

system('cls')

print()
while True:
	qtde = int(input('\nInforme um inteiro >0 para qtde de nºs primos: '))
	if qtde > 0:
		break

count = 1
num = 3
ref = True

print(f'\n2', end=' ')

#@jit(nopython=True)
while count < qtde:
	for i in range(2, num//2+1):
		if num % i == 0:
			ref = False
			break
	if ref:
		print(f'{num}', end=' ')
		count += 1
	else:
		ref = True
	num += 2
print('\n')
