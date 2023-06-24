import random
name1 = input('What\'s your name: ')
name2 = input('What\'s your name: ')
name3 = input('What\'s your name: ')
name4 = input('What\'s your name: ')
# list = [name1, name2, name3, name4]
# random.shuffle(list)
# print(list)
s = random.sample([name1, name2, name3, name4], k=4)
print(s)
