import math
l, d, k = list(map(int, input().split()))

lane = math.ceil((k/(d * 2)))
a = ((2 * d) * lane) - (2 * d) - 1

desk = k - a
print(a)
print('*******************')
print(desk)

if desk == 0: 
    print(lane, 1, "L")
elif desk == 1:
    print(lane, 1, "R")

else:
    if desk % 2 == 0:
        print(lane, desk - 1, "L")
    else:
        print(lane, desk, "R")
