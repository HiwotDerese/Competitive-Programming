test = int(input())

for i in range(test):
    arr = list(map(int, input().split()))

    arr.sort()

    if arr[2] + arr[1] >= 10:
        print("YES")

    else:
        print("NO")

