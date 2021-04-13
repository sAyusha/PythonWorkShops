'''Given a positive real number, print its fractional part.'''
import math
a=float(input("Enter the positive real number:"))
math.modf(a)
#return the fractional and integer parts of x. Both results carry the sign of x and are floats.
x,y=math.modf(a)
print(x)
print(y)

