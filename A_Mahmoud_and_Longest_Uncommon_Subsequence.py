s1 = input()
s2 = input()
n, m = len(s1), len(s2)
if s1 == s2:
    print(-1)

else:
    if n > m:
        print(n)

    else:
        print(m)

