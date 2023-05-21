from collections import defaultdict


n, m = map(int, input().split())
graph1 = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph1[u].append(v)
    graph1[v].append(u)



# print(graph1)

graph2 = defaultdict(list)








