import math
from os import system

def radiano(angulo):
	return angulo * math.pi / 180


if __name__ == '__main__':
	system('cls')
	ang = float(input(f'\nInforme a medidado do ângulo [0° ... 360°]: '))
	print(f'\n{ang}° equivale {radiano(ang)} radianos\n')
