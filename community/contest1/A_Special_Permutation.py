test = int(input())

for i in range(test):
    n = int(input())
    arr = [n]
    for j in range(1, n):
        arr.append(j)

    print(*arr)