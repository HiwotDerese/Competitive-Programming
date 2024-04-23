n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
forward = [0] * (n + 1)
backward = [0] * (n + 1)

for i in range(1, n + 1):
    forward[i] = forward[i - 1] + a[i - 1]

for i in range(n - 1, -1, -1):
    backward[i] = backward[i + 1] + a[i]

for i in range(q):
    x, y = map(int, input().split())
    total = forward[-1] - forward[n - x] - backward[n - x + y]
    print(total)
