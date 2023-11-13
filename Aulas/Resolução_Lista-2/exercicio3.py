'''
Crie um programa em Python que solicite que o usuário informe um número entre 1 e 7 e
exiba na tela:
Segunda-feira caso o número digitado seja 1
Terça-feira-feira caso o número digitado seja 2
...
Sábado caso o número digitado seja 6
Domingo caso o número digitado seja 7
Obs.: Caso o número que o usuário informou esteja fora do limite estabelecido deve ser
exibida uma mensagem na tela indicando que o número é inválido.
'''

from os import system

system('cls')

n = int(input('Informe o dia da semana [1...7]: '))

if n > 0:
	if n <= 7:
		if n == 1:
			print('\nSegunda-feira\n')
		else:
			if n == 2:
				print('\nTerça-feira\n')
			else:
				if n == 3:
					print('\nQuarta-feira\n')
				else:
					if n == 4:
						print('\nQuinta-feira\n')
					else:
						if n == 5:
							print('\nSexta-feira\n')
						else:
							if n == 6:
								print('\nSábado\n')
							else:
								print('\nDomingo\n')
	else:
		print('\nDia inválido\n')
else:
	print('\nDia inválido\n')
	