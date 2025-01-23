n=int(input())
divisores = []
for i in range(1,n+1,1):
    if n%i==0:
        divisores.append(i) 
print(" ".join(map(str, divisores)))