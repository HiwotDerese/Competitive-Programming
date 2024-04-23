test = int(input())

for i in range(test):
    x = int(input())
    if x == 1:
        print(3)
    
    else:
        num = (x - (x & (x - 1)))
        num2 = (x & (x - 1))
        if x % 2 != 0:
            print(1)

        elif num2 == 0:
            print(num + 1)

        else:
            print(num)


