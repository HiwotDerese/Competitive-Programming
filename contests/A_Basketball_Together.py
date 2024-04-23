import math
# print(math.ceil(1.2))
n, d = list(map(int, input().split()))

p = list(map(int, input().split()))

l, r, ans,  = 0, len(p) - 1, 0
p.sort()
while l <= r:
    sum_ = p[r]

    if l == r:
        if sum_ > d:
            ans += 1
        break

    while l < r and sum_ <= d:
        sum_ += p[r]
        l += 1
 
    if sum_ > d:
        ans += 1
        r -= 1

print(ans)


