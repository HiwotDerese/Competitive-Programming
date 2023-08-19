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
            self.rank[root_x] += 1

        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        n = len(source)
        costs = []
        ans = 0
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

        for pair in allowedSwaps:
            self.union(pair[0], pair[1])

        map = {}
        for i in range(n):
            root = self.find(i)
            if root not in map:
                map[root] = defaultdict(int)

            map[root][source[i]] += 1

        # print(map)
        ans = 0
        # print(self.parent)
        for i in range(n):
            root = self.find(i)
            parent = map[root]

            if(target[i] in parent and parent[target[i]] > 0):
                parent[target[i]] -= 1

            else:
                ans += 1

            # print(parent)

        return ans