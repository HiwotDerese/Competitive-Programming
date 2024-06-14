n = int(input())

arr = map(int, input().split())
c = m = s = 0
for i in arr:
    if i < s:
        c = 1
    else:
        c += 1
    m = max(m, c)
    s = i


print(m)