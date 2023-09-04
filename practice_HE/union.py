class Solution:

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y

            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x

            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        leng = len(edges)

        for i in range(leng):
            self.union(edges[i][0], edges[i][1])

        source_p = self.find(source)
        destination_p = self.find(destination)
        2
        return source_p == destination_p





