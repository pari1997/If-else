actual_cost=int(input("enter amount"))
selling_cost=int(input("enter amount"))
if actual_cost>selling_cost:
    print("lose=",actual_cost-selling_cost)
elif actual_cost<selling_cost:
    print("profit=",selling_cost-actual_cost)
else:
    print("no lose no profit")