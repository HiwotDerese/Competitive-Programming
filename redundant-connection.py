class Solution:

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            self.ans.append([x + 1, y + 1])
            return True
        
        else:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x

            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y

            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.ans = []
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

        for edge in edges:
            self.union(edge[0] - 1, edge[1] - 1)

        return self.ans[-1]