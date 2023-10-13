from cmath import inf
from collections import defaultdict, deque
import heapq

n, m = map(int, input().split())
graph = defaultdict(list)
flag = False

for _ in range(m):
    u,v,weight = map(int,input().split())
    graph[u].append((weight, v))
    graph[v].append((weight, u))

dist = [inf]*(n+1)
queue = [(0, 1)]
visited = set()
parent = [None]*(n+1)

while queue:
    weight, node = heapq.heappop(queue)
    if node == n:
        flag = True
        break

    if node not in visited:
        visited.add(node)

        for weightc, child in graph[node]:

            if child not in visited:
                sum_ = weight + weightc

                if sum_ < dist[child]:
                    dist[child] = sum_
                    heapq.heappush(queue, (sum_, child))
                    parent[child] = node

if flag == False:
    print(-1)

else:
    ans = [n]
    idx = n
    while parent[idx] != 1:
        ans.append(parent[idx])
        idx = parent[idx]

    ans.append(1)   
    print(*ans[::-1])




    # if node not in visited:
    #     visited.add(node)
 
    #     for child, child_weight in graph[node]:
    #         curr_weight = weight + child_weight
    #         if child not in visited:
    #             # print(child)
    #             if curr_weight < dist[child]:
    #                 dist[child] = curr_weight
    #                 parent[child] = node
    #                 heapq.heappush(queue,(child, curr_weight))





    











# from collections import defaultdict
# import heapq
 
 
# n,m = map(int,input().split())
# graph = defaultdict(list)
 
# for _ in range(m):
#     start,end,weight = map(int,input().split())
#     graph[start].append((weight,end))
#     graph[end].append((weight,start))
 
# distances = [float('inf')]*(n+1)
 
 
# queue = [(0,1)]
# visited = set()
# parent = [None]*(n+1)
# flag = False
# while queue:
#     weight,node = heapq.heappop(queue)
#     print(weight,node)
 
#     if node == n:
#         flag = True
#         break
 
#     if node not in visited:
#         visited.add(node)
 
#         for child_weight,child in graph[node]:
#             curr_weight = weight + child_weight
#             if child not in visited:
#                 if curr_weight < distances[child]:
#                     distances[child] = curr_weight
#                     parent[child] = node
#                     heapq.heappush(queue,(curr_weight,child))
 
# path = []
# curr_node = n
# if flag == False:
#     print(-1)
# else:
#     while curr_node != 1:
#         path.append(curr_node)
#         curr_node = parent[curr_node]
#     path.append(1)  
#     path.reverse() 
 
#     print(*path)



