class Solution:

    def dfs(self, graph, node, visited):

        if node in visited:
            return

        visited.add(node)

        if node in graph:
            for i in graph[node]:
                self.dfs(graph, i, visited)

 
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        arr = []
        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                r1, r2 = bombs[i][2], bombs[j][2]
                x1, x2 = bombs[i][0], bombs[j][0]
                y1, y2 = bombs[i][1], bombs[j][1]

                if (((x1 - x2) ** 2) + ((y2 - y1) ** 2)) <= r1 ** 2:
                    graph[i].append(j)

                if (((x1 - x2) ** 2) + ((y2 - y1) ** 2)) <= r2 ** 2:
                    graph[j].append(i)

        # print(graph)

        ans = 1
        for node in graph:
            visited = set()
            self.dfs(graph, node, visited)
            ans = max(ans, len(visited))


        return ans





        # return max(arr)