n = int(input())
valorInserido = n
notas = [100,50,20,10,5,2,1]
print(valorInserido)

for nota in notas:
    quantidade = n // nota
    n %= nota
    print(f"{quantidade} nota(s) de R$ {nota},00")