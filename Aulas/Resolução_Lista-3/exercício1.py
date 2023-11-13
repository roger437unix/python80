'''
Uma tela em modo texto que simule a autenticação no sistema. Deverá ser
solicitado login e senha. Se o usuário informar seus dados corretamente, uma
mensagem de boas-vindas deverá ser exibida, caso contrário, este somente
poderá errar três vezes.
'''

from os import system
import getpass

system('cls')

user_cad = 'Tux'
senha_cad = 'abc123'

print('\n*** Sistema Financeiro ***')
for i in range(3):	
	user = input('\nUsuário: ')
	#senha = input('Senha: ')
	senha = getpass.getpass('Senha: ')


	if user == user_cad and senha == senha_cad:
		system('cls')
		print(f'\nSeja bem-vindo Sr(a) {user}')
		break
	else:
		system('cls')
		print('\n*** Usuário ou senha  inválida ***')
		if 2-i != 0:
			print(f'\tRestam {2-i} tentativas')
		else:
			print('    *** SENHA BLOQUEADA ***')
print()