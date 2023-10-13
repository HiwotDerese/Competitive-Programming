from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph, m = defaultdict(list), len(edges)
        for i in range(m):
            prob = succProb[i]
            u, v = edges[i][0], edges[i][1]
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        # print(graph)

        dist = [0] * n
        dist[start_node] = 1

        max_heap = [(-1, start_node)]

        while max_heap:
            probability, node = heapq.heappop(max_heap)

            probability = -probability

            if node == end_node:
                return probability

            for neighbor, neighbor_prob in graph[node]:
                new_prob = probability * neighbor_prob

                if new_prob > dist[neighbor]:
                    dist[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))

        return dist[end_node]