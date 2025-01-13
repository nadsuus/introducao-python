n = int(input())
nlista = list(map(int,input().split()))
media = sum(nlista) / n
naMedia = 0
abaixoMedia = 0
for i in nlista:
    if i < media:
        abaixoMedia += 1
    elif i >= media:
        naMedia += 1
print(""f"{media:.1f}")
print(abaixoMedia)
print(naMedia)