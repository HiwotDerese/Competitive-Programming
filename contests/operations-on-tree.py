class LockingTree:

    def __init__(self, parent: List[int]):
        self.graph, n = defaultdict(list), len(parent)
        self.parent = parent

        for idx in range(n):
            self.graph[parent[idx]].append(idx)

        self.locks = {}

    def lock(self, num: int, user: int) -> bool:
        if num not in self.locks:
            self.locks[num] = user
            return True
        
        return False

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locks and self.locks[num] == user:
            del self.locks[num]
            return True
        return False

    def has_locked_ancestors(self, node):
        parent = self.parent[node]
        while parent != -1:
            if parent in self.locks:
                return True
            parent = self.parent[parent]
        return False

    def has_locked_descendants(self, node):
        for child in self.graph[node]:
            if child in self.locks or self.has_locked_descendants(child):
                return True
        return False

    def unlock_descendants(self, node):
        if node in self.locks:
            del self.locks[node]
            
        for child in self.graph[node]:
            self.unlock_descendants(child)

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locks:
            return False

        if self.has_locked_ancestors(num):
            return False

        if not self.has_locked_descendants(num):
            return False

        self.unlock_descendants(num)
        self.locks[num] = user
        return True