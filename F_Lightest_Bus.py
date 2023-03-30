test = int(input())

for i in range(test):
    leng = int(input())
    weight = list(map(int, input().split()))

    if leng <= 12:
        print(sum(weight))

    else:
        index = 0
        _min = sum(weight[index: index+12])

        while index < leng:
            index += 12
            _min = min(_min, sum(weight[index: index+12]))
