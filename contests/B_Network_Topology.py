from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dic = {1:0, 2:0, 3:0}
for i in range(1, n + 1):
    if len(graph[i]) == 1:
        dic[1] += 1
    elif len(graph[i]) == 2:
        dic[2] += 1
    else:   
        dic[3] += 1


if dic[1] == 2 and dic[2] == n - 2: 
    print("bus topology")

elif dic[1] == 0 and dic[2] == n:
    print("ring topology")

elif dic[1] == n - 1 and dic[3] == 1:   
    print("star topology")

else:   
    print("unknown topology")

  