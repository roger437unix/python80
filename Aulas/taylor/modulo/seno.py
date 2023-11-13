from os import system
from fatorial import fatorial
from radiano import radiano as rad

def seno(angulo):
	x = rad(angulo)
	sin = x
	ref = True

	for i in range(3, 160+2, 2):
		if ref:
			sin -= x ** i / fatorial(i)
			ref = False
		else:
			sin += x ** i / fatorial(i)
			ref = True
	return round(sin, 4)


if __name__ == '__main__':
	system('cls')
	graus = float(input('\nInforme a medidado do ângulo: '))
	print(f'\nO seno de {graus}° : {seno(graus)}\n')
