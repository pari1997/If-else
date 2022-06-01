a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a>c and a<b:
    print(a,"is second largest")
elif b>c and b<a:
    print(b,"is second largest")
elif c>a and c<b:
    print(c,"is second largest")
elif a>b and b>c:
    print(b,"second largest")
elif a>b and a<c:
    print(a,"second largest")
elif b>a and b<c:
    print(b,"second lardest")
else:
    print("erorr")