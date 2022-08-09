copies = input("enter no. of copies:")
price = input("enter book price:")
try:
    copies,price = float(copies),float(price)
    total_cost = (price*.6*copies)+3+(.75*(copies-1))
    print("Total Cost :"+str(total_cost))
except Exception as e :
    # print(e)
    print("Please enter a number")
