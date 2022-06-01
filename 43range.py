age=int(input("enter age"))
sex=input("enter number")
day=int(input("enter day"))
if age>=18 and age<=30 and sex=="m":
    total=day*700
    print("total=",total)
elif age>=18 and age<=30 and sex=="f":
    total=day*750
    print("total=",total) 
elif age>=30 and age<=40 and sex=="m":
    total=day*800
    print("total=",total)
elif age>=30 and age<=40 and sex=="f":
    total=day*850
    print("total=",total)
else:
    print("none")  
    