from os import system

def menu():
	system('cls')
	print('\n*** Calculadora básica ***\n')
	print('Escolha:\n')
	print('1. Soma')
	print('2. Subtração')
	print('3. Multiplicação')
	print('4. Divisão')
	op = int(input('\nOpção: '))
	return op


def entrada():
	n1 = float(input('\nDigite o 1º nº: '))
	n2 = float(input('Digite o 2º nº: '))
	return n1, n2


def exibir(n1, n2, resulta, sinal):
	print(f'\n{n1} {sinal} {n2} = {resulta}\n')


def somar(n1, n2):	
	exibir(n1, n2, (n1+n2), '+')


def subtrair(numero1, numero2):
	exibir(numero1, numero2, numero1-numero2, '-')


def multiplicar(n1, n2):
	exibir(n1, n2, n1*n2, 'x')


def dividir(n1, n2):
	exibir(n1, n2, n1/n2, ':')


if __name__ == '__main__':
	op = menu()
	num1, num2 = entrada()

	match op:
		case 1:
			somar(num1, num2)
		case 2:
			subtrair(num1, num2)
		case 3:
			multiplicar(num1, num2)
		case 4:
			dividir(num1, num2)
		case _:
			menu()
