num = input()
ans = ""

for i in range(len(num)):
    sub = 9 - int(num[i])
    if i == 0 and sub == 0:
        ans += str(num[i])
    elif i == 0 and int(num[i]) == 0:
        ans += str(sub)

    else:
        _min = min(sub, int(num[i]))
        ans += str(_min)

print(ans)