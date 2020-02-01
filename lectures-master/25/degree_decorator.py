from math import sin, cos, pi

print(sin(pi/2))
print(sin(90))

def rad2deg(f):
   def f2(degrees):
     return f(pi*degrees/180)
   return f2

sin2 = rad2deg(sin)
print(sin2(pi/2))
print(sin2(90))

cos2 = rad2deg(cos)
print(cos2(pi/2))
print(cos2(90))

########################################

@rad2deg
def tan(rad):
    return sin(rad)/cos(rad)
