firstNumber = float(input('type the first number: '))
secondNumber = float(input('type the second number: '))
thirdNumber = float(input('type the third number: '))

if firstNumber >= secondNumber and firstNumber >= thirdNumber:
    higherNumber = firstNumber
    if secondNumber >= thirdNumber:
        smallerNumber = thirdNumber
    else:
        smallerNumber = secondNumber
elif secondNumber >= firstNumber and secondNumber >= thirdNumber:
    higherNumber = secondNumber
    if firstNumber >= thirdNumber:
        smallerNumber = thirdNumber
    else:
        smallerNumber = firstNumber
else:
    higherNumber = thirdNumber
    if firstNumber >= secondNumber:
        smallerNumber = secondNumber
    else:
        smallerNumber = firstNumber

print('Higher number = {}\nSmaller number = {}'.format(higherNumber, smallerNumber))
