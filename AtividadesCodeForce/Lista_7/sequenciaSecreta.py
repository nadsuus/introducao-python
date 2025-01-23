n = int(input())
sequencia = [int(input()) for _ in range(n)]
marcados = 1

for i in range(1, n):
    if sequencia[i] != sequencia[i - 1]:
        marcados += 1
print(marcados)