import math
angle = float(input('type the angle of triangle:'))

# math.radians(angle)
angleRadian = (math.pi * angle)/180

sin = math.sin(angleRadian)
cos = math.cos(angleRadian)
tan = math.tan(angleRadian)

print('angle = {}\nsin = {:.2f}\ncos = {:.2f}\ntan = {:.2f}'.format(angle, sin, cos, tan))
