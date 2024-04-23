test = int(input())

for i in range(test):
    l, r = map(int, input().split())
    # print(l, r)
    x = l
    while x < r:
        if x * 2 <= r:
            print(x, x*2)
            break
        else:
            x += 1
