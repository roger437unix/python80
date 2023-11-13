from os import system
import sys
sys.path.insert(1, './modulo')

from modulo.seno import seno
from modulo.cosseno import cosseno as cos


def tangente(angulo):
	if angulo == 90:
		return 'Não existe'
	return seno(angulo) / cos(angulo)


if __name__ == '__main__':
	system('cls')
	ang = float(input('\nIforme o ângulo: '))
	print(f'\nTangente {ang}: {tangente(ang)}\n')
