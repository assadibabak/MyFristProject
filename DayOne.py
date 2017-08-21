



def myAdd(x,y):
    sum = x+y+aa
    sam = 5
    return sum


myList = [1,2,3,"Bob"]
print(myList)
print(myList[3])
myList.append('Toad')
print(myList)

ab = list(range(0,10,2))
print(ab)

for i in range(1,15,4):
    print(i)

ac = list(range(0,31,2))
print(ac)
print(ac[5:22:2])
print(ac[5:22:2][1:6:2])

a2dList = [myList,[1,3,6,8]]

print(a2dList)
print(a2dList[0])
print(a2dList[1])
print(a2dList[1][1:])
print(len(a2dList))

aa = 7
print(myAdd(2,3))
# print(sam)

babak = myAdd
print(babak(1,1))

if aa == 7:
    print("yes")
elif aa==3:
    print("3")
else:
    pass

import numpy as np

toad = np.array(range(0,100,10))
print(toad)

print(toad[toad>35])

print(" I made a change")