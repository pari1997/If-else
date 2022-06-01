attendence=int(input("enter class attendence"))
classes=int(input("enter class held"))
percentege=attendence/classes*100
if percentege>=75:
    print(percentege,"student allow to sit the exm")
else:
    print(percentege,"student not allow to sit the exm")
