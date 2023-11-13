'''
Mostra a série de Fibonacci, sendo que o usuário determinado a quantidade
de números desta série que deve aparecer na tela.
'''

import sys
from os import system

system('cls')

print()
while True:
	n = int(input('Informe um nº positivo para o tamanho da série de Fibonacci: '))
	if n >= 0:
		break

if n == 0:
	print()
	sys.exit()

if n == 1:
	print(f'\n1\n')
	sys.exit()

n1 = 1
n2 = 1

print(f'\n{n1}  {n2}', end='  ')

for i in range(2, n):
	print(f'**{round(n2/n1, 4)}**', end='  ')
	n3 = n1 + n2
	print(f'{n3}', end='  ')
	n1 = n2
	n2 = n3
print('\n')