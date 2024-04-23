class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.graph = defaultdict(list)
        self.deaths = set()
        
    def birth(self, parentName: str, childName: str) -> None:

        self.graph[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.deaths.add(name)

    def getInheritanceOrder(self) -> List[str]:
        curOrder = []

        def dfs(node = self.kingName):
            # if node in self.curOrder:
            #     return
            if node not in self.deaths:
                curOrder.append(node)

            if node in self.graph:
                for i in self.graph[node]:
                    dfs(i)
        dfs()

        return curOrder

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()