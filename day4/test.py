import random

counter = 100
mySet = set()
while counter:
    randomVal = random.randint(0,100)
    mySet.add(randomVal)
    counter -= 1
for i in range(1,101):
    if i not in mySet:
        print(i)