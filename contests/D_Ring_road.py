from collections import defaultdict

nodes = int(input())
adj = defaultdict(list)
c = {}
for _ in range(nodes):
    parent , child , cost = map(int , input().split())
    adj[parent].append(child)
    adj[child].append(parent)
    c[(child, parent)] = cost

seen =set()
costs = [0]
res = float('inf')
def dfs(node):
    
    seen.add(node)
    
    child1 , child2 = adj[node]
 
    if child1 not in seen:
        if (node , child1) in c:
            costs[0] += c[(node, child1)]
        dfs(child1)

    if child2 not in seen:
        if (node , child2) in c:
            costs[0] += c[(node, child2)]
        
        dfs(child2)

dfs(parent)
seen = set()
res = min(res, costs[0])
print(costs[0])
costs[0] = 0
a = adj[parent] 

a[0] , a[1] = a[1] , a[0]
dfs(parent)
res = min(res, costs[0])
print(costs[0])
# print(res)
            

    

