month=input("enter month")
a=("jan,march,may,july,oct,aug,dec")
b=("apl,jun,sep,nov")
if month in (a):
    print("31 days")
elif month in (b):
    print("30 day")
else:
    print("28 day")