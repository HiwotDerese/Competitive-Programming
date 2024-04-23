from cmath import inf

s = input()
n = len(s)

if n < 4:
    print("NO")

else:
    left, right, found, idx1, idx2  = 0, 2, set(), [], []

    while right < n + 1:
        sub = s[left:right]
        if sub == "AB":
            found.add(sub)
            idx1.append(left)

        if sub == "BA":
            found.add(sub)
            idx2.append(left)

        left += 1
        right += 1

    if len(found) < 2 or len(idx1) == 0 or len(idx2) == 0:
        print('NO')

    elif idx1[-1] > idx2[-1]:
        if idx1[-1] - idx2[0] == 1:
            print("No")
        else:
            print("YES")

    elif idx2[-1] > idx1[-1]:
        if idx2[-1] - idx1[0] == 1:
            print("NO")
        else:
            print("YES")

    else:
        print("YES") 
