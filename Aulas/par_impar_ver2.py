'''
par_impar_ver2.py

Verifica se um número é maior ou igual a zero, caso positivo informa
se é par ou impar.

Versão 2 do programa par_impar
'''

from os import system

system('cls')

n = int(input('\nDigite um nº inteiro >= 0: '))

if n >= 0:
	if n % 2 == 0:
		print(f'\n{n} é par\n')
	else:
		print(f'\n{n} é impar\n')
else:
	print('Números negativos não são aceitos')
