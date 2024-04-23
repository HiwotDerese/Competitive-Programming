class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(set)
        n = len(routes)
        for i in range(n):
            m = len(routes[i])
            for j in range(m):
                graph[routes[i][j]].add(i)

        queue = deque([source])
        visited = set()
        ans = 0

        while queue:
            m = len(queue)
            for i in range(m):
                road = queue.popleft()
                if road == target:
                    return ans

                for neighbor in graph[road]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.extend(routes[neighbor])

            ans += 1

        return -1