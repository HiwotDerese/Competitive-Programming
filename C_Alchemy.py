n = int(input())
t = list(map(int, input().split()))

l = 0
r = n - 1
preL = 0
preR = 0

while r - l > 1:
    if t[l] < t[r]:
        l += 1
        t[l] += t[l - 1]

    elif t[r] < t[l]:
        r -= 1
        t[r] += t[r + 1]

    else:
        l += 1
        r -= 1
    # print(l, r)

if l == r:
    print(l+1, n-r-1)

else:
    print(l+1, n-r)