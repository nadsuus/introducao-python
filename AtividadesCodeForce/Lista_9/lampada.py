n = int(input())
comandos = list(map(int, input().split()))

i1 = 0
i2 = 0

for comando in comandos:
    if comando == 1:
        i1 = 1 - i1
    elif comando == 2:
        i1 = 1 - i1
        i2 = 1 - i2

print(i1)
print(i2)
