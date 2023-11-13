'''
Crie um programa em Python que a partir do peso e altura de uma pessoa, calcule e informe
o IMC (Índice de massa corpóreo) arredondado, informando também o estado da pessoa
baseado na tabela abaixo.
'''

from os import system

system('cls')

peso = float(input('\nInforme seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / altura ** 2
print(f'\nIMC: {round(imc, 1)}\n')

if imc < 17:
	print("Muito abaixo do peso\n")
elif 17 <= imc < 18.5:
	print('Abaixo do peso\n')
elif 18.5 <= imc < 25:
	print('Peso normal\n')
elif 25 <= imc < 30:
	print('Obesidade I\n')
elif 35 <= imc < 40:
	print('Obesidade II (severa)\n')
else:
	print('Obesidade III (mórbida)\n')










