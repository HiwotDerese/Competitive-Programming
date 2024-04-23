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

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        costs = []
        ans = 0
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        for i in range(n):
            self.rank[i] = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                point1 = points[i]
                point2 = points[j]
                dis = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                costs.append((dis, i, j))

        # print(costs)
        heapq.heapify(costs)
        # print(costs)

        while costs:
            min_cost = heapq.heappop(costs)
            # print(min_cost)
            root_x = self.find(min_cost[1])
            root_y = self.find(min_cost[2])
            if self.parent[root_x] != self.parent[root_y]:
                # print(min_cost, "min")
                self.union(min_cost[1], min_cost[2])
                ans += min_cost[0]


        return ans