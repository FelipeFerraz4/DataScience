listNumber = []
for i in range(0, 5):
    number = int(input('Type a number: '))
    count = 0
    if i == 0:
        listNumber.append(number)
    else:
        maior = listNumber.index(max(listNumber))
        if max(listNumber) > number:
            for j in range(maior-1, -1, -1):
                if number > listNumber[j]:
                    listNumber.insert(j+1, number)
                    break
                else:
                    count += 1
                if count == maior:
                    listNumber.insert(0, number)
        else:
            listNumber.append(number)
    print(listNumber)
print(listNumber)
