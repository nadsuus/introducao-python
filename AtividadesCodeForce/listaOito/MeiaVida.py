from datetime import timedelta
s, mi = map(int, input().split())

# Calculando o tempo necessário para que a massa fique menor que 0,5 gramas
tempo_total = 0  # Tempo em segundos
massa = mi

while massa >= 0.5:
    massa /= 2
    tempo_total += s
# Convertendo o tempo total para dias, horas, minutos e segundos
tempo = timedelta(seconds=tempo_total)
dias = tempo.days
horas, resto = divmod(tempo.seconds, 3600)
minutos, segundos = divmod(resto, 60)

print(f"{dias} dias {horas:02}:{minutos:02}:{segundos:02}")
