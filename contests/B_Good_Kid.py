from math import prod


test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr[0] += 1
    print(prod(arr))