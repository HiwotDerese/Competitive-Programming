n = int(input())
x, y = set(), set()

for i in range(n):
    s = input()
    for j in range(n):
        if i == j or i + j == n - 1:
            x.add(s[j])
        else:
            y.add(s[j])

if len(x) == 1 and len(y) == 1 and list(x)[0] != list(y)[0]:
    print("YES")
else:
    print("NO")
