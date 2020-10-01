def add(n):
    add=0
    for i in range (1,n+1):

        add+=i
    return add


x=int(input("enter the number"))
print(add(x))