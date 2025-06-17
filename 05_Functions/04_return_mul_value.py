# Question 4 - Function returning multiple values.
# Statement: Create a function that return both the area and circumference of a circle given ite radius.

radius = 7

def areaCircum(r):
   area = 22/7 * (r*r)
   curcum = 2*22/7*r
   return area, curcum

circle_area,circle_circum = areaCircum(radius)

print("Area of Circle: ", circle_area)
print("Circumference of Circle: ", circle_circum)