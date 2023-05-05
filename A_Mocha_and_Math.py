test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    l = 0
    r = n - 1

    for i in range(n):
        arr[i + l] = arr[i + l] & arr[r - i]

    print(min(arr))