class Solution:
    def findComponent(self, node, visited, graph):
        visited.add(node)

        for i in range(len(graph[node])):
            if graph[node][i] not in visited:
                self.findComponent(graph[node][i], visited, graph)



    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
        # print(graph)
        ans = 0
        visited = set()
        for node in graph:
            # print(node)
            if node not in visited:
                ans += 1
                self.findComponent(node, visited, graph)

        return ans