n = int(input())
for _ in range(n):
    c = float(input())
    dias = 0

    while c > 1.0:
        c /= 2
        dias += 1

    print(f"{dias} dias")
