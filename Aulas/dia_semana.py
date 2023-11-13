import click

click.clear()

dia = int(input('\nInforme o dia na forma numérica: '))

match dia:
	case 1:
		print('\nsegunda\n')
	case 2:
		print('\nterça\n')
	case 3:
		print('\nquarta\n')
	case 4:
		print('\nquinta\n')
	case 5:
		print('\nsexta\n')
	case 6:
		print('\nsábado\n')
	case 7:
		print('\ndomingo\n')
	case _:
		print('\nDia inválido\n')



