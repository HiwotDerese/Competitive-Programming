class Solution:
    def paths(self,graph, path):
        if path[-1] == self.leng - 1:
            self.ans.append(path.copy())
            return

        for i in graph[path[-1]]:
            path.append(i)
            self.paths(graph, path)
            path.pop()


    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        self.leng = len(graph)
        self.paths(graph, [0])
        return self.ans