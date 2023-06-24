from math import sqrt
base = float(input('type the base of triangle:'))
altitude = float(input('type the altitude of triangle:'))
# math.hypot(base, altitude)
hypotenuse = sqrt((base ** 2) + (altitude ** 2))
print('the hypotenuse of triangle = {:.3f}'.format(hypotenuse))
