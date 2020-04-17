import math
x=[]
for i in range(2):
    x.append(int(input()))

value=x[0]/x[1]

angle=round(math.degrees(math.atan(value)))
print(str(int(angle))+'°')
