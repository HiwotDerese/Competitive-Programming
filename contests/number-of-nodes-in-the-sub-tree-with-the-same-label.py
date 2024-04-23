class Solution:
    def dfs(self, node, graph, labels):
        curr = Counter()
        curr[labels[node]] = 1
        
        self.visited.add(node)
        for i in graph[node]:
            if i not in self.visited:
                curr += self.dfs(i, graph, labels)
        # print(curr, node, curr[node])
        self.ans[node] = curr[labels[node]]
        return curr

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.ans, self.visited = [0] * n, set()
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        self.dfs(0, graph, labels)

        return self.ans