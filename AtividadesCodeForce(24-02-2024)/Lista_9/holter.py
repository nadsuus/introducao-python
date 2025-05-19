n = int(input())

medicoes = []
for i in range(n):
    b = int(input())
    medicoes.append(b)

mediaDeBatimentos = sum(medicoes) / len(medicoes)
mediaDeBatimentos = int(mediaDeBatimentos)

# Define os limites de 10% da média
limiteAbaixo = int(mediaDeBatimentos * 0.9)
limiteAcima = int(mediaDeBatimentos * 1.1)
mediaDiferente = 0
for batimento in medicoes:
    if batimento < limiteAbaixo or batimento > limiteAcima:
        mediaDiferente += 1

print(mediaDeBatimentos)
print(mediaDiferente)
