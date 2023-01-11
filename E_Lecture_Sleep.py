test = list(map(lambda a: int(a), input().split()))
theorems = list(map(lambda a: int(a), input().split()))
behavior = list(map(lambda a: int(a), input().split()))

_sum = 0
for i in range(test[0]):
    if behavior[i] == 1:
        _sum += theorems[i]

ans = 0
# sliding first window
for i in range(test[1]):
    if behavior[i] == 0:
        ans += theorems[i]

j = test[1]
slide = test[0] - test[1]
maxm = ans
for i in range(slide):
    if behavior[i] == 0:
        ans -= theorems[i]
    if behavior[j] == 0:
        ans += theorems[j]
    maxm = max(maxm, ans)
    j += 1

print(maxm + _sum)
