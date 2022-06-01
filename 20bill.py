
unit=int(input("enter unit"))
if unit>=1 and unit<=50:
    electricity_bill=unit*0.50+20/100
    print("electricity_bill",electricity_bill)
elif unit>50 and unit<=150:
    electricity_bill=unit*0.75+20/100
    print("electricity_bill",electricity_bill) 
elif unit>150 and unit<250:
    electricity_bill=unit*1.20+20/100
    print("electricity_bill",electricity_bill)
elif unit>250:
    electricity_bill=unit*1.50+20/100
    print("electricity_bill",electricity_bill)
else:
    print("none")