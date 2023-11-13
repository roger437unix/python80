import requests, json

cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
cotacao = cotacao.json()

taxa = float(cotacao['USDBRL']['bid'])

print(taxa)