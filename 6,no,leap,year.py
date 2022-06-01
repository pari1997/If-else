year=int(input("enter year"))
if year%4==0 and year%100!=0:
    print(year,"is leap year")
elif year%100==0 and year%400==0:
    print(year,"is a leap year")
else:
    print("not a leap year")