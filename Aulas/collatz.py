'''
Cenário
Em 1937, um matemático alemão chamado Lothar Collatz formulou uma hipótese intrigante (ainda não comprovada) que pode 
ser descrita da seguinte forma:

pegue qualquer número inteiro diferente de zero e diferente de zero e nomeie-o como c0;
se for par, avalie um novo c0 como c0 ÷ 2;
caso contrário, se for ímpar, avalie um novo c0 como 3 × c0 + 1;
se c0 ≠ 1 , volte ao ponto 2.
A hipótese diz que, independentemente do valor inicial de c0, ela sempre vai para 1.

Obviamente, é uma tarefa extremamente complexa usar um computador para provar a hipótese de qualquer número natural 
(pode até exigir inteligência artificial), mas você pode usar o Python para verificar alguns números individuais. 
Talvez você até encontre aquele que refutaria a hipótese.

Escreva um programa que leia um número natural e execute as etapas acima, desde que c0 permaneça diferente de 1. 
Também queremos que você conte as etapas necessárias para atingir o objetivo. Seu código deve gerar todos os valores 
intermediários de c0 também.
'''

import click

click.clear()

c0 = int(input('\nInforme um nº qq inteiro diferente de zero: '))
etapas = 0

print()
while c0 != 1:
	etapas += 1
	if c0 % 2:
		c0 = c0 * 3 + 1
	else:
		c0 /= 2
	print(int(c0))
print(f'\nEtapas: {etapas}\n')