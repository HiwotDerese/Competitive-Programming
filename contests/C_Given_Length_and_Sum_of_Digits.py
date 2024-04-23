m, s = map(int, input().split())
ans = ""
while s > 0:
    if s > 9:
        ans += "9"
        s -= 9

    else:
        ans += str(s)
        s = 0

n = len(ans)
if not ans or n > m:
    print(-1, -1)

elif n == m:
    min_ = "".join(sorted(ans))
    # print(ans)
    max_ = ans
    print(min_, max_)
# else:

else:
    max_ = 
    while n < m:
