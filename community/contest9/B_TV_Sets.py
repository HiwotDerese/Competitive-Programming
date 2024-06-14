n, m = map(int, input().split())

arr = list(map(int, input().split()))

neg = []

for i in range(n):
    if arr[i] < 0:
        neg.append(arr[i])

neg.sort()
ans = 0

idx = 0
while idx < m and idx < len(neg):
    ans += neg[idx]
    idx += 1

print(-ans)

