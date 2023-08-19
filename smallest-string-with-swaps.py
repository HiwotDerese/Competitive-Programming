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

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        m = len(pairs)

        if not m:
            return s

        ans = [0] * n
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

        for pair in pairs:
            self.union(pair[0], pair[1])
            # print(self.parent)

        for i in range(m):
            self.find(pairs[i][0])
            self.find(pairs[i][1])

        # print(self.parent)

        graph = defaultdict(list)

        for i in range(n):
            graph[self.parent[i]].append(i)

        # print(graph)
        for node in graph:
            graph[node].sort()
            word = ""
            for i in graph[node]:
                word += s[i]
            w = sorted(word)

            for i in range(len(graph[node])):
                ans[graph[node][i]] = w[i]

        return ''.join(ans)