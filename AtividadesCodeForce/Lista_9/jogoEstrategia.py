j, r = map(int, input().split())
pontos = list(map(int, input().split()))
pontuacoes = [0] * j

for i in range(len(pontos)):
    jogador = i % j
    pontuacoes[jogador] += pontos[i]

vencedor = 0
maior_pontuacao = 0
for i in range(j):
    if pontuacoes[i] >= maior_pontuacao:
        maior_pontuacao = pontuacoes[i]
        vencedor = i + 1

print(vencedor)