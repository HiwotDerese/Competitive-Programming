class Solution:

    def hascycle(self, graph, color, ans, node):

        if color[node] == 1:
            print(node)
            return True

        if graph[node]:
            color[node] = 1

        for neighbor in graph[node]:
            if color[neighbor] != 2:
                if self.hascycle(graph, color, ans, neighbor):
                    return True

        color[node] = 2
        ans.append(node)
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        n = len(graph)
        color = [0] * n

        for i in range(n):
            if color[i] != 0:
                continue

            if not self.hascycle(graph, color, ans, i):
                ans.append(i)

        final = sorted(set(ans))
        return final