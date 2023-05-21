from collections import defaultdict

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        edge = list(map(int, input().split()))
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    x, y = 0, 0
    for node in graph:
        if x and y:
            break
        n = graph[node]
        if len(n) > 1:
            for i in n:
                if len(graph[i]) == 1:
                    y = len(n) - 1
                else:
                    x = len(graph[i])

    print(x, y)