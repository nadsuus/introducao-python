c = int(input())
valores = [int(input()) for _ in range(c)]
saldo = 100
max_saldo = saldo
for valor in valores:
    saldo += valor
    max_saldo = max(max_saldo, saldo)
print(max_saldo)