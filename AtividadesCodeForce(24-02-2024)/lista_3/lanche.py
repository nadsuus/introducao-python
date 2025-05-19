c,q = map(int,input().split())
if(c == 1): 
    valorDoItem = 4.00
elif(c == 2):
    valorDoItem = 4.50
elif(c == 3):
    valorDoItem = 5.00
elif(c == 4):
    valorDoItem = 2.00
else:
    valorDoItem = 1.50
total = q * valorDoItem
print("Total: R$ " f"{total:.2f}")