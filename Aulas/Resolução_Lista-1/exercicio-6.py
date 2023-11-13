from os import system

system('cls')

preco_prod = float(input("\nPreço do produto? "))
desc_percent = float(input('Valor do desconto? '))

desc_monetario = (preco_prod * desc_percent) / 100
valor_final = preco_prod - desc_monetario

print(f'\nPreço do produto: R$ {preco_prod}')
print(f'% de desconto: {desc_percent}')
print(f'Valor a pagar: R$ {valor_final}\n')
