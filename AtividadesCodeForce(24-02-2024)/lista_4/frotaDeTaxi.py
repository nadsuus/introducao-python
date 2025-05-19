precoA,precoG,Ra,Rg = map(float,input().split())
rendimentoA = Ra /precoA
rendimentoG = Rg /precoG
if(rendimentoA > rendimentoG):
    print("A")
else:
    print("G")
