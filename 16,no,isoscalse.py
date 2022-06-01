a=int(input("enter angle"))
b=int(input("enter angle"))
c=int(input("enter angle"))
if a==b and b==c and c==a:
    print("equilateral")
elif a+b>=c and b+c>=a and c+a>=b:
    print("isoscales")
elif a!=b and b!=c and c!=a:
    print("scalene")
else:
    print("none")