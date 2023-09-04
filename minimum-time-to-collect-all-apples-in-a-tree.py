class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(set)

        for x, y in edges:
            adj[x].add(y)
            adj[y].add(x)
        
        def dfs(parent, val):
            count = 0
            for neighbour in adj[val]:
                if neighbour != parent:
                    count += dfs(val, neighbour)

            if count > 0:
                if val > 0:
                    return count + 2
                else:
                    return count
            
            if hasApple[val] and val > 0:
                return 2
            
            return 0

        count = dfs(None, 0)

        return count