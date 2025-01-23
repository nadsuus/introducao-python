a,b = map(int,input().split())
multiplos = [];
for contador in range(a,b+1,a):
    if contador%a == 0:
        multiplos.append(contador)
print(" ".join(map(str, multiplos)))