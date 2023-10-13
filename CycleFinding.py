from cmath import inf

n, m = map(int, input().split())

graph = []

for _ in range(m):
    edge = list(map(int, input().split()))
    graph.append(edge)

dist = [inf] * n
dist[0] = 0
path = [""] * n

for _ in range(n - 1):
    for u, v, w in graph:
        if dist[u - 1] != inf and dist[u - 1] + w < dist[v - 1]:
            dist[v - 1] = dist[u - 1] + w

found = False
for u, v, w in graph:
    if dist[u - 1] != inf and dist[u - 1] + w < dist[v - 1]:
        if dist[u - 1] + w < 0:
            print("YES")
            print(path[v - 1])
            found = True

        dist[v - 1] = dist[u - 1] + w
        path[v - 1] = path[u - 1] + str(v) if path[u - 1] else str(u) + str(v)

        

if not found:
    print("NO")







