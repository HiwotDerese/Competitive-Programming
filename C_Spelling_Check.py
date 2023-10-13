s1 = input()
s2 = input()

n, m = len(s1), len(s2)

idx = 0
f = False
while idx < m and s1[idx] == s2[idx]:
    idx += 1

if idx != m:
    r = idx + 1
    while r < n:
        if s1[r] != s2[r - 1]:
            # print(r, idx)
            print(0)
            f = True
            break

        r += 1

if not f:
    ans = set()

    left, right = idx, idx

    while left >= 0 and s1[left] == s1[idx]:
        ans.add(str(left + 1))
        left -= 1

    while right < n and s1[right] == s1[idx]:
        ans.add(str(right + 1))
        right += 1

    ans = list(ans)
    print(len(ans))
    ans =list(map(int,ans))
    ans.sort()
    print(*ans)















