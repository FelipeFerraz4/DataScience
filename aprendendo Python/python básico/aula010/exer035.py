side1 = float(input('type the length of one side of the triangle: '))
side2 = float(input('type the length of one side of the triangle: '))
side3 = float(input('type the length of one side of the triangle: '))
cont = 0
if abs(side2-side3) < side1 < side2 + side3:
    if abs(side1-side3) < side2 < side1 + side3:
        if abs(side1 - side2) < side3 < side1 + side2:
            print('the sides form a triangle')
else:
    print('the sides not form a triangle')
