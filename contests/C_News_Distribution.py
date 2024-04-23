n, m = map(int, input().split())
parent = [i for i in range(n)]
rank = [0] * n
members = [1 for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return 
    
    elif rank[root_x] == rank[root_y]:
        rank[root_x] += 1

    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
        members[root_x] += members[root_y]

    else:
        parent[root_x] = root_y
        members[root_y] += members[root_x]

for _ in range(m):
    group = list(map(int, input().split()))
    if group[0] > 1:
        num = group[1]
        for i in range(2, group[0]+1):
            union(num - 1, group[i] - 1)

ans = []
for i in range(n):
    root = find(i)
    ans.append(str(members[root]))

print(' '.join(ans))
