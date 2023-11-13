from os import system

# Converte a temperatura de graus celsis para fahrenheit
# Autor: Tux
# data: 28/09/2023
# Versão 1.0

# Limpa a tela
system('cls')

c = float(input('Informe a temperatura em ° Celsius: '))

# Calculando a temperatura em fahrenheit
f = (9 * c + 150) / 5

print(f'{c}° celsius equivale a {f} ° fahrenheit')