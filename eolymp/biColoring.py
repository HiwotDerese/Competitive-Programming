from collections import defaultdict

def dfs(node, color):
    if arr[node - 1] == 0:
        arr[node - 1] = color

    for i in graph[node]:
        if arr[i - 1] == color or (arr[i - 1] == 0 and not dfs(i, -color)):
            return False

    return True

while True:
    n = int(input())

    if n == 0:
        break

    e, graph = int(input()), defaultdict(list) 

    for i in range(e):
        edge = list(map(int, input().split()))
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    arr = [0]*n

    if dfs(1, 1):
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")

    


