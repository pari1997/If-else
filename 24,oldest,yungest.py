a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a>b and a>c:
    print("oldest")
elif b>a and b>c:
    print("oldest")
elif c>a and c>b:
    print("oldest")
elif a<b and a<c:
    print("a is youngest")
elif b<a and b<c:
    print("b is youngest")
elif c<a and c<b:
    print("c is youngest")
else:
    print("all are equal")