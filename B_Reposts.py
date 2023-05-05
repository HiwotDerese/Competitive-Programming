from collections import defaultdict

test = int(input())
graph = defaultdict(list)
for _ in range(test):
    name1, repost, name2 = input().split()
    graph[name2.lower()].append(name1.lower())
# print(graph)

a = [0]
visited = set()
def dfs(node, count):
    visited.add(node)
    count  += 1
    a[0] = max(a[0], count)

    if node in graph:
        for i in graph[node]:
            if i not in visited:
                dfs(i, count)

for node in graph:
    dfs(node, 0)
    break

print(a[0])

    

