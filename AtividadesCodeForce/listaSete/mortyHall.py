n = int(input())
resultados = [int(input()) for _ in range(n)]

vitorias = 0
for portaDoCarro in resultados:
    if portaDoCarro !=1:
        vitorias += 1

print(vitorias)