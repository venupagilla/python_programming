import math
def calc(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

x1=10
y1=20
x2=56
y2=50
print(f"The distance between points ({x1},{y1}) and ({x2,y2}) is {int(calc(x1,y1,x2,y2))}")