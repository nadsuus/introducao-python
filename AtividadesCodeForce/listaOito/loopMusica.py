while True:
    n = int(input())
    if n == 0:
        break

    alturas = list(map(int, input().split()))

    picos = 0
    for i in range(n):
        anterior = alturas[i - 1]
        atual = alturas[i]
        proximo = alturas[(i + 1) % n]
        if (atual > anterior and atual > proximo) or (atual < anterior and atual < proximo):
            picos += 1

    print(picos)