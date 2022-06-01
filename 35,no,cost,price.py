cp=int(input("enter number"))
if cp>100000:
    print("tex",cp*15/100)
elif cp>50000 and cp<=100000:
    print("tex",cp*10/100)
elif cp<=50000:
    print("tex",cp*5/100)
else:
    print("no tex")