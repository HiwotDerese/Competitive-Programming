n, s = map(int, input().split())

arr = list(map(int, input().split()))
ans, left, sum_ = 0, 0, 0

for right in range(n):
    sum_ += arr[right]

    while sum_  >= s:
        ans += (n - right)
        sum_ -= arr[left]
        left += 1

print(ans)

