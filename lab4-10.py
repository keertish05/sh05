import math
a=int(input('enter any number'))
b=int(input('enter any number'))
c=int(input('enter any number'))
discriminant = b**2 - 4*a*c
if discriminant > 0:
  root1 = (-b + math.sqrt(discriminant)) / (2*a)
  root2 = (-b - math.sqrt(discriminant)) / (2*a)
elif discriminant == 0:
    root = -b / (2*a)
else:
    print(None)
 