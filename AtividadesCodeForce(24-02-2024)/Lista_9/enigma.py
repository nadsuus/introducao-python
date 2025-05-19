mensagem = input().strip()
crib = input().strip()

tamanhoMensagem = len(mensagem)
tamanhoCrib = len(crib)

posicoesValidas = 0

for i in range(tamanhoMensagem - tamanhoCrib + 1):
    valido = True
    for j in range(tamanhoCrib):
        if mensagem[i + j] == crib[j]:
            valido = False
            break
    if valido:
        posicoesValidas += 1
        
print(posicoesValidas)