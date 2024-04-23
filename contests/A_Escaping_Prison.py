test = int(input())

for i in range(test):
    n, h = map(int, input().split())

    max_ = 0
    for j in range(n):
        w, l = map(int, input().split())
        max_ += max(w, l)

    if max_ >= h:
        print("YES")
    else:
        print("NO")