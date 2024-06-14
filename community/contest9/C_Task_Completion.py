test = int(input())

for _ in range(test):
    n = int(input())
    start = list(map(int, input().split()))
    finish = list(map(int, input().split()))

    ans = []
    s = 0
    for i in range(n):
        if s >= start[i]:
            time = finish[i] - s

        else:
            time = finish[i] - start[i]

        ans.append(time)

        s = finish[i]

    print(*ans)