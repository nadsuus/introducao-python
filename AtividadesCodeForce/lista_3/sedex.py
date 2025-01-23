diametroN = int(input())
a,l,p = map(int,input().split())
if(diametroN > a or diametroN > l or diametroN > p):
    print("N")
else:
    print("S")