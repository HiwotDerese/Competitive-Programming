n, k = map(int, input().split())
arr = list(input().split())
ans = 0
for num in arr:
    lucky = 0

    for j in range(len(num)):
        if num[j] == '4' or num[j] == '7':
            lucky += 1

    if lucky <= k:
        ans += 1

print(ans)