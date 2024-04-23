from collections import defaultdict

n = int(input())
k = int(input())
graph = defaultdict(list)

for i in range(k):
    operation = list(map(int, input().split()))

    # add(u, v) operation
    if operation[0] == 1:
        graph[operation[1]].append(operation[2])
        graph[operation[2]].append(operation[1])

    # vertex(u) operation
    else:
        # ans = graph[operation[1]]
        print(*graph[operation[1]])
