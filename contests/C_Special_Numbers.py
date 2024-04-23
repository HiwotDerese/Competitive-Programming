test = int(input())

for i in range(test):
    n,k = list(map(int, input().split()))
    ans, index = 0, 0
    # print(n, k, ans)
    while k:
        if k % 2 != 0:
            ans += n ** index
        k >>= 1
        index += 1

    print(ans % 1000000007)
