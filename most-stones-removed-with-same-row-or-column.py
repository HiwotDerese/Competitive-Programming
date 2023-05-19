class Solution:

    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return 

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x

        else:
            self.parent[root_x] = root_y

    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        self.parent = {}
        self.rank = {}
        components = defaultdict(list)

        for stone in stones:
            self.parent[tuple(stone)] = tuple(stone)
            self.rank[tuple(stone)] = 0

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.union(tuple(stones[i]), tuple(stones[j]))

        for i in self.parent:
            self.parent[i] = self.find(i)

        for i in self.parent:
            components[self.parent[i]].append(i)

        m = len(components)

        return n - m