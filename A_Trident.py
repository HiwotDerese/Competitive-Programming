test = int(input())
for i in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    f = True

    left_min = [arr[0]]
    right_min = [arr[-1]]
    for i in range(2, n - 1):
        left_min.append(min(left_min[-1], arr[i-1]))

    for i in range(-3, -n, -1):
        right_min.append(min(right_min[-1], arr[i + 1]))

    right_min.reverse()

    f = True
    for i in range(1, n - 1):
        if arr[i] > left_min[i - 1] and arr[i] > right_min[i - 1]:
            print("YES")
            left_min_idx = arr.index(left_min[i - 1])
            right_min_idx = arr.index(right_min[i - 1])
            print(left_min_idx + 1, i + 1, right_min_idx + 1)
            f = False
            break

    if f:
        print("NO")