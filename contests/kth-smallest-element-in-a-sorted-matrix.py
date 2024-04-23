class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        pq = []
        for i in range(n):
            for j in range(m):
                heapq.heappush(pq, matrix[i][j])

        
        for i in range(k - 1):
            heapq.heappop(pq)

        return heapq.heappop(pq)