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

# Versão 3

from os import system

system('cls')

n = int(input('Informe o dia da semana [1...7]: '))

match n:
	case 1:
		print('Segunda-feira')
	case 2:
		print('Terça-feira')
	case 3:
		print('Quarta-feira')
	case 4:
		print('Quinta-feira')
	case 5:
		print('Sexta-feira')
	case 6:
		print('Sábado')
	case 7:
		print('Domingo')
	case _:
		print('Opção inválida')
