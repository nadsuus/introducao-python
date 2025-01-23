C = int(input())
D = int(input())
T = int(input())

necessario = D / C
if T >= necessario:
    comprar = 0.0
else:
    comprar = necessario - T
    comprar = round(comprar + 1e-8, 1) 

print("{:.1f}".format(comprar))
