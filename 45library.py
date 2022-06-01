day=int(input("enter day"))
if day>=0 and day<=5:
    print(day*2)
elif day>=6 and day<=10:
    print(day*3)
elif day>=11 and day<=15:
    print(day*4)
elif day>=15:
    print(day*5)
else:
    print("none")