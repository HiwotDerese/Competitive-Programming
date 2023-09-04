from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    parent = list(map(int, input().split()))

    color = input()
    store =  defaultdict(int)

    for i in range(n):
        if i + 1 not in store:
            if color[i] == "W":
                store[i + 1] += 1

            else:
                store[i + 1] -= 1

    for i in range(n - 2, -1, -1):
        store[parent[i]] += store[i + 2]

    ans = 0
    for par in store:
        if store[par] == 0:
            ans += 1

    print(ans)


