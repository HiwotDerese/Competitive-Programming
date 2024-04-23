
class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    
    def rep(self, x):
        if self.root[x] != x:
            self.root[x] = self.rep(self.root[x])
        return self.root[x]
    
    def getCost(self, x):
        root = self.rep(x)
        return self.cost[root]
     
    def getReps(self):
        return [i for i in range(len(self.root)) if self.root[i]==i]
    
    def areConnected(self, x, y):
        return self.rep(x) == self.rep(y)
    
    def allComponents(self):
        return [self.components(rep) for rep in self.getReps()]

    def components(self, x):
        root = self.rep(x)
        answer = []
        for i in range(len(self.root)):
            if self.rep(i) == root:
                answer.append(i)
        return answer

    def union(self, x, y):
        rootX = self.rep(x)
        rootY = self.rep(y)

        if rootX == rootY:
            return
        
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX

        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.rank[rootX] += 1
            self.root[rootY] = rootX

from collections import defaultdict

n_players, n_queries = list(map(int, input().split()))
teams = DisjointSet(n_players+1)
experience = defaultdict(int)

for _ in range(n_queries):
    temp = input().split()
    if len(temp) == 2:
        print(experience[int(temp[1])])
    else:
        if temp[0] == 'join':
            teams.union(int(temp[1]), int(temp[2]))
        else:
            other = teams.rep(int(temp[1]))
            for node in teams.components(int(temp[1])):
                experience[node] += int(temp[2])
