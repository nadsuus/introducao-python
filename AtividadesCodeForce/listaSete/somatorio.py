def somatorio(n):
    soma = sum(1 / i for i in range(1, n + 1))
    return f"{soma:.4f}"
n = int(input())
print(somatorio(n))
