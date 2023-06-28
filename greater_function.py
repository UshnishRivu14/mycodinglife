def greatnum(a,b):
    if (a>b):
        print(a ," is greater thean ", b)
    elif (a==b):
        print(a ," is equal to ",b)    
    else:
        print(b ,"is greater than ", a)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

greatnum(a,b)