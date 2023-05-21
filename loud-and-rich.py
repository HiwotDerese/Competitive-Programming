class Solution:

    def bfs(self, num, minm, adj, quiet):
        queue = deque([num])
        visited = set([num])

        while queue:
            n = queue.popleft()
            if quiet[n] < quiet[minm]:
                minm = n

            for i in adj[n]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

        return minm

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n, ans = len(quiet), []
        adj = defaultdict(list)
        
        for i in richer:
            adj[i[1]].append(i[0])

        for i in range(n):
            if i in adj:
                min_ = self.bfs(i, i, adj, quiet)
                ans.append(min_)

            else:
                ans.append(i)

        return ans