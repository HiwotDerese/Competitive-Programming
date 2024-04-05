test = int(input())

for i in range(test):
    n = int(input())
    arry = list(map(int, input().split()))
    max_ = sorted(arry)
    max_ = max_[-2:]


    ans = []
    for i in range(n):
        ans.append(arry[i] - max_[-1] if arry[i] != max_[-1] else arry[i] - max_[-2])

    print(*ans)