test = int(input())

for i in range(test):
    n, m = list(map(int, input().split()))
    if m == 0:
        print(-1 if n > 2 else 0)
        continue
    dividers = list(map(int, input().split()))

    if n == 1:
        print(0)
    elif n == 2:
        print(0)

    else:
        arr = sorted(dividers)
        ans, count, flag = 0, 2, 0
        while arr and count < n :
            ans += 1
            count += arr[-1] - 1
            if count >= n:
                flag = 1
                print(ans)
            # print(ans, count, arr[-1])
            arr.pop()

        if flag == 0:
            print(-1)

