t = int(input())
for _ in range(t):
    d, n = map(int, input().split())
    precos = list(map(float, input().split()))
    max_troco = 0.0
    for preco in precos:
        if preco <= d:
            troco = d % preco
            max_troco = max(max_troco, troco)

    print(f"{max_troco:.2f}")