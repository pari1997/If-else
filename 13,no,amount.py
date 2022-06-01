amount=int(input("enter amount"))
if amount>=5:
    a=amount//2000
    b=amount%2000
    c=a//500
    d=a%500
    e=c//200
    f=c%200
    g=e//100
    h=e%200
    i=g//100
    j=g%100
    k=i//50
    l=i%50
    m=k//20
    n=k%20
    o=m//10
    p=m%10
    q=o//5
    print("notes of 2000",a,"notes of 500",c,"notes of 200",e,"notes of 100",g,"notes of 50",k,"notes of 20",m,"notes of 10",0,"notes of 5",q,)
else:
    print("not a amount")