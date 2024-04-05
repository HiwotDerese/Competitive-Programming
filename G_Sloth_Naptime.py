from collections import defaultdict, deque


n = int(input())
graph = defaultdict(list)
for i in range(n - 1):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)
    
def bfs(start,energy,destination):
    visited = {start}
    queue = deque()
    queue.append((start,energy))
    while queue:
        vertex,e  = queue.popleft()
        if (vertex == destination and e >= 0):
            return vertex
        
        if e > 0:
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor,e - 1))

    return vertex

q = int(input())	
for _ in range(q):
    a,b,c = list(map(int, input().split()))
    if a==b:
        print(b)
    else:
        print(bfs(a,c,b))


