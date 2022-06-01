a=float(input("enter number"))
b=float(input("enter number"))
c=float(input("enter number"))
if a>=b and c>=a:
    print(a,"is medium")
elif b>=a and c>=b:
    print(b,"is medium")
elif c>=a and b>=c:
    print(c,"is medium")