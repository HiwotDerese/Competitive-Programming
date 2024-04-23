from collections import defaultdict


n = int(input())
graph = defaultdict(list)
for _ in range(n):
    name1, reposted, name2 = input().split()
    # print(name1, reposted, name2)
    graph[name2.lower()].append(name1.lower())


def dfs(node, graph):
    if node not in graph:
        return 1
    
    else:
        max_ = 1
        for child in graph[node]:
            max_ = max(max_, 1 + dfs(child, graph))
        return max_



ans = 1

for node in graph["polycarp"]:
    ans = max(ans, 1 + dfs(node, graph))

print(ans)