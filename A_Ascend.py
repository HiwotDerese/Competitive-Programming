n = int(input())
a = list(map(int, input().split()))

left, right, max_ = 0, 1, 1

while right < n:
    if a[right - 1] >= a[right]:
        max_ = max(max_, right - left)
        left = right

    right += 1

max_ = max(max_, right - left)
print(max_)