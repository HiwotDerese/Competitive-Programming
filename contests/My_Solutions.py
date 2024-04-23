from collections import defaultdict

def bicolor(graph, node, curr, color):
    if curr == 0:
        color[node - 1] = -1
        curr = -1
    else:
        color[node - 1] = 0
        curr = 0

    for i in graph[node]:
        if color[i - 1] == curr or color[i - 1] > 0 and not bicolor(graph, i, curr, color):
            return "NOT BICOLOURABLE."
        
    return "BICOLOURABLE."

test = 1
while test:
    test = int(input())
    
    if test:
        graph = defaultdict(list)
        nodes = test
        edges = int(input())

        for i in range(edges):
            edge = list(map(int, input().split()))
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        color = [1]*nodes
        curr = 0

        print(bicolor(graph, 1, curr, color))
        

    else:
        break
                

