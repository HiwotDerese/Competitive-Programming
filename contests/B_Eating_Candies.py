test = int(input())

for i in range(test):
    n = int(input())
    arr = list(map(int, input().split()))

    lpre_sum = [arr[0]]
    rpre_sum = [arr[-1]]

    for idx in range(1, n):
        lpre_sum.append(lpre_sum[idx - 1] + arr[idx])
        rpre_sum.append(rpre_sum[idx - 1] + arr[-(idx + 1)])


    rpre_sum = rpre_sum[::-1]
    # print(rpre_sum)

    left, right, ans = 0, n - 1, 0

    while left < right:
        # print(lpre_sum, "left")
        # print(rpre_sum, "right")
        # print(left, right)
        if lpre_sum[left] == rpre_sum[right]:
            ans = (left + 1 + n - right)
            left += 1
            right -= 1

        elif lpre_sum[left] < rpre_sum[right]:
            left += 1

        else:
            right -= 1


    print(ans)
