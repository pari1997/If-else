phy=int(input("enter mark"))
chem=int(input("enter mark"))
bio=int(input("enter mark"))
math=int(input("enter mark"))
com=int(input("enter mark"))
total=phy+chem+bio+math+com
per=total/500*100
if per>=90 and per<=100:
    print("grade A")
elif per>=80 and per<=89:
    print("grade B")
elif per>=70 and per<=79:
    print("grade C")
elif per>=60 and per<=69:
    print("grade D")
elif per>=40 and per<=59:
    print("grade E")
else:
    print("grade F")