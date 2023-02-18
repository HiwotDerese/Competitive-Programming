test = int(input())

for i in range(test):
    s = input()
    leng = len(s)
    l = 0
    r = 0
    ans = ""
    while r < leng:
        cnt = 0
        while r < leng and s[l] == s[r]:
            cnt += 1
            r += 1
        
        if cnt == 1:
            ans += s[l]
        l = r
    ansr = set(ans)
    print(''.join(sorted(ansr)))



