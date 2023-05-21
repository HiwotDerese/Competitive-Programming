class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj, n = defaultdict(list), len(adjacentPairs) + 1
        visited = set()

        for edge in adjacentPairs:
            adj[edge[1]].append(edge[0])
            adj[edge[0]].append(edge[1])

        stack = []
        for x in adj:
            if len(adj[x]) == 1:
                stack.append(x)
                break

        ans = []
        while stack:
            num = stack.pop()
            visited.add(num)
            ans.append(num)

            for neighbor in adj[num]:
                if neighbor not in visited:
                    stack.append(neighbor)

        return ans