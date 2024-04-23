test = int(input())

for _ in range(test):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    l, r= 0, 1

    while r < len(a):
        # print(l, r, a)
        diff = a[r] - a[l]
        if diff == 1 or diff == 0:
            a = a[1:]

        else:
            break

    if len(a) == 1:
        print("YES")

    else:
        print("NO")

