a,b,c,d = map(float,input().split())

if( a < b + c ):
    print("S")
elif(b < a + c):
    print("S")
elif(c < a + b):
    print("S")
# --------------------------------
elif(b < c + d):
    print("S")
elif(c < b + d):
    print("S")
elif(d < b + c):
    print("S")
# ---------------------------------
elif(b < c + d):
    print("S")
elif(c < b + d):
    print("S")
elif(d < b + c):
    print("S")
# --------------------------------
elif(d < c + a):
    print("S")
elif(c < d + a):
    print("S")
elif(a < c + d):
    print("S")
# --------------------------------
elif(d < b + a):
    print("S")
elif(b < d + a):
    print("S")
elif(a < d + b):
    print("S")

else:
    print("N")