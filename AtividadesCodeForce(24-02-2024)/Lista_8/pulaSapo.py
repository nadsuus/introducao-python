p, n = map(int, input().split())
alturas = list(map(int, input().split()))

vitoria = True
for i in range(1, n):
    if abs(alturas[i] - alturas[i - 1]) > p:
        vitoria = False
        break

if vitoria:
    print("YOU WIN")
else:
    print("GAME OVER")