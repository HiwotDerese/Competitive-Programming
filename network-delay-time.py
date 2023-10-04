class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = []

        for time in times:
            graph.append(time)

        dist = [inf] * n
        dist[k - 1] = 0

        for _ in range(n - 1):
            for u, v, w in graph:
                if dist[u - 1] != inf and dist[u - 1] + w < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + w

        print(dist)

        for i in range(n):
            if dist[i] == inf:
                return -1
        
        return max(dist)