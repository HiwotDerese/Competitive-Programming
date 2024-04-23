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

    def equationsPossible(self, equations: List[str]) -> bool:
        self.parent = [i for i in range(26)]
        self.rank = [0 for i in range(26)]

        for eq in equations:
            if eq[1] == "=":
                self.union(ord(eq[0]) - 97, ord(eq[3]) - 97)

        for eq in equations:
            if eq[1] == "!":
                root1 = self.find(ord(eq[0]) - 97)
                root2 = self.find(ord(eq[3]) - 97)

                if root1 == root2:
                    return False

        return True