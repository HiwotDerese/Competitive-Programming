n, a, b = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

if h[b - 1] == h[b]:
    print(0)

else:
    print(h[b] - h[b - 1])

