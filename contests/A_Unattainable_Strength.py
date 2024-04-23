n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 1
for i in range(n):
    if arr[i] > ans:
        break
    ans += arr[i]
print(ans)

