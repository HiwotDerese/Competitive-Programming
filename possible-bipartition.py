class Solution:
    def biPartition(self, graph, node, curr):
        if self.arr[node - 1] > 0:
            if curr == 0:
                self.arr[node - 1] = -1
                curr = -1

            else:
                self.arr[node - 1] = 0
                curr = 0

        for i in graph[node]:
            if self.arr[i - 1] == curr or self.arr[i - 1] > 0 and not self.biPartition(graph, i, curr):
                return False

        return True

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.arr = [1] * n

        graph = defaultdict(list)
        for i in range(len(dislikes)):
            graph[dislikes[i][0]].append(dislikes[i][1])
            graph[dislikes[i][1]].append(dislikes[i][0])

        self.curr = 0
        for node in graph:

            if self.arr[node - 1] > 0 and not self.biPartition(graph, node, self.curr):
                return False

        return True