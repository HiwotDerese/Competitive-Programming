test = int(input())

for i in range(test):
    s = input()

    w = s[0]
    idx, cnt, f = 0, 0, 0
    while idx < len(s):
        if s[idx] == w:
            cnt += 1

        elif cnt == 1:
            f = 1
            print("NO")
            break

        else:
            cnt = 1

        w = s[idx]
        idx += 1

    if cnt == 1 and f == 0:
        print("NO")

    elif f == 0:
        print("YES")



