a =10
b=10

if (a>b):
    print("a is greater")
elif(a==b):
    print("a and b are equal")
else:
    print("b is greater")

print("A") if a > b else print("B")


print("A is greater") if a>b else print("b") if a==b else print("B")