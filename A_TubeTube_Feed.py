test = int(input())

for _ in range(test):
    n, t = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_, sat = -1, 0

    for i in range(n):
        if a[i] <= t and b[i] >= sat:
            max_ = i + 1
            sat = b[i]
        t -= 1
    print(max_)


