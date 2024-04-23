from cmath import inf


n, m, k = list(map(int, input().split()))

graph = []

for _ in range(m):
    edge = list(map(int, input().split()))
    graph.append(edge)

dist = [inf] * n
dist[0] = 0

for _ in range(n - 1):
    for u, v, w in graph:
        if dist[u - 1] != inf and dist[u - 1] + w < dist[v - 1]:
            dist[v - 1] = dist[u - 1] + w


# print(dist)
ans = 0
for _ in range(k):
    s, y = list(map(int, input().split()))

    if dist[s - 1] >= y:
        ans += 1

    else:
        dist[s - 1] = y

print(ans)



