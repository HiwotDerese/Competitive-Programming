import random


test = int(input())

for _ in range(test):

    n = int(input())
    arr = list(map(int, input().split()))

    unique = set(arr)

    if len(unique) != n:
        print("NO")

    else:
        print("YES")

        random.choice()