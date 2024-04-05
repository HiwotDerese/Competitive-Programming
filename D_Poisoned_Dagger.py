# For each test case, print a single integer — the minimum value of the parameter , such that Monocarp will cause at least h damage to the dragon.
import math


test = int(input())

for _ in range(test):
    n, h = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()
    
    if n == h:
        print(1)
        continue

    diff = []

    c = 1
    while c < len(arr):
        diff.append(arr[c] - arr[c-1] - 1)
        c += 1

    # diff.sort(reverse=True)
    sum_ = n
    f = 0
    i = 0
    while i < len(diff):
       
        range = n - i
        if (diff[i] * range) + sum_ < h:
            sum_ += diff[i]
        else:
            if (diff[i] * range) + sum_ == h:
                f = 1
                # print("c")
                print(diff[i])
                break
            else:
                # print(diff, i, (h - sum_), "ssss")
                # print(h, sum_, range, diff[i])
                a = math.ceil((h - sum_) / range) + 1
                f = 1
                # print("bb")
                print(a)
                break
        i += 1
    if not f:
        # print("a")
        a = h - sum_ + diff[-1]
        print(a)


