class Solution:

    def find(self, x):
        if self.parent[x] != x:
            return self.find(self.parent[x])

        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x ] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.minimum[root_x] = min(self.minimum[root_x], self.minimum[root_y])

        else:
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1

            self.parent[root_y] = root_x
            self.minimum[root_x] = min(self.minimum[root_x], self.minimum[root_y])
            

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n, m = len(s1), len(baseStr)

        self.parent = [i for i in range(26)]
        self.rank = [0] * 26
        self.minimum = [i for i in range(26)]


        for idx in range(n):
            self.union(ord(s1[idx]) - 97, ord(s2[idx]) - 97)

        ans = ""
        for i in range(m):
            root = self.find(ord(baseStr[i]) - 97)            
            ans += chr(self.minimum[root] + 97)

        return ans