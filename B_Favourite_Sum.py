test = int(input())

for i in range(test):

    n, x = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    nums.sort()
    ans = x * (x+1) // 2
    # print(ans)

    for num in nums:
        if num <= x:
            ans -= (2 * num)

    print(ans)

