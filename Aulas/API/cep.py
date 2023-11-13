from click import clear
import requests, json


def via_cep(cep):
	try:
		req = requests.get(f'https://viacep.com.br/ws/{cep}/json')
		req = req.json()
		return req
	except:
		return -1


if __name__ == '__main__':
	clear()
	try:
		nome = input('\nInforme seu nome: ')
		cep = input('Informe o CEP: ')
		requisicao = via_cep(cep)
		if requisicao != -1:
			print('\n** Dados pessoas **\n')
			print(f'Nome: {nome}')
			print(f"Endereço: {requisicao['logradouro']}")
			print(f"Bairro: {requisicao['bairro']}")
			print(f"Cidade: {requisicao['localidade']}")
			print(f"Estado: {requisicao['uf']}")
			print(f"CEP: {requisicao['cep']}")
		else:
			print('\n** CEP inválido **\n')
	except KeyError:
		print('\n** CEP inválido **\n')
	except:
		print('\n** CEP inválido **\n')

