n, k = map(int, input().split())

h = list(map(int, input().split()))

min_ = sum(h[:k])
ans = min_
left, right = 0, k
idx = 1

while right < n:
    temp = ans
    ans = min(ans,  min_ - h[left] + h[right])

    if temp != ans:
        idx = left + 2

    min_ = min_ - h[left] + h[right]
    left += 1
    right += 1

print(idx)
