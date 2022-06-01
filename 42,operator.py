num1=int(input("enter number"))
num2=int(input("enter number"))
operator=input("enter any mathematical operator")
if operator=='+':
    print(num1+num2,"is the sum of the number")
elif operator=='-':
    print(num1-num2,"is the substract of the number")
elif operator=='*':
    print(num1*num2,"is the multiply of the number")
elif operator=='/':
    print(num1/num2,"is the divide of the number")
elif operator=='%':
    print(num1%num2,"is the modulus of the number")
elif operator=='**':
    print(num1**num2,"is the exponent of the number")
elif operator=='//':
    print(num1//num2,"is the floor division of the number")
else:
    print("is not mathamatical operator")

