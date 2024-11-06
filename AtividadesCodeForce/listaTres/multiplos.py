a = int(input())
b = int(input())
if (a>b):
    maior = a;
    menor = b;
else:
    maior = b
    menor = a;

if (maior%menor == 0):
    print("Multiplos")
else:
    print("Nao multiplos")

