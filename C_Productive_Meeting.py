test = int(input())

for _ in range(test):
    n = int(input())
    soc = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append([soc[i], i + 1])

    arr.sort()
    soc.sort()
    sum_ = sum(soc[:n - 1])

    diff = sum_ - soc[-1]

    ans = []

    if diff > 0:
        l, r = 0, 1

        while sum_ > soc[-1]:
            if arr[l][0] == 0:
                l += 1
                r += 1

            else:
                ans.append([arr[l][1], arr[r][1]])
                arr[l][0] -= 1
                arr[r][0] -= 1
                sum_ -= 2

    l = 0
    while l < n - 1:
        if arr[l][0] == 0:
            l += 1

        else:
            ans.append([arr[l][1], arr[n - 1][1]])
            arr[l][0] -= 1
            arr[n - 1][0] -= 1

    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])


               