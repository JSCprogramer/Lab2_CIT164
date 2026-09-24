#this is the part 3 of lab 2 to find the distance between them#
import math

x1=float(input('Enter x-coordinate for Point 1:'))
y1=float(input('Enter y-coordinate for Point 1:'))
x2=float(input('Enter x-coordinate for Point 2:'))
y2=float(input('Enter y-coordinate for Point 2:'))

total=math.sqrt((x2-x1)**2+(y2-y1)**2)
print('The distance between the two points:',round(total,2))


