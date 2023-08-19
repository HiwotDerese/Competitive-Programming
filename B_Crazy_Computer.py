n, c = map(int, input().split())

time = list(map(int, input().split()))

ans = 1

for idx in range(1, n):
    if time[idx] - time[idx - 1] <= c:
        ans += 1

    else:
        ans = 1

print(ans)