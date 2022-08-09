import math
inp = input("Enter the radius of sphere:")
try:
    rad = float(inp)
    vol = 4/3*math.pi*rad**3
    print(vol)
except:
    print("please enter number")
    