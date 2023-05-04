class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(n):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if x != y:
                new = y - x
                heapq.heappush(stones, new)            

        if stones:
            return -heapq.heappop(stones)

        return 0