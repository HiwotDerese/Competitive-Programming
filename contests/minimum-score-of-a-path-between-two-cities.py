class Solution:
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y, weight):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            self.minimum[root_x] = min(self.minimum[root_x], weight)
            return 

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.minimum[root_x] = min(self.minimum[root_x], self.minimum[root_y], weight)

        else:
            self.parent[root_x] = root_y
            self.minimum[root_y] = min(self.minimum[root_x], self.minimum[root_y], weight)

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.minimum = [inf for i in range(n)]

        for edge in roads:
            self.union(edge[0] - 1, edge[1] - 1, edge[2])

        root = self.find(n - 1)
        return self.minimum[root]


















# class Solution:
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])

#         return self.parent[x]

#     def union(self, x, y):
#         root_x = self.find(x)
#         root_y = self.find(y)

#         if root_x == root_y:
#             return 

#         if self.rank[root_x] > self.rank[root_y]:
#             self.parent[root_y] = root_x

#         elif self.rank[root_x] < self.rank[root_y]:
#             self.parent[root_x] = root_y

#         else:
#             self.parent[root_y] = root_x
#             self.rank[root_x] += 1

#     def minScore(self, n: int, roads: List[List[int]]) -> int:
#         self.parent = [i for i in range(n)]
#         self.rank = [0] * n
#         min_ = inf

#         for edge in roads:
#             self.union(edge[0] - 1, edge[1] - 1)

#         for edge in roads:
#             if self.find(edge[0] - 1) == self.find(n - 1):
#                 min_ = min(min_, edge[2])

#         return min_