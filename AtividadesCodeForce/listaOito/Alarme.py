while True:
    entrada = input()

    h1, m1, h2, m2 = map(int, entrada.split())
    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break
    minutos_inicio = h1 * 60 + m1
    minutos_fim = h2 * 60 + m2

    if minutos_fim < minutos_inicio:
        minutos_fim += 24 * 60

    print(minutos_fim - minutos_inicio)