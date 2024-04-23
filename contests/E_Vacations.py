n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * 3 for _ in range(n)]

if arr[0] == 2 or arr[0] == 3:
    dp[0][2] = 1

if arr[0] == 1 or arr[0] == 3:
    dp[0][1] = 1
    

for i in range(1, len(arr)):
    dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][1], dp[i - 1][2]))
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2])

    if arr[i] == 1 or arr[i] == 3:
        dp[i][1] += 1

    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1])

    if arr[i] == 2 or arr[i] == 3:
        dp[i][2] += 1

ans = n - max(dp[n - 1][0], max(dp[n - 1][1], dp[n - 1][2]))

print(ans)
