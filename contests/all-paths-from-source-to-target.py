class Solution:
    def paths(self,graph, path):
        if path[-1] == len(graph) - 1:
            self.ans.append(path)
            return

        for i in graph[path[-1]]:
            self.paths(graph, path + [i])

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        self.paths(graph, [0])
        return self.ans