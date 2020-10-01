def sum(x,y):
    s=0
    for i in range (x,y+1):
        s=s+i
    return s

x=int(input("enter the number"))
y=int(input("enter the number"))

print(sum(x,y))
