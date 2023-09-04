from cmath import inf
from collections import defaultdict

test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    s = list(input())
    graph = defaultdict(list)
    visited = {1}

    for idx in range(2, n + 1):
        graph[idx].append(a[idx - 2])
        graph[a[idx - 2]].append(idx)

    def dfs(node, parent, ans):
        print(node, parent)
        sum_ = inf 
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                if sum_ == inf:
                    sum_ = dfs(neighbour, node, ans)
                else:
                   sum_ += dfs(neighbour, node, ans)
        print(node, "kkkkkkk")
        if sum_ == 0:
            ans[0] += 1
         
        if s[node - 1] == "W":
            print(node, "node")
            return 1
        else:
            return -1

    ans = [0]
    dfs(1, None, ans)
    print(*ans)

