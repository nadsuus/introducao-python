d = int(input())
v = int(input())
tempo = d/v
tempoEmSegundos = tempo * 3600
horas = tempoEmSegundos // 3600;
minutos = (tempoEmSegundos / 60)%60
print("%02d:%02d" % (horas, minutos))