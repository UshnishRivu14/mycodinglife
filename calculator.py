a = int(input("Enter first number\n"))
b = int(input("Enter second number\n"))
c = input("Enter a operator between(+ , - , * , \ )\n")

if (c == "+"):
    print(a + b)
elif (c == "-"):
    print(a - b )
elif (c == '*'):
    print(a * b)
elif (c == " / "):
    print(a/b)
else :
    print("Wrong input")               