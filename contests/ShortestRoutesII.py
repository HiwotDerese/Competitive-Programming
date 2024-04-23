from cmath import inf
n, m, q = list(map(int, input().split()))

dist = [[inf] * n for _ in range(n)]

for idx in range(m):
    a, b, c = list(map(int, input().split()))
    dist[a-1][b-1] = min(dist[a-1][b-1], c)
    dist[b-1][a-1] = min(dist[b-1][a-1], c)

for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(q):
    query = list(map(int, input().split()))
    ans = dist[query[0] - 1][query[1] - 1]
    print(-1 if ans == float(inf) else ans)















