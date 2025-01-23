a = int(input())
b = int(input())
c = int(input())

if(a >= b and a <= c) or (a >= c and a <= b):
        print(a)
elif(b >= a and b <= c) or (a >= c and b <= a):
        print(b)
elif(c >= a and c <= b) or (a >= b and c <= a):
        print(c)