from typing import Counter


n = int(input())

if n % 4 != 0:
    print("===")
    exit()

s = input()
targ = n // 4

dic = Counter(s)
if dic['A'] > targ or dic['C'] > targ or dic['G'] > targ or dic['T'] > targ:
    print("===")

else:
    ans = ["A"] * n
    for i in range(n):
        if s[i] == "?":
            if dic['A'] < targ:
                ans[i] = "A"
                dic['A'] += 1
            elif dic['C'] < targ:
                ans[i] = "C"
                dic['C'] += 1
            elif dic['G'] < targ:
                ans[i] = "G"
                dic['G'] += 1
            elif dic['T'] < targ:
                ans[i] = "T"
                dic['T'] += 1
            else:
                print("===")
                exit()

        else:
            ans[i] = s[i]
    print("".join(ans))