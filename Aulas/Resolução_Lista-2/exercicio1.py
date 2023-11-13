'''
Crie um programa em Python que solicite a idade do usuário e informe se este e menor ou
maior de idade. Considere avaliar se a idade é válida, sendo que esta não pode ser menor
que zero ou maior que cento e vinte anos.
'''
from os import system

system('cls')

idade = int(input('Informe sua idade: '))

if idade > 0:
	if idade <= 120:
		if idade >= 18:
			print('\nMaior de idade\n')
		else:
			print('\nMenor de idade\n')
	else:
		print(f'\n{idade} Idade inválida\n')
else:
	print(f'\n{idade} Idade inválida\n')
