inp = input("enter Celsius Temp:")
try:
    cel = float(inp)
    fahr = (cel*9.0/5.0)+32.0
    print(fahr)
except:
    print("Please enter a number")