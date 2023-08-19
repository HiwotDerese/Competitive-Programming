test = int(input())

for i in range(test):
    s = input()
    s += " "
    res = set()

    idx = 0
    while idx < (len(s) - 1):
        if s[idx] != s[idx + 1]:
            res.add(s[idx])
            idx += 1
        
        elif s[idx] == s[idx + 1]:
            idx += 2

    sorted_list = sorted(res)

    ans = ''.join(sorted_list)

    print(ans)
