import click

click.clear()

x = [int(x) for x in input('\nInforme o valor de x1: ').split()]

x1 = x[0]
x2 = x[1]

w1 = .7
w2 = .6
bias = -.6

# Potencial de ativação [u]
u = x1*w1 + x2*w2 + bias

# Função de ativação [y]
if u >= 0:
	print(f'\n{x1} E {x2} = 1\n')
else:
	print(f'\n{x1} E {x2} = 0\n')
