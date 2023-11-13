h = [int(x) for x in input('\nInforme o horário de início [hh:mm]: ').split(':')]
duracao = int(input("Duração do evento (minutos): "))

hora = h[0]
minutos = h[1]

minutos = minutos + duracao # encontre um total de todos os minutos
hora = hora + minutos // 60 # encontre um número de horas escondido em minutos e atualize a hora
minutos = minutos % 60 # minutos corretos para cair no intervalo (0..59)
hora = hora % 24 # horas corretas para cair no intervalo (0..23)

print(f'\n{hora}:{minutos}\n')