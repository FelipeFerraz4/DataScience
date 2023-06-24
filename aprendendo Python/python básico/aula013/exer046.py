from time import sleep
for i in range(10, -1, -1):
    sleep(1)
    print(i)
for i in range(40, 48, 1):
    sleep(0.5)
    print('\033[0:{}:{}mfogos'.format(i-10, i))
