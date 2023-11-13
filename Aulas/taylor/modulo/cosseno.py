from os import system
from fatorial import fatorial as fat
from radiano import radiano as rad


def cosseno(angulo):
	x = rad(angulo)
	cos = 1
	ref = True

	for i in range(2, 160+2, 2):
		if ref:
			cos -= x**i / fat(i)
			ref = False
		else:
			cos += x**i / fat(i)
			ref = True
	return round(cos, 4)


if __name__ == '__main__':
	system('cls')
	ang = float(input('\nInforme o ângulo: '))
	print(f'\nO cosseno de {ang}: {cosseno(ang)}\n')
