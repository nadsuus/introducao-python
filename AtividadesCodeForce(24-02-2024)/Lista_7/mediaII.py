n = int(input())
numeros = list(map(int, input().split()))
media = sum(numeros) / n
abaixo = []
acima_ou_igual = []

for num in numeros:
    if num < media:
        abaixo.append(num)
    else:
        acima_ou_igual.append(num)
        
print(f"{media:.1f}")  # Média com 1 casa decimal
print(len(abaixo), " ".join(map(str, abaixo)))  # Números abaixo da média
print(len(acima_ou_igual), " ".join(map(str, acima_ou_igual)))  # Números iguais ou acima da média